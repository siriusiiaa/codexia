# 🧮 Codexia - Calculadora con Claude Code

Código generado con Claude Code - Ejemplo básico para comenzar a usar la plataforma web

## 📋 Descripción

Este proyecto es un **ejemplo básico** que demuestra las capacidades de Claude Code para:
- ✍️ Crear y organizar archivos de código
- 🧪 Escribir tests automatizados
- 📚 Generar documentación clara
- 🔧 Estructurar proyectos de software

## 📁 Estructura del Proyecto

```
codexia/
├── calculadora.py       # Módulo principal con operaciones matemáticas
├── test_calculadora.py  # Tests unitarios con pytest
├── ejemplo_uso.py       # Script de demostración
└── README.md           # Este archivo
```

## 🚀 Uso Rápido

### Ejecutar el ejemplo:

```bash
python ejemplo_uso.py
```

### Ejecutar los tests:

```bash
# Instalar pytest si no lo tienes
pip install pytest

# Ejecutar tests
pytest test_calculadora.py -v
```

## 💡 Funcionalidades

El módulo `calculadora.py` incluye:

| Función | Descripción | Ejemplo |
|---------|-------------|---------|
| `sumar(a, b)` | Suma dos números | `sumar(5, 3) → 8` |
| `restar(a, b)` | Resta dos números | `restar(10, 4) → 6` |
| `multiplicar(a, b)` | Multiplica dos números | `multiplicar(6, 7) → 42` |
| `dividir(a, b)` | Divide dos números | `dividir(20, 4) → 5.0` |
| `potencia(base, exp)` | Calcula potencias | `potencia(2, 3) → 8` |
| `raiz_cuadrada(n)` | Calcula raíz cuadrada | `raiz_cuadrada(16) → 4.0` |

## 📝 Ejemplo de Código

```python
from calculadora import sumar, multiplicar, potencia

# Operaciones simples
resultado = sumar(5, 3)  # 8

# Operaciones combinadas
resultado = multiplicar(sumar(3, 2), 4)  # (3 + 2) × 4 = 20

# Potencias
resultado = potencia(2, 4)  # 2⁴ = 16
```

## 🧪 Tests Incluidos

Los tests verifican:
- ✅ Operaciones matemáticas correctas
- ✅ Manejo de casos especiales (ceros, negativos)
- ✅ Manejo de errores (división por cero, raíz de negativos)

## 🎯 Qué Aprendiste sobre Claude Code

Este ejemplo demuestra cómo Claude Code puede:

1. **Crear proyectos completos** desde cero
2. **Escribir código bien documentado** con docstrings
3. **Generar tests automáticos** con buenas prácticas
4. **Estructurar código limpio** siguiendo convenciones Python
5. **Manejar errores** de forma apropiada
6. **Documentar proyectos** de forma clara y profesional

## 🔧 Requisitos

- Python 3.6+
- pytest (solo para ejecutar tests)

## 📚 Próximos Pasos

Ahora que conoces lo básico, puedes:
- Agregar más operaciones matemáticas
- Crear una interfaz gráfica con tkinter
- Implementar una calculadora científica
- Agregar soporte para expresiones complejas
- Exportar resultados a archivos

## 🤖 Generado con Claude Code

Este proyecto fue creado completamente usando Claude Code en la plataforma web, demostrando la capacidad de la IA para generar código funcional, bien estructurado y documentado. 
