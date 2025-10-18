# codexia

Script en Python para resolver problemas de **programación lineal** usando
el método símplex. No requiere librerías externas y puede ejecutarse desde
la línea de comandos para resolver un problema definido en formato JSON o
probar el ejemplo incluido.

## Uso

### Resolver el ejemplo incluido

```bash
python linear_programming.py --example
```

### Resolver un problema desde un archivo JSON

El archivo debe contener un objeto con el vector objetivo y la lista de
restricciones en el siguiente formato:

```json
{
  "objective": [3, 5],
  "constraints": [
    {"coefficients": [2, 1], "bound": 14},
    {"coefficients": [1, 3], "bound": 18},
    {"coefficients": [2, 3], "bound": 24}
  ]
}
```

Una vez creado el archivo (por ejemplo `problema.json`), ejecute:

```bash
python linear_programming.py problema.json
```

Use la opción `--as-json` si desea obtener el resultado en formato JSON.
