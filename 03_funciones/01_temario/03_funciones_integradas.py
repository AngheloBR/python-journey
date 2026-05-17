# ══════════════════════════════════════════════════════════════
#  Python Journey — by AngheloBR
#  Módulo 03: Funciones
#  Tema 03: Funciones integradas (built-in)
# ══════════════════════════════════════════════════════════════


# ─────────────────────────────────────────
#  ¿Qué son las funciones integradas?
# ─────────────────────────────────────────
# Python trae funciones listas para usar sin importar nada.
# Ya usaste algunas: print(), input(), type(), len(), int(), float()
# Aquí veremos las más útiles.


# ─────────────────────────────────────────
#  Funciones numéricas
# ─────────────────────────────────────────
print(abs(-10))        # 10  → valor absoluto
print(round(3.7))      # 4   → redondea al entero más cercano
print(round(3.14159, 2))  # 3.14 → redondea a 2 decimales
print(max(3, 7, 1, 9, 4))  # 9  → el mayor
print(min(3, 7, 1, 9, 4))  # 1  → el menor
print(sum([10, 20, 30]))   # 60 → suma de una lista
print(pow(2, 8))        # 256 → potencia (igual que 2**8)


# ─────────────────────────────────────────
#  Funciones de secuencias
# ─────────────────────────────────────────
numeros = [3, 1, 4, 1, 5, 9, 2, 6]

print(len(numeros))          # 8   → longitud
print(sorted(numeros))       # [1, 1, 2, 3, 4, 5, 6, 9] → ordenado
print(sorted(numeros, reverse=True))  # [9, 6, 5, 4, 3, 2, 1, 1]
print(list(reversed(numeros)))        # [6, 2, 9, 5, 1, 4, 1, 3]
print(list(enumerate(["a", "b", "c"])))  # [(0,'a'),(1,'b'),(2,'c')]


# ─────────────────────────────────────────
#  zip() — combinar secuencias
# ─────────────────────────────────────────
nombres = ["Ana", "Luis", "María"]
edades  = [20, 25, 22]

for nombre, edad in zip(nombres, edades):
    print(f"{nombre} tiene {edad} años.")

# Ana tiene 20 años.
# Luis tiene 25 años.
# María tiene 22 años.


# ─────────────────────────────────────────
#  map() — aplicar función a cada elemento
# ─────────────────────────────────────────
numeros = [1, 2, 3, 4, 5]

dobles = list(map(lambda x: x * 2, numeros))
print(dobles)   # [2, 4, 6, 8, 10]

# Equivalente con for:
dobles = [n * 2 for n in numeros]
print(dobles)   # [2, 4, 6, 8, 10]


# ─────────────────────────────────────────
#  filter() — filtrar elementos
# ─────────────────────────────────────────
numeros = [1, 2, 3, 4, 5, 6, 7, 8]

pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)    # [2, 4, 6, 8]

# Equivalente con for:
pares = [n for n in numeros if n % 2 == 0]
print(pares)    # [2, 4, 6, 8]


# ─────────────────────────────────────────
#  Conversión de tipos
# ─────────────────────────────────────────
print(int("42"))        # 42
print(float("3.14"))    # 3.14
print(str(100))         # "100"
print(bool(0))          # False
print(bool(1))          # True
print(list("Python"))   # ['P', 'y', 't', 'h', 'o', 'n']
print(tuple([1, 2, 3])) # (1, 2, 3)


# ─────────────────────────────────────────
#  Otras útiles
# ─────────────────────────────────────────
print(range(5))              # range(0, 5)
print(list(range(5)))        # [0, 1, 2, 3, 4]
print(type("hola"))          # <class 'str'>
print(isinstance(42, int))   # True
print(isinstance("hi", int)) # False
print(id(42))                # dirección en memoria


# ─────────────────────────────────────────
#  Resumen rápido
# ─────────────────────────────────────────
#   abs()        → valor absoluto
#   round()      → redondear
#   max/min()    → mayor/menor
#   sum()        → suma
#   len()        → longitud
#   sorted()     → ordenar (devuelve nueva lista)
#   reversed()   → invertir
#   enumerate()  → índice + valor
#   zip()        → combinar secuencias
#   map()        → aplicar función a cada elemento
#   filter()     → filtrar elementos
#   isinstance() → verificar tipo
