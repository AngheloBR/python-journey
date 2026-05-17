# ══════════════════════════════════════════════════════════════
#  Python Journey — by AngheloBR
#  Módulo 02: Control de flujo
#  Soluciones 03: Bucle while
# ══════════════════════════════════════════════════════════════
#
#  ⚠️  Intenta resolver los ejercicios por tu cuenta primero.
#  Solo revisa esto si ya lo intentaste y no pudiste.
# ══════════════════════════════════════════════════════════════


# ─────────────────────────────────────────
#  Ejercicio 1
# ─────────────────────────────────────────
i = 1

while i <= 10:
    print(i)
    i += 1


# ─────────────────────────────────────────
#  Ejercicio 2
# ─────────────────────────────────────────
contador = 0
numero = int(input("Ingresa un número positivo: "))

while numero > 0:
    contador += 1
    numero = int(input("Ingresa un número positivo: "))

print(f"Ingresaste {contador} números.")


# ─────────────────────────────────────────
#  Ejercicio 3
# ─────────────────────────────────────────
clave = ""

while clave != "python123":
    clave = input("Ingresa la contraseña: ")
    if clave != "python123":
        print("Contraseña incorrecta, intenta de nuevo.")

print("Acceso concedido.")


# ─────────────────────────────────────────
#  Ejercicio 4
# ─────────────────────────────────────────
cuenta = 10

while cuenta >= 1:
    print(cuenta)
    cuenta -= 1

print("¡Tiempo!")


# ─────────────────────────────────────────
#  Ejercicio 5
# ─────────────────────────────────────────
total = 0
numero = int(input("Ingresa un número (0 para terminar): "))

while numero != 0:
    total += numero
    numero = int(input("Ingresa un número (0 para terminar): "))

print(f"Suma total: {total}")


# ─────────────────────────────────────────
#  Ejercicio 6
# ─────────────────────────────────────────
secreto = 15
intentos = 5

while intentos > 0:
    intento = int(input(f"Adivina el número ({intentos} intentos): "))
    intentos -= 1

    if intento == secreto:
        print("¡Correcto!")
        break
    elif intento < secreto:
        print("Más alto.")
    else:
        print("Más bajo.")
else:
    print("Perdiste. Era el 15.")
