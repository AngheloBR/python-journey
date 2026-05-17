# ══════════════════════════════════════════════════════════════
#  Python Journey — by AngheloBR
#  Módulo 04: Estructuras de datos
#  Tema 01: Listas
# ══════════════════════════════════════════════════════════════


# ─────────────────────────────────────────
#  ¿Qué es una lista?
# ─────────────────────────────────────────
# Una lista es una colección ordenada y mutable de elementos.
# Puede contener cualquier tipo de dato, incluso mezclados.

frutas = ["manzana", "pera", "uva"]
numeros = [1, 2, 3, 4, 5]
mixta = [1, "hola", True, 3.14]
vacia = []

print(type(frutas))   # <class 'list'>


# ─────────────────────────────────────────
#  Acceder a elementos — índices
# ─────────────────────────────────────────
# Los índices empiezan en 0. Los negativos cuentan desde el final.

frutas = ["manzana", "pera", "uva", "mango"]

print(frutas[0])    # manzana
print(frutas[1])    # pera
print(frutas[-1])   # mango  (último)
print(frutas[-2])   # uva    (penúltimo)


# ─────────────────────────────────────────
#  Slicing — obtener sublistas
# ─────────────────────────────────────────
# lista[inicio:fin]      → desde inicio hasta fin-1
# lista[inicio:fin:paso] → con saltos

numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(numeros[2:5])    # [2, 3, 4]
print(numeros[:4])     # [0, 1, 2, 3]
print(numeros[6:])     # [6, 7, 8, 9]
print(numeros[::2])    # [0, 2, 4, 6, 8]
print(numeros[::-1])   # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0] → invertida


# ─────────────────────────────────────────
#  Modificar elementos
# ─────────────────────────────────────────
frutas = ["manzana", "pera", "uva"]
frutas[1] = "kiwi"
print(frutas)   # ['manzana', 'kiwi', 'uva']


# ─────────────────────────────────────────
#  Métodos principales
# ─────────────────────────────────────────
frutas = ["manzana", "pera", "uva"]

# Agregar
frutas.append("mango")        # agrega al final
frutas.insert(1, "kiwi")      # inserta en posición 1
print(frutas)   # ['manzana', 'kiwi', 'pera', 'uva', 'mango']

# Eliminar
frutas.remove("pera")         # elimina por valor
frutas.pop()                  # elimina el último
frutas.pop(0)                 # elimina por índice
print(frutas)   # ['kiwi', 'uva']

# Información
numeros = [3, 1, 4, 1, 5, 9, 2, 6]
print(len(numeros))           # 8
print(numeros.count(1))       # 2  → cuántas veces aparece
print(numeros.index(5))       # 4  → índice de la primera aparición

# Ordenar
numeros.sort()                # ordena en el lugar
print(numeros)   # [1, 1, 2, 3, 4, 5, 6, 9]

numeros.sort(reverse=True)
print(numeros)   # [9, 6, 5, 4, 3, 2, 1, 1]

numeros.reverse()             # invierte en el lugar
print(numeros)   # [1, 1, 2, 3, 4, 5, 6, 9]

# Copiar y limpiar
copia = numeros.copy()
numeros.clear()               # vacía la lista
print(numeros)   # []
print(copia)     # [1, 1, 2, 3, 4, 5, 6, 9]


# ─────────────────────────────────────────
#  Iterar sobre una lista
# ─────────────────────────────────────────
colores = ["rojo", "verde", "azul"]

for color in colores:
    print(color)

for i, color in enumerate(colores):
    print(f"{i}: {color}")


# ─────────────────────────────────────────
#  List comprehension
# ─────────────────────────────────────────
# Forma compacta de crear listas.
# [expresion for item in iterable if condicion]

cuadrados = [x ** 2 for x in range(1, 6)]
print(cuadrados)   # [1, 4, 9, 16, 25]

pares = [x for x in range(1, 11) if x % 2 == 0]
print(pares)       # [2, 4, 6, 8, 10]

mayusculas = [nombre.upper() for nombre in ["ana", "luis", "maría"]]
print(mayusculas)  # ['ANA', 'LUIS', 'MARÍA']


# ─────────────────────────────────────────
#  Resumen rápido
# ─────────────────────────────────────────
#   lista[i]          → acceder por índice
#   lista[a:b]        → slicing
#   lista.append(x)   → agregar al final
#   lista.insert(i,x) → insertar en posición
#   lista.remove(x)   → eliminar por valor
#   lista.pop(i)      → eliminar por índice
#   lista.sort()      → ordenar
#   lista.reverse()   → invertir
#   lista.copy()      → copiar
#   lista.clear()     → vaciar
#   len(lista)        → longitud
#   [x for x in ...]  → list comprehension
