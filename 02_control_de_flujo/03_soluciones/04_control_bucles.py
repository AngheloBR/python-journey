# ══════════════════════════════════════════════════════════════
#  Python Journey — by AngheloBR
#  Módulo 02: Control de flujo
#  Soluciones 04: Control de bucles (break, continue, pass)
# ══════════════════════════════════════════════════════════════
#
#  ⚠️  Intenta resolver los ejercicios por tu cuenta primero.
#  Solo revisa esto si ya lo intentaste y no pudiste.
# ══════════════════════════════════════════════════════════════


# ─────────────────────────────────────────
#  Ejercicio 1
# ─────────────────────────────────────────
for i in range(1, 21):
    if i % 7 == 0:
        print(f"Primer múltiplo de 7: {i}")
        break


# ─────────────────────────────────────────
#  Ejercicio 2
# ─────────────────────────────────────────
for i in range(1, 16):
    if i % 3 == 0:
        continue
    print(i)


# ─────────────────────────────────────────
#  Ejercicio 3
# ─────────────────────────────────────────
while True:
    print("\n1. Saludar")
    print("2. Salir")
    opcion = input("Elige una opción: ")

    if opcion == "1":
        print("¡Hola!")
    elif opcion == "2":
        print("Saliendo...")
        break
    else:
        print("Opción no válida.")


# ─────────────────────────────────────────
#  Ejercicio 4
# ─────────────────────────────────────────
palabras = ["sol", "luna", "error", "mar", "error", "rio"]

for palabra in palabras:
    if palabra == "error":
        continue
    print(palabra)


# ─────────────────────────────────────────
#  Ejercicio 5
# ─────────────────────────────────────────
contador = 0

while True:
    palabra = input("Ingresa una palabra (o 'fin' para terminar): ")
    if palabra == "fin":
        break
    contador += 1

print(f"Ingresaste {contador} palabras.")


# ─────────────────────────────────────────
#  Ejercicio 6
# ─────────────────────────────────────────
encontrados = 0

for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0:
        print(i)
        encontrados += 1
        if encontrados == 3:
            break
