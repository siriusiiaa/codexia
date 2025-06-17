"""Ejemplos de uso de operadores logicos en Python."""

def evaluar_logica(a: bool, b: bool, c: bool) -> dict:
    """Devuelve un diccionario con el resultado de operaciones logicas."""
    resultados = {
        'a_and_b': a and b,
        'a_or_b': a or b,
        'not_c': not c,
        'a_and_b_or_not_c': (a and b) or (not c),
        'a_or_b_and_c': a or (b and c),
        'doble_negacion_a': not not a,
    }
    return resultados


def main():
    casos = [
        (True, True, False),
        (False, True, True),
        (False, False, False),
    ]

    for i, (a, b, c) in enumerate(casos, 1):
        print(f"Caso {i}: a={a}, b={b}, c={c}")
        resultados = evaluar_logica(a, b, c)
        for nombre, valor in resultados.items():
            print(f"  {nombre}: {valor}")
        print()


if __name__ == "__main__":
    main()
