"""Herramientas básicas para resolver problemas de programación lineal.

Este módulo implementa el método símplex en su forma estándar para
problemas de maximización con restricciones del tipo ``Ax ≤ b`` y
variables no negativas. También incluye una interfaz de línea de
comandos que permite cargar una descripción del problema en formato
JSON o ejecutar un ejemplo incluido.

El objetivo es ofrecer un script autónomo sin dependencias externas
que pueda utilizarse como punto de partida en cursos o proyectos
introductorios de programación lineal.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, List, Optional
import argparse
import json
import sys


@dataclass
class SimplexResult:
    """Resultado de la ejecución del algoritmo símplex."""

    status: str
    optimal_value: Optional[float] = None
    solution: Optional[List[float]] = None
    iterations: int = 0

    def to_dict(self) -> Dict[str, Any]:
        """Convierte el resultado a un diccionario serializable."""

        data: Dict[str, Any] = {
            "status": self.status,
            "iterations": self.iterations,
        }
        if self.optimal_value is not None:
            data["optimal_value"] = self.optimal_value
        if self.solution is not None:
            data["solution"] = self.solution
        return data


class LinearProgrammingProblem:
    """Representa un problema de programación lineal estándar."""

    def __init__(self, objective: List[float], coefficients: List[List[float]], bounds: List[float]):
        if not coefficients or not coefficients[0]:
            raise ValueError("La matriz de coeficientes no puede estar vacía")

        if len(objective) != len(coefficients[0]):
            raise ValueError("La dimensión del vector objetivo no coincide con la matriz de coeficientes")

        if len(coefficients) != len(bounds):
            raise ValueError("Cada restricción debe tener un límite (b)")

        if any(b < 0 for b in bounds):
            raise ValueError(
                "El método implementado requiere límites no negativos. "
                "Multiplique por -1 las restricciones con b negativo antes de resolver."
            )

        self.objective = objective
        self.coefficients = coefficients
        self.bounds = bounds

    def solve(self) -> SimplexResult:
        """Resuelve el problema usando el método símplex."""

        solver = _SimplexSolver(self.coefficients, self.bounds, self.objective)
        return solver.solve()


class _SimplexSolver:
    """Implementación interna del método símplex."""

    def __init__(self, A: List[List[float]], b: List[float], c: List[float]):
        self.A = A
        self.b = b
        self.c = c
        self.m = len(A)
        self.n = len(A[0])
        self.tableau = self._build_tableau()
        self.basis = [self.n + i for i in range(self.m)]

    def _build_tableau(self) -> List[List[float]]:
        columns = self.n + self.m + 1  # variables + holguras + términos independientes
        tableau = [[0.0 for _ in range(columns)] for _ in range(self.m + 1)]

        for i in range(self.m):
            for j in range(self.n):
                tableau[i][j] = float(self.A[i][j])
            tableau[i][self.n + i] = 1.0  # variable de holgura
            tableau[i][-1] = float(self.b[i])

        for j in range(self.n):
            tableau[-1][j] = -float(self.c[j])

        return tableau

    def solve(self) -> SimplexResult:
        iterations = 0

        while True:
            entering = self._choose_entering_variable()
            if entering is None:
                solution = self._extract_solution()
                optimal_value = self.tableau[-1][-1]
                return SimplexResult("optimal", optimal_value, solution, iterations)

            leaving = self._choose_leaving_variable(entering)
            if leaving is None:
                return SimplexResult("unbounded", iterations=iterations)

            self._pivot(leaving, entering)
            self.basis[leaving] = entering
            iterations += 1

    def _choose_entering_variable(self) -> Optional[int]:
        objective_row = self.tableau[-1]
        entering: Optional[int] = None
        for j, value in enumerate(objective_row[:-1]):
            if value < -1e-9:  # Selecciona el coeficiente más negativo
                entering = j
                break
        return entering

    def _choose_leaving_variable(self, entering: int) -> Optional[int]:
        min_ratio = float("inf")
        pivot_row: Optional[int] = None
        for i in range(self.m):
            coefficient = self.tableau[i][entering]
            if coefficient > 1e-9:
                ratio = self.tableau[i][-1] / coefficient
                if ratio < min_ratio - 1e-12:
                    min_ratio = ratio
                    pivot_row = i
        return pivot_row

    def _pivot(self, row: int, col: int) -> None:
        pivot_value = self.tableau[row][col]
        if abs(pivot_value) < 1e-12:
            raise ZeroDivisionError("Intento de pivoteo con valor nulo")

        # Normaliza la fila pivote
        self.tableau[row] = [value / pivot_value for value in self.tableau[row]]

        # Elimina la columna pivote del resto de filas
        for i in range(len(self.tableau)):
            if i == row:
                continue
            factor = self.tableau[i][col]
            self.tableau[i] = [
                current - factor * pivot
                for current, pivot in zip(self.tableau[i], self.tableau[row])
            ]

    def _extract_solution(self) -> List[float]:
        solution = [0.0 for _ in range(self.n)]
        for row_index, column in enumerate(self.basis):
            if column < self.n:
                solution[column] = self.tableau[row_index][-1]
        return solution


def _load_problem_from_json(path: str) -> LinearProgrammingProblem:
    with open(path, "r", encoding="utf-8") as fh:
        data = json.load(fh)

    try:
        objective = data["objective"]
        constraints = data["constraints"]
    except KeyError as exc:
        raise ValueError("El archivo JSON debe contener 'objective' y 'constraints'") from exc

    coefficients: List[List[float]] = []
    bounds: List[float] = []
    for constraint in constraints:
        coefficients.append(constraint["coefficients"])
        bounds.append(constraint["bound"])

    return LinearProgrammingProblem(objective, coefficients, bounds)


def _example_problem() -> LinearProgrammingProblem:
    objective = [3, 5]
    coefficients = [
        [2, 1],
        [1, 3],
        [2, 3],
    ]
    bounds = [14, 18, 24]
    return LinearProgrammingProblem(objective, coefficients, bounds)


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Resolver problemas de programación lineal con el método símplex")
    parser.add_argument(
        "path",
        nargs="?",
        help="Ruta a un archivo JSON que describa el problema",
    )
    parser.add_argument(
        "--example",
        action="store_true",
        help="Resuelve un problema de ejemplo para demostrar el funcionamiento",
    )
    parser.add_argument(
        "--as-json",
        action="store_true",
        help="Muestra el resultado en formato JSON",
    )
    return parser


def main(argv: Optional[List[str]] = None) -> int:
    parser = _build_parser()
    args = parser.parse_args(argv)

    if args.example:
        problem = _example_problem()
    elif args.path:
        try:
            problem = _load_problem_from_json(args.path)
        except (OSError, ValueError) as exc:
            parser.error(str(exc))
            return 2
    else:
        parser.print_help(sys.stderr)
        return 1

    result = problem.solve()

    if args.as_json:
        print(json.dumps(result.to_dict(), indent=2, ensure_ascii=False))
    else:
        print(f"Estado: {result.status}")
        if result.status == "optimal":
            print("Valor óptimo:", result.optimal_value)
            print("Solución:", ", ".join(f"x{i+1} = {value:.4f}" for i, value in enumerate(result.solution or [])))
        print("Iteraciones:", result.iterations)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
