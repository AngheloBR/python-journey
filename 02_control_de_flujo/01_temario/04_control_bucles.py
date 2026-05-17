# ══════════════════════════════════════════════════════════════
#  Python Journey — by AngheloBR
#  Módulo 02: Control de flujo
#  Tema 04: Control de bucles (break, continue, pass)
# ══════════════════════════════════════════════════════════════


# ─────────────────────────────────────────
#  ¿Para qué sirven?
# ─────────────────────────────────────────
# A veces necesitas controlar el flujo dentro de un bucle:
#   break    → salir del bucle por completo
#   continue → saltar la iteración actual y seguir con la siguiente
#   pass     → no hacer nada (placeholder)


# ─────────────────────────────────────────
#  break — salir del bucle
# ─────────────────────────────────────────
# Detiene el bucle inmediatamente sin importar la condición.

for i in range(10):
    if i == 5:
        break
    print(i)

# 0 1 2 3 4
# Al llegar a 5, sale del bucle.

# Con while
contador = 0

while True:
    print(contador)
    contador += 1
    if contador == 4:
        break

# 0 1 2 3


# ─────────────────────────────────────────
#  continue — saltar iteración
# ─────────────────────────────────────────
# Salta el resto del código en la iteración actual
# y pasa a la siguiente.

for i in range(10):
    if i % 2 == 0:
        continue
    print(i)

# 1 3 5 7 9
# Los pares se saltan, los impares se imprimen.


# ─────────────────────────────────────────
#  pass — no hacer nada
# ─────────────────────────────────────────
# Es un placeholder. Se usa cuando la sintaxis requiere
# un bloque pero aún no quieres escribir código.

for i in range(5):
    if i == 3:
        pass    # aquí irá algo luego
    print(i)

# Imprime todos — pass no hace nada, solo evita el error de sintaxis.

# También se usa en funciones o clases vacías:
# def mi_funcion():
#     pass


# ─────────────────────────────────────────
#  break vs continue
# ─────────────────────────────────────────
# break    → termina el bucle
# continue → salta esta vuelta, sigue con la siguiente

print("--- break ---")
for i in range(5):
    if i == 3:
        break
    print(i)
# 0 1 2

print("--- continue ---")
for i in range(5):
    if i == 3:
        continue
    print(i)
# 0 1 2 4


# ─────────────────────────────────────────
#  Ejemplo práctico — menú con break
# ─────────────────────────────────────────
# while True:
#     print("\n1. Saludar")
#     print("2. Despedirse")
#     print("3. Salir")
#     opcion = input("Elige una opción: ")
#
#     if opcion == "1":
#         print("¡Hola!")
#     elif opcion == "2":
#         print("¡Hasta luego!")
#     elif opcion == "3":
#         print("Saliendo...")
#         break
#     else:
#         print("Opción no válida.")


# ─────────────────────────────────────────
#  Resumen rápido
# ─────────────────────────────────────────
#   break    → sale del bucle inmediatamente
#   continue → salta la iteración actual
#   pass     → no hace nada, es un placeholder
