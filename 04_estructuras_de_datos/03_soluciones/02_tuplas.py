# ══════════════════════════════════════════════════════════════
#  Python Journey — by AngheloBR
#  Módulo 04: Estructuras de datos
#  Soluciones 02: Tuplas
# ══════════════════════════════════════════════════════════════
#
#  ⚠️  Intenta resolver los ejercicios por tu cuenta primero.
#  Solo revisa esto si ya lo intentaste y no pudiste.
# ══════════════════════════════════════════════════════════════


# ─────────────────────────────────────────
#  Ejercicio 1
# ─────────────────────────────────────────
persona = ("Ana", 20, "Lima", "Programadora")

print(persona[0])   # Ana
print(persona[1])   # 20
print(persona[2])   # Lima
print(persona[3])   # Programadora


# ─────────────────────────────────────────
#  Ejercicio 2
# ─────────────────────────────────────────
punto = (15, 30, 45)
x, y, z = punto

print(f"x = {x}, y = {y}, z = {z}")


# ─────────────────────────────────────────
#  Ejercicio 3
# ─────────────────────────────────────────
numeros = (4, 7, 2, 7, 9, 1, 7, 3)

print(numeros.count(7))    # 3
print(numeros.index(9))    # 4


# ─────────────────────────────────────────
#  Ejercicio 4
# ─────────────────────────────────────────
colores = ["rojo", "verde", "azul"]
colores_tupla = tuple(colores)

print(colores_tupla)        # ('rojo', 'verde', 'azul')
print(type(colores_tupla))  # <class 'tuple'>

# colores_tupla[0] = "amarillo"
# → TypeError: 'tuple' object does not support item assignment
# Las tuplas son inmutables — no se pueden modificar una vez creadas.


# ─────────────────────────────────────────
#  Ejercicio 5
# ─────────────────────────────────────────
datos = ("Ana", 20, "Lima", "Python", "Kotlin")
nombre, edad, *resto = datos

print(f"Nombre: {nombre}")   # Ana
print(f"Edad  : {edad}")     # 20
print(f"Resto : {resto}")    # ['Lima', 'Python', 'Kotlin']


# ─────────────────────────────────────────
#  Ejercicio 6
# ─────────────────────────────────────────
estudiantes = [("Ana", 18), ("Luis", 14), ("María", 20), ("Carlos", 11)]

for nombre, nota in estudiantes:
    print(f"{nombre}: {nota}")

print("\nAprobados:")
for nombre, nota in estudiantes:
    if nota >= 13:
        print(f"  {nombre}: {nota}")
