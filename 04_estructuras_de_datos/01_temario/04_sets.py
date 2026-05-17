# ══════════════════════════════════════════════════════════════
#  Python Journey — by AngheloBR
#  Módulo 04: Estructuras de datos
#  Tema 04: Sets (conjuntos)
# ══════════════════════════════════════════════════════════════


# ─────────────────────────────────────────
#  ¿Qué es un set?
# ─────────────────────────────────────────
# Un set es una colección NO ordenada de elementos ÚNICOS.
# No permite duplicados y no tiene índices.
# Es útil para eliminar duplicados y operaciones matemáticas de conjuntos.

frutas = {"manzana", "pera", "uva", "manzana"}
print(frutas)        # {'pera', 'uva', 'manzana'} — sin duplicados
print(type(frutas))  # <class 'set'>

vacio = set()   # ⚠️ {} crea un diccionario vacío, no un set


# ─────────────────────────────────────────
#  Agregar y eliminar
# ─────────────────────────────────────────
numeros = {1, 2, 3}

numeros.add(4)         # agrega un elemento
numeros.add(2)         # no hace nada — ya existe
print(numeros)         # {1, 2, 3, 4}

numeros.remove(3)      # elimina — lanza KeyError si no existe
numeros.discard(99)    # elimina — NO lanza error si no existe
print(numeros)         # {1, 2, 4}

numeros.clear()        # vacía el set
print(numeros)         # set()


# ─────────────────────────────────────────
#  Sin índices
# ─────────────────────────────────────────
# Los sets no tienen orden, no puedes acceder por índice.

colores = {"rojo", "verde", "azul"}
# print(colores[0])   # ❌ TypeError — los sets no tienen índices

# Solo puedes iterar
for color in colores:
    print(color)

# O verificar pertenencia
print("rojo" in colores)    # True
print("negro" in colores)   # False


# ─────────────────────────────────────────
#  Operaciones de conjuntos
# ─────────────────────────────────────────
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}

# Unión — todos los elementos de ambos
print(a | b)           # {1, 2, 3, 4, 5, 6, 7, 8}
print(a.union(b))      # igual

# Intersección — elementos comunes
print(a & b)                # {4, 5}
print(a.intersection(b))    # igual

# Diferencia — en a pero no en b
print(a - b)                # {1, 2, 3}
print(a.difference(b))      # igual

# Diferencia simétrica — en uno u otro pero no en ambos
print(a ^ b)                          # {1, 2, 3, 6, 7, 8}
print(a.symmetric_difference(b))      # igual


# ─────────────────────────────────────────
#  Uso práctico — eliminar duplicados
# ─────────────────────────────────────────
lista_con_duplicados = [1, 2, 2, 3, 4, 4, 4, 5]
sin_duplicados = list(set(lista_con_duplicados))
print(sin_duplicados)   # [1, 2, 3, 4, 5]


# ─────────────────────────────────────────
#  Comparar conjuntos
# ─────────────────────────────────────────
a = {1, 2, 3}
b = {1, 2, 3, 4, 5}

print(a.issubset(b))     # True  → a está dentro de b
print(b.issuperset(a))   # True  → b contiene a
print(a.isdisjoint({6, 7, 8}))  # True → no tienen elementos en común


# ─────────────────────────────────────────
#  Resumen rápido
# ─────────────────────────────────────────
#   {a, b, c}          → crear set
#   set()              → set vacío
#   set.add(x)         → agregar elemento
#   set.remove(x)      → eliminar (KeyError si no existe)
#   set.discard(x)     → eliminar (sin error si no existe)
#   a | b              → unión
#   a & b              → intersección
#   a - b              → diferencia
#   a ^ b              → diferencia simétrica
#   x in set           → verificar pertenencia
#   list(set(lista))   → eliminar duplicados de una lista
