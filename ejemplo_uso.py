#!/usr/bin/env python3
"""
Ejemplo de uso de la calculadora
=================================

Este script demuestra cómo usar las funciones de la calculadora.
"""

from calculadora import sumar, restar, multiplicar, dividir, potencia, raiz_cuadrada


def main():
    print("=" * 50)
    print("CALCULADORA - Ejemplo de uso con Claude Code")
    print("=" * 50)
    print()

    # Operaciones básicas
    print("📊 Operaciones Básicas:")
    print(f"  5 + 3 = {sumar(5, 3)}")
    print(f"  10 - 4 = {restar(10, 4)}")
    print(f"  6 × 7 = {multiplicar(6, 7)}")
    print(f"  20 ÷ 4 = {dividir(20, 4)}")
    print()

    # Operaciones avanzadas
    print("🔬 Operaciones Avanzadas:")
    print(f"  2³ = {potencia(2, 3)}")
    print(f"  5² = {potencia(5, 2)}")
    print(f"  √16 = {raiz_cuadrada(16)}")
    print(f"  √25 = {raiz_cuadrada(25)}")
    print()

    # Ejemplo de manejo de errores
    print("⚠️  Manejo de Errores:")
    try:
        resultado = dividir(10, 0)
    except ValueError as e:
        print(f"  Error al dividir por cero: {e}")

    try:
        resultado = raiz_cuadrada(-4)
    except ValueError as e:
        print(f"  Error con número negativo: {e}")
    print()

    # Cálculos combinados
    print("🧮 Cálculos Combinados:")
    resultado1 = multiplicar(sumar(3, 2), 4)
    print(f"  (3 + 2) × 4 = {resultado1}")

    resultado2 = dividir(potencia(2, 4), 4)
    print(f"  2⁴ ÷ 4 = {resultado2}")

    resultado3 = raiz_cuadrada(sumar(9, 16))
    print(f"  √(9 + 16) = {resultado3}")
    print()

    print("=" * 50)
    print("✅ Ejemplo completado exitosamente!")
    print("=" * 50)


if __name__ == "__main__":
    main()
