# ══════════════════════════════════════════════════════════════
#  Python Journey — by AngheloBR
#  Módulo 03: Funciones
#  Soluciones 03: Funciones integradas (built-in)
# ══════════════════════════════════════════════════════════════
#
#  ⚠️  Intenta resolver los ejercicios por tu cuenta primero.
#  Solo revisa esto si ya lo intentaste y no pudiste.
# ══════════════════════════════════════════════════════════════


# ─────────────────────────────────────────
#  Ejercicio 1
# ─────────────────────────────────────────
numeros = [4, -2, 9, -7, 3, 0, -1, 8]

print(f"Mayor  : {max(numeros)}")             # 9
print(f"Menor  : {min(numeros)}")             # -7
print(f"Suma   : {sum(numeros)}")             # 14
print(f"Promedio: {sum(numeros)/len(numeros):.2f}")  # 1.75


# ─────────────────────────────────────────
#  Ejercicio 2
# ─────────────────────────────────────────
precios = [19.99, 5.5, 34.1, 8.75, 12.0]

print(sorted(precios))                  # [5.5, 8.75, 12.0, 19.99, 34.1]
print(sorted(precios, reverse=True))    # [34.1, 19.99, 12.0, 8.75, 5.5]


# ─────────────────────────────────────────
#  Ejercicio 3
# ─────────────────────────────────────────
productos = ["laptop", "mouse", "teclado"]
precios   = [2500, 45, 120]

for producto, precio in zip(productos, precios):
    print(f"{producto:<10} → S/. {precio}")


# ─────────────────────────────────────────
#  Ejercicio 4
# ─────────────────────────────────────────
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

cuadrados = list(map(lambda x: x ** 2, numeros))
print(cuadrados)   # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


# ─────────────────────────────────────────
#  Ejercicio 5
# ─────────────────────────────────────────
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

mayores = list(filter(lambda x: x > 5, numeros))
print(mayores)   # [6, 7, 8, 9, 10]


# ─────────────────────────────────────────
#  Ejercicio 6
# ─────────────────────────────────────────
temperaturas = [-5, 0, 15, -3, 22, -10, 8]

absolutas = list(map(abs, temperaturas))
print(absolutas)            # [5, 0, 15, 3, 22, 10, 8]
print(f"Máxima: {max(absolutas)}")  # 22
print(f"Mínima: {min(absolutas)}")  # 0
