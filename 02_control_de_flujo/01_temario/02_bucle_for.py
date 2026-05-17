# ══════════════════════════════════════════════════════════════
#  Python Journey — by AngheloBR
#  Módulo 02: Control de flujo
#  Tema 02: Bucle for
# ══════════════════════════════════════════════════════════════


# ─────────────────────────────────────────
#  ¿Qué es un bucle for?
# ─────────────────────────────────────────
# Un bucle for repite un bloque de código para cada elemento
# de una secuencia (lista, string, rango, etc.)


# ─────────────────────────────────────────
#  Sintaxis básica
# ─────────────────────────────────────────
frutas = ["manzana", "pera", "uva"]

for fruta in frutas:
    print(fruta)

# manzana
# pera
# uva


# ─────────────────────────────────────────
#  range() — generar secuencias de números
# ─────────────────────────────────────────
# range(fin)          → 0 hasta fin-1
# range(inicio, fin)  → inicio hasta fin-1
# range(inicio, fin, paso) → con saltos

for i in range(5):
    print(i)        # 0 1 2 3 4

for i in range(1, 6):
    print(i)        # 1 2 3 4 5

for i in range(0, 11, 2):
    print(i)        # 0 2 4 6 8 10

# Contar hacia atrás
for i in range(5, 0, -1):
    print(i)        # 5 4 3 2 1


# ─────────────────────────────────────────
#  Iterar sobre un string
# ─────────────────────────────────────────
nombre = "Python"

for letra in nombre:
    print(letra)    # P y t h o n (uno por línea)


# ─────────────────────────────────────────
#  enumerate() — índice + valor
# ─────────────────────────────────────────
# Cuando necesitas saber la posición del elemento.

colores = ["rojo", "verde", "azul"]

for indice, color in enumerate(colores):
    print(f"{indice}: {color}")

# 0: rojo
# 1: verde
# 2: azul

# Puedes cambiar el inicio del índice
for indice, color in enumerate(colores, start=1):
    print(f"{indice}. {color}")

# 1. rojo
# 2. verde
# 3. azul


# ─────────────────────────────────────────
#  Bucles for anidados
# ─────────────────────────────────────────
# Un for dentro de otro for.

for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i * j}")
    print("---")


# ─────────────────────────────────────────
#  Ejemplo práctico — suma de una lista
# ─────────────────────────────────────────
numeros = [10, 25, 8, 42, 15]
total = 0

for numero in numeros:
    total += numero

print(f"Suma total: {total}")   # Suma total: 100


# ─────────────────────────────────────────
#  Resumen rápido
# ─────────────────────────────────────────
#   for item in secuencia:       → itera sobre cualquier secuencia
#   for i in range(n):           → repite n veces (0 a n-1)
#   for i in range(a, b):        → de a hasta b-1
#   for i in range(a, b, paso):  → con saltos
#   for i, v in enumerate(lista) → índice + valor
