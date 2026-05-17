# ══════════════════════════════════════════════════════════════
#  Python Journey — by AngheloBR
#  Módulo 04: Estructuras de datos
#  Tema 02: Tuplas
# ══════════════════════════════════════════════════════════════


# ─────────────────────────────────────────
#  ¿Qué es una tupla?
# ─────────────────────────────────────────
# Una tupla es una colección ordenada e INMUTABLE de elementos.
# Una vez creada, no puedes modificarla.
# Se usa cuando los datos no deben cambiar.

coordenadas = (10, 20)
colores_rgb = (255, 128, 0)
vacia = ()
un_elemento = (42,)   # ⚠️ la coma es obligatoria para tuplas de un elemento

print(type(coordenadas))   # <class 'tuple'>


# ─────────────────────────────────────────
#  Acceder a elementos
# ─────────────────────────────────────────
# Igual que las listas — índices y slicing.

punto = (3, 7, 15, 22)

print(punto[0])     # 3
print(punto[-1])    # 22
print(punto[1:3])   # (7, 15)


# ─────────────────────────────────────────
#  Inmutabilidad
# ─────────────────────────────────────────
# No puedes modificar, agregar ni eliminar elementos.

colores = ("rojo", "verde", "azul")
# colores[0] = "amarillo"   # ❌ TypeError — las tuplas no se modifican


# ─────────────────────────────────────────
#  Métodos disponibles
# ─────────────────────────────────────────
# Al ser inmutables, solo tienen dos métodos:

numeros = (1, 2, 3, 2, 4, 2, 5)

print(numeros.count(2))    # 3  → cuántas veces aparece
print(numeros.index(4))    # 4  → índice de la primera aparición


# ─────────────────────────────────────────
#  Desempaquetado (unpacking)
# ─────────────────────────────────────────
# Puedes asignar los valores de una tupla a variables.

punto = (10, 20)
x, y = punto
print(x)   # 10
print(y)   # 20

persona = ("Ana", 20, "Lima")
nombre, edad, ciudad = persona
print(nombre, edad, ciudad)

# Con * para capturar el resto
primero, *resto = (1, 2, 3, 4, 5)
print(primero)   # 1
print(resto)     # [2, 3, 4, 5]


# ─────────────────────────────────────────
#  Tuplas vs Listas
# ─────────────────────────────────────────
# Lista  → mutable,   más lenta, más métodos
# Tupla  → inmutable, más rápida, menos métodos
#
# Usa tuplas cuando:
#   - Los datos no deben cambiar (coordenadas, colores, configs)
#   - Quieres proteger datos de modificaciones accidentales
#   - Necesitas usarla como clave de un diccionario (las listas no pueden)


# ─────────────────────────────────────────
#  Convertir entre lista y tupla
# ─────────────────────────────────────────
lista = [1, 2, 3]
tupla = tuple(lista)
print(tupla)         # (1, 2, 3)

tupla2 = (4, 5, 6)
lista2 = list(tupla2)
print(lista2)        # [4, 5, 6]


# ─────────────────────────────────────────
#  Iterar sobre una tupla
# ─────────────────────────────────────────
colores = ("rojo", "verde", "azul")

for color in colores:
    print(color)

for i, color in enumerate(colores):
    print(f"{i}: {color}")


# ─────────────────────────────────────────
#  Resumen rápido
# ─────────────────────────────────────────
#   (a, b, c)       → crear tupla
#   (x,)            → tupla de un elemento (coma obligatoria)
#   tupla[i]        → acceder por índice
#   tupla[a:b]      → slicing
#   a, b = tupla    → desempaquetado
#   tupla.count(x)  → contar apariciones
#   tupla.index(x)  → índice de primera aparición
#   tuple(lista)    → convertir lista a tupla
#   list(tupla)     → convertir tupla a lista
