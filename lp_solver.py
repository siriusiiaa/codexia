"""Script sencillo para resolver problemas de programación lineal usando el método Simplex.

El script admite problemas de maximización con restricciones tipo `<=`, `>=` o `=`.
Por defecto ejecuta un ejemplo básico, pero también puede leer un archivo JSON con el
formato:

{
  "objective": [c1, c2, ...],
  "constraints": [
    {"coefficients": [a11, a12, ...], "sense": "<=", "rhs": b1},
    ...
  ]
}

El número de coeficientes en cada restricción debe coincidir con los del vector objetivo.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from typing import List, Optional, Tuple

BIG_M = 1e6


@dataclass
class Constraint:
    coefficients: List[float]
    sense: str  # one of '<=', '>=', '='
    rhs: float

    def normalized(self) -> "Constraint":
        """Devuelve la restricción con un RHS no negativo.

        Si el término independiente es negativo, multiplica todo por -1 y adapta el signo.
        """
        if self.rhs >= 0:
            return self
        flipped_sense = {"<=": ">=", ">=": "<=", "=": "="}[self.sense]
        negated_coeffs = [-c for c in self.coefficients]
        return Constraint(negated_coeffs, flipped_sense, -self.rhs)


@dataclass
class LinearProgrammingProblem:
    objective: List[float]
    constraints: List[Constraint]

    @classmethod
    def from_json(cls, path: str) -> "LinearProgrammingProblem":
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        constraints = [Constraint(**item).normalized() for item in data["constraints"]]
        return cls(objective=data["objective"], constraints=constraints)


class SimplexSolver:
    def __init__(self, problem: LinearProgrammingProblem):
        self.problem = problem
        self.num_original_vars = len(problem.objective)

        self.tableau: List[List[float]] = []
        self.basic_vars: List[int] = []
        self.var_names: List[str] = []

    def _build_tableau(self) -> None:
        rows: List[List[float]] = []
        var_index = 0
        self.var_names = [f"x{i+1}" for i in range(self.num_original_vars)]

        # Reserve space for original variables.
        for _ in self.problem.objective:
            var_index += 1

        # Agregar restricciones con variables de holgura/superávit y artificiales.
        for constraint in self.problem.constraints:
            row = list(constraint.coefficients)

            # Expandir fila con columnas futuras.
            row.extend([0.0] * len(self.problem.constraints))
            row.append(constraint.rhs)

            if constraint.sense == "<=":
                slack_col = var_index
                row[slack_col] = 1.0
                self.var_names.append(f"s{len(self.var_names)-self.num_original_vars+1}")
                self.basic_vars.append(slack_col)
                var_index += 1
            elif constraint.sense == ">=":
                surplus_col = var_index
                artificial_col = var_index + 1
                row[surplus_col] = -1.0
                row[artificial_col] = 1.0
                self.var_names.extend(
                    [
                        f"e{len(self.var_names)-self.num_original_vars+1}",
                        f"a{len(self.var_names)-self.num_original_vars+1}",
                    ]
                )
                self.basic_vars.append(artificial_col)
                var_index += 2
            elif constraint.sense == "=":
                artificial_col = var_index
                row[artificial_col] = 1.0
                self.var_names.append(f"a{len(self.var_names)-self.num_original_vars+1}")
                self.basic_vars.append(artificial_col)
                var_index += 1
            else:
                raise ValueError(f"Sentido desconocido: {constraint.sense}")

            rows.append(row)

        total_vars = var_index
        # Asegurar longitud uniforme.
        for r in rows:
            if len(r) < total_vars + 1:
                missing = total_vars + 1 - len(r)
                r[-1:-1] = [0.0] * missing

        # Fila objetivo con penalización Big-M para variables artificiales.
        obj_row = [-c for c in self.problem.objective]
        obj_row.extend([0.0] * (total_vars - len(obj_row)))
        obj_row.append(0.0)

        artificial_indices = [i for i, name in enumerate(self.var_names) if name.startswith("a")]
        for i, row in enumerate(rows):
            if self.basic_vars[i] in artificial_indices:
                for j in range(total_vars + 1):
                    obj_row[j] += BIG_M * row[j]

        self.tableau = rows + [obj_row]

    def _pivot(self, pivot_row: int, pivot_col: int) -> None:
        pivot_element = self.tableau[pivot_row][pivot_col]
        if abs(pivot_element) < 1e-12:
            raise ZeroDivisionError("Elemento pivote cercano a cero")

        self.tableau[pivot_row] = [v / pivot_element for v in self.tableau[pivot_row]]

        for r, row in enumerate(self.tableau):
            if r == pivot_row:
                continue
            factor = row[pivot_col]
            self.tableau[r] = [val - factor * self.tableau[pivot_row][c] for c, val in enumerate(row)]

        self.basic_vars[pivot_row] = pivot_col

    def _choose_pivot(self) -> Optional[Tuple[int, int]]:
        last_row = self.tableau[-1]
        # Variable entrante: coeficiente más negativo en función objetivo.
        pivot_col = min(range(len(last_row) - 1), key=lambda c: last_row[c])
        if last_row[pivot_col] >= -1e-9:
            return None

        ratios = []
        for i, row in enumerate(self.tableau[:-1]):
            if row[pivot_col] > 1e-9:
                ratios.append((row[-1] / row[pivot_col], i))
        if not ratios:
            raise ValueError("Problema no acotado: no hay fila saliente")

        _, pivot_row = min(ratios, key=lambda x: (x[0], self.basic_vars[x[1]]))
        return pivot_row, pivot_col

    def solve(self) -> Tuple[str, Optional[float], Optional[List[float]]]:
        self._build_tableau()

        while True:
            pivot = self._choose_pivot()
            if pivot is None:
                break
            self._pivot(*pivot)

        solution = [0.0] * len(self.var_names)
        for row_idx, var_idx in enumerate(self.basic_vars):
            solution[var_idx] = self.tableau[row_idx][-1]

        optimum_value = self.tableau[-1][-1]
        # Solo devolver las variables originales.
        original_solution = solution[: self.num_original_vars]

        return "optimal", optimum_value, original_solution


def default_problem() -> LinearProgrammingProblem:
    constraints = [
        Constraint([2, 1], "<=", 18),
        Constraint([2, 3], "<=", 42),
        Constraint([3, 1], "<=", 24),
    ]
    objective = [3, 2]  # Maximizar 3x1 + 2x2
    return LinearProgrammingProblem(objective=objective, constraints=constraints)


def main() -> None:
    parser = argparse.ArgumentParser(description="Resolver programación lineal por Simplex")
    parser.add_argument(
        "--file",
        type=str,
        help="Ruta a un JSON con la definición del problema. Si se omite, se usa un ejemplo.",
    )
    args = parser.parse_args()

    if args.file:
        problem = LinearProgrammingProblem.from_json(args.file)
    else:
        problem = default_problem()

    solver = SimplexSolver(problem)
    status, optimum, solution = solver.solve()

    print("Estado:", status)
    if optimum is not None:
        print("Valor óptimo:", optimum)
    if solution is not None:
        for i, value in enumerate(solution, start=1):
            print(f"x{i} = {value}")


if __name__ == "__main__":
    main()
