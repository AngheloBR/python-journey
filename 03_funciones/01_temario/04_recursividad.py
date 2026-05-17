# ══════════════════════════════════════════════════════════════
#  Python Journey — by AngheloBR
#  Módulo 03: Funciones
#  Tema 04: Recursividad
# ══════════════════════════════════════════════════════════════


# ─────────────────────────────────────────
#  ¿Qué es la recursividad?
# ─────────────────────────────────────────
# Una función recursiva es aquella que se llama a sí misma.
# Es útil para resolver problemas que se pueden dividir
# en versiones más pequeñas del mismo problema.
#
# Toda función recursiva necesita:
#   1. Caso base  → condición que detiene la recursión
#   2. Caso recursivo → la función se llama a sí misma


# ─────────────────────────────────────────
#  Ejemplo clásico — factorial
# ─────────────────────────────────────────
# 5! = 5 x 4 x 3 x 2 x 1 = 120
# 0! = 1 (por definición)

def factorial(n):
    if n == 0:       # caso base
        return 1
    return n * factorial(n - 1)   # caso recursivo

print(factorial(5))   # 120
print(factorial(0))   # 1
print(factorial(3))   # 6

# Cómo funciona factorial(3):
#   factorial(3) → 3 * factorial(2)
#   factorial(2) → 2 * factorial(1)
#   factorial(1) → 1 * factorial(0)
#   factorial(0) → 1  ← caso base
#   vuelve: 1 * 1 = 1
#   vuelve: 2 * 1 = 2
#   vuelve: 3 * 2 = 6


# ─────────────────────────────────────────
#  Ejemplo — cuenta regresiva
# ─────────────────────────────────────────
def cuenta_regresiva(n):
    if n == 0:          # caso base
        print("¡Despegue!")
        return
    print(n)
    cuenta_regresiva(n - 1)   # caso recursivo

cuenta_regresiva(5)
# 5 4 3 2 1 ¡Despegue!


# ─────────────────────────────────────────
#  Ejemplo — suma recursiva
# ─────────────────────────────────────────
def sumar_hasta(n):
    if n == 0:       # caso base
        return 0
    return n + sumar_hasta(n - 1)

print(sumar_hasta(5))   # 15  (5+4+3+2+1+0)


# ─────────────────────────────────────────
#  Ejemplo — Fibonacci
# ─────────────────────────────────────────
# 0, 1, 1, 2, 3, 5, 8, 13, 21...
# Cada número es la suma de los dos anteriores.

def fibonacci(n):
    if n <= 1:          # caso base
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

for i in range(10):
    print(fibonacci(i), end=" ")
# 0 1 1 2 3 5 8 13 21 34


# ─────────────────────────────────────────
#  ⚠️ Límite de recursión
# ─────────────────────────────────────────
# Python tiene un límite de recursión (por defecto ~1000 llamadas).
# Si lo superas, lanza RecursionError.

# import sys
# print(sys.getrecursionlimit())   # 1000

# Para problemas grandes, es mejor usar un bucle.


# ─────────────────────────────────────────
#  Recursión vs iteración
# ─────────────────────────────────────────
# Recursión   → más elegante, más fácil de leer en ciertos problemas
# Iteración   → más eficiente en memoria y velocidad

# factorial con bucle (iterativo)
def factorial_iterativo(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

print(factorial_iterativo(5))   # 120


# ─────────────────────────────────────────
#  Resumen rápido
# ─────────────────────────────────────────
#   Recursividad → función que se llama a sí misma
#   Caso base    → condición que detiene la recursión (obligatorio)
#   Caso recursivo → la función avanza hacia el caso base
#
#   Sin caso base → RecursionError (bucle infinito)
#   Para problemas grandes → preferir iteración
