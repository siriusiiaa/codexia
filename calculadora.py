"""
Calculadora Simple - Ejemplo básico con Claude Code
====================================================

Este módulo demuestra operaciones básicas de una calculadora.
"""


def sumar(a, b):
    """Suma dos números."""
    return a + b


def restar(a, b):
    """Resta dos números."""
    return a - b


def multiplicar(a, b):
    """Multiplica dos números."""
    return a * b


def dividir(a, b):
    """Divide dos números.

    Args:
        a: Numerador
        b: Denominador

    Returns:
        Resultado de la división

    Raises:
        ValueError: Si el denominador es cero
    """
    if b == 0:
        raise ValueError("No se puede dividir por cero")
    return a / b


def potencia(base, exponente):
    """Calcula la potencia de un número."""
    return base ** exponente


def raiz_cuadrada(n):
    """Calcula la raíz cuadrada de un número.

    Args:
        n: Número del cual calcular la raíz

    Returns:
        Raíz cuadrada del número

    Raises:
        ValueError: Si el número es negativo
    """
    if n < 0:
        raise ValueError("No se puede calcular la raíz cuadrada de un número negativo")
    return n ** 0.5
