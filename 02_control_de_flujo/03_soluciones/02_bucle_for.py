# ══════════════════════════════════════════════════════════════
#  Python Journey — by AngheloBR
#  Módulo 02: Control de flujo
#  Soluciones 02: Bucle for
# ══════════════════════════════════════════════════════════════
#
#  ⚠️  Intenta resolver los ejercicios por tu cuenta primero.
#  Solo revisa esto si ya lo intentaste y no pudiste.
# ══════════════════════════════════════════════════════════════


# ─────────────────────────────────────────
#  Ejercicio 1
# ─────────────────────────────────────────
for i in range(1, 11):
    print(i)


# ─────────────────────────────────────────
#  Ejercicio 2
# ─────────────────────────────────────────
# Opción 1 — con paso
for i in range(2, 21, 2):
    print(i)

# Opción 2 — con %
for i in range(1, 21):
    if i % 2 == 0:
        print(i)


# ─────────────────────────────────────────
#  Ejercicio 3
# ─────────────────────────────────────────
nombres = ["Ana", "Luis", "María", "Carlos"]

for indice, nombre in enumerate(nombres, start=1):
    print(f"{indice}. {nombre}")


# ─────────────────────────────────────────
#  Ejercicio 4
# ─────────────────────────────────────────
numero = int(input("Ingresa un número: "))

for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")


# ─────────────────────────────────────────
#  Ejercicio 5
# ─────────────────────────────────────────
precios = [15.5, 8.0, 22.3, 5.9, 11.0]
total = 0

for precio in precios:
    total += precio

print(f"Total: {total:.2f}")   # Total: 62.70


# ─────────────────────────────────────────
#  Ejercicio 6
# ─────────────────────────────────────────
for i in range(1, 6):
    print("* " * i)
