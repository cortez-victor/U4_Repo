"""interpolacion_lineal — cuaderno 01.

Libro: ecuación (18.2). Recta por dos nodos, evaluada en ``x``.

La función devuelve **dos** cosas: el valor interpolado y el error. El error es
``None`` cuando no se da un tercer dato; si se da, se estima con (18.18).
"""

from ejercicios.interpolacion.error_estimado_interpolacion import (
    error_estimado_interpolacion,
)

def interpolacion_lineal(x0, y0, x1, y1, x, x2=None, y2=None):

    # Ecuación (18.2): Interpolación lineal
    y = y0 + ((y1 - y0) / (x1 - x0)) * (x - x0)

    # Error estimado
    error = None

    if x2 is not None and y2 is not None:
        error = error_estimado_interpolacion(
            x0, y0, x1, y1, x2, y2, x
        )

    return y, error

if __name__ == "__main__":
    # Sin tercer dato
    print(interpolacion_lineal(1, 0, 4, 3, 2))

    # Con tercer dato
    print(interpolacion_lineal(1, 0, 4, 3, 2, x2=6, y2=5))
