# codexia

Código generado con Codex IA

## Script de programación lineal

El repositorio incluye `lp_solver.py`, un script en Python que resuelve problemas de programación lineal de maximización usando el método Simplex con penalización Big-M.

### Requisitos
- Python 3.10 o superior (no requiere dependencias externas).

### Uso
1. Ejecuta el ejemplo predeterminado:

   ```bash
   python lp_solver.py
   ```

2. Usa un archivo JSON personalizado:

   ```bash
   python lp_solver.py --file problema.json
   ```

   Formato esperado del archivo `problema.json`:

   ```json
   {
     "objective": [3, 2],
     "constraints": [
       {"coefficients": [2, 1], "sense": "<=", "rhs": 18},
       {"coefficients": [2, 3], "sense": "<=", "rhs": 42},
       {"coefficients": [3, 1], "sense": "<=", "rhs": 24}
     ]
   }
   ```

El script mostrará el estado, el valor óptimo y el valor de cada variable de decisión.
