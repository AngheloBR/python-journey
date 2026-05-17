# ══════════════════════════════════════════════════════════════
#  Python Journey — by AngheloBR
#  Módulo 02: Control de flujo
#  Tema 03: Bucle while
# ══════════════════════════════════════════════════════════════


# ─────────────────────────────────────────
#  ¿Qué es un bucle while?
# ─────────────────────────────────────────
# Un bucle while repite un bloque de código MIENTRAS
# una condición sea True. A diferencia del for, no necesita
# una secuencia — solo una condición.


# ─────────────────────────────────────────
#  Sintaxis básica
# ─────────────────────────────────────────
contador = 0

while contador < 5:
    print(contador)
    contador += 1

# 0 1 2 3 4

# ⚠️ Si no actualizas el contador, el bucle es infinito.
# Siempre asegúrate de que la condición pueda volverse False.


# ─────────────────────────────────────────
#  while vs for
# ─────────────────────────────────────────
# Usa for cuando sabes cuántas veces repetir.
# Usa while cuando no sabes cuántas veces — dependes de una condición.

# Ejemplo: pedir un número hasta que sea positivo
# numero = int(input("Ingresa un número positivo: "))
#
# while numero <= 0:
#     print("Debe ser positivo, intenta de nuevo.")
#     numero = int(input("Ingresa un número positivo: "))
#
# print(f"Gracias, ingresaste: {numero}")


# ─────────────────────────────────────────
#  Bucle infinito controlado con break
# ─────────────────────────────────────────
# while True crea un bucle que nunca termina por sí solo.
# Se usa cuando no sabes cuándo el usuario va a querer salir.

# while True:
#     comando = input("Escribe algo (o 'salir' para terminar): ")
#     if comando == "salir":
#         break
#     print(f"Escribiste: {comando}")
#
# print("Hasta luego.")


# ─────────────────────────────────────────
#  while con contador — ejemplo clásico
# ─────────────────────────────────────────
# Cuenta regresiva
cuenta = 5

while cuenta > 0:
    print(f"{cuenta}...")
    cuenta -= 1

print("¡Despegue!")


# ─────────────────────────────────────────
#  while / else
# ─────────────────────────────────────────
# El bloque else se ejecuta cuando la condición del while
# se vuelve False (no cuando se interrumpe con break).

intentos = 3

while intentos > 0:
    print(f"Intentos restantes: {intentos}")
    intentos -= 1
else:
    print("Se agotaron los intentos.")


# ─────────────────────────────────────────
#  Ejemplo práctico — adivina el número
# ─────────────────────────────────────────
# secreto = 7
# intento = 0
#
# while intento != secreto:
#     intento = int(input("Adivina el número (1-10): "))
#     if intento < secreto:
#         print("Más alto.")
#     elif intento > secreto:
#         print("Más bajo.")
#
# print("¡Correcto!")


# ─────────────────────────────────────────
#  Resumen rápido
# ─────────────────────────────────────────
#   while condicion:    → repite mientras condicion sea True
#   while True:         → bucle infinito (necesita break para salir)
#   while ... else:     → else se ejecuta al terminar normalmente
#
#   for  → cuando sabes cuántas veces
#   while → cuando dependes de una condición
