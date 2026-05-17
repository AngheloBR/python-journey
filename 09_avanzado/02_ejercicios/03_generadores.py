# ══════════════════════════════════════════════════════════════
#  Python Journey — by AngheloBR
#  Módulo 09: Avanzado
#  Ejercicios 03: Generadores
# ══════════════════════════════════════════════════════════════
#
#  Lee cada enunciado, escribe tu solución debajo.
#  Si no puedes, revisa el temario primero.
#  Si aún no puedes, revisa soluciones/03_generadores.py
# ══════════════════════════════════════════════════════════════


# ─────────────────────────────────────────
#  Ejercicio 1
# ─────────────────────────────────────────
# Crea un generador "pares(n)" que produzca
# los números pares del 0 hasta n.
# Pruébalo con un for.

# TU CÓDIGO AQUÍ ↓


# ─────────────────────────────────────────
#  Ejercicio 2
# ─────────────────────────────────────────
# Crea un generador "fibonacci()" infinito
# que produzca la secuencia de Fibonacci.
# Imprime los primeros 10 números usando next().

# TU CÓDIGO AQUÍ ↓


# ─────────────────────────────────────────
#  Ejercicio 3
# ─────────────────────────────────────────
# Crea un generador "tomar(gen, n)" que tome
# solo los primeros n elementos de cualquier generador.
# Úsalo con el generador de Fibonacci para tomar los primeros 8.

# TU CÓDIGO AQUÍ ↓


# ─────────────────────────────────────────
#  Ejercicio 4
# ─────────────────────────────────────────
# Compara el uso de memoria entre:
#   - una lista con los cuadrados del 1 al 100,000
#   - un generador con los mismos valores
# Imprime el tamaño en bytes de cada uno.
# Pista: import sys → sys.getsizeof()

# TU CÓDIGO AQUÍ ↓


# ─────────────────────────────────────────
#  Ejercicio 5
# ─────────────────────────────────────────
# Crea un pipeline de tres generadores:
#   1. "numeros(n)"      → produce números del 1 al n
#   2. "multiplos_3(gen)"→ filtra solo los múltiplos de 3
#   3. "al_cubo(gen)"    → eleva cada uno al cubo
# Imprime los resultados para n=20.

# TU CÓDIGO AQUÍ ↓
