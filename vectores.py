def suma(v1, v2):
    return tuple(a + b for a, b in zip(v1, v2))


def resta(v1, v2):
    return tuple(a - b for a, b in zip(v1, v2))


def escalar(k, v):
    return tuple(k * a for a in v)


def mostrar_resultados():
    
    print("\n--- SUMA DE VECTORES ---")
    sumas = [
        ((2, 3), (1, 2)),
        ((4, 1), (2, 3)),
        ((-2, 3), (3, -1)),
        ((1, 4), (-2, 2)),
        ((3, -2), (-1, 4))
    ]

    for i, (v1, v2) in enumerate(sumas, 1):
        print(f"Ejercicio {i}: {v1} + {v2} = {suma(v1, v2)}")


    print("\n--- RESTA DE VECTORES ---")
    restas = [
        ((3, 2), (1, 4)),
        ((5, 3), (2, 1)),
        ((-1, 4), (3, 2)),
        ((2, -3), (1, -2)),
        ((-3, -2), (2, 3))
    ]

    for i, (v1, v2) in enumerate(restas, 1):
        print(f"Ejercicio {i}: {v1} - {v2} = {resta(v1, v2)}")


    print("\n--- PRODUCTO POR ESCALAR ---")
    escalares = [
        (2, (2, 1)),
        (0.5, (4, 2)),
        (-1, (2, 3)),
        (3, (-1, 2)),
        (-2, (3, -1))
    ]

    for i, (k, v) in enumerate(escalares, 1):
        print(f"Ejercicio {i}: {k} * {v} = {escalar(k, v)}")

if __name__ == "__main__":
    mostrar_resultados()


