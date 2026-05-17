# ══════════════════════════════════════════════════════════════
#  Python Journey — by AngheloBR
#  Módulo 09: Avanzado
#  Tema 03: Generadores
# ══════════════════════════════════════════════════════════════


# ─────────────────────────────────────────
#  ¿Qué es un generador?
# ─────────────────────────────────────────
# Un generador es una función que produce valores uno a la vez
# usando yield en vez de return.
# No guarda todos los valores en memoria — los genera bajo demanda.
#
# Analogía:
#   Una lista = preparas 1000 sándwiches y los guardas todos.
#   Un generador = preparas un sándwich cada vez que alguien lo pide.


# ─────────────────────────────────────────
#  yield — la clave de los generadores
# ─────────────────────────────────────────
def contar_hasta(n):
    for i in range(1, n + 1):
        yield i   # pausa y entrega el valor

gen = contar_hasta(5)
print(gen)           # <generator object contar_hasta at ...>
print(next(gen))     # 1
print(next(gen))     # 2
print(next(gen))     # 3

# Iterar con for — la forma más común
for numero in contar_hasta(5):
    print(numero, end=" ")
# 1 2 3 4 5


# ─────────────────────────────────────────
#  Generador vs Lista — diferencia de memoria
# ─────────────────────────────────────────
import sys

lista = [x ** 2 for x in range(1000)]
gen   = (x ** 2 for x in range(1000))

print(f"Lista    : {sys.getsizeof(lista)} bytes")
print(f"Generador: {sys.getsizeof(gen)} bytes")
# La lista ocupa mucho más — el generador es casi constante


# ─────────────────────────────────────────
#  Generadores infinitos
# ─────────────────────────────────────────
# Un generador puede ser infinito — produce valores sin fin.
# Solo tomas los que necesitas.

def numeros_infinitos(inicio=0):
    n = inicio
    while True:
        yield n
        n += 1

gen = numeros_infinitos()
for _ in range(5):
    print(next(gen), end=" ")
# 0 1 2 3 4


# ─────────────────────────────────────────
#  Ejemplo práctico — leer archivo grande
# ─────────────────────────────────────────
# Sin generador — carga todo en memoria
# def leer_todo(ruta):
#     with open(ruta) as f:
#         return f.readlines()   # ← todo en RAM

# Con generador — una línea a la vez
def leer_lineas(ruta):
    with open(ruta, encoding="utf-8") as f:
        for linea in f:
            yield linea.strip()

# for linea in leer_lineas("archivo_enorme.txt"):
#     print(linea)


# ─────────────────────────────────────────
#  Encadenar generadores — pipeline
# ─────────────────────────────────────────
def numeros(n):
    for i in range(1, n + 1):
        yield i

def solo_pares(gen):
    for n in gen:
        if n % 2 == 0:
            yield n

def al_cuadrado(gen):
    for n in gen:
        yield n ** 2

# Pipeline: números → filtrar pares → elevar al cuadrado
pipeline = al_cuadrado(solo_pares(numeros(10)))

for valor in pipeline:
    print(valor, end=" ")
# 4 16 36 64 100


# ─────────────────────────────────────────
#  send() — enviar valores al generador
# ─────────────────────────────────────────
def acumulador():
    total = 0
    while True:
        valor = yield total
        if valor is None:
            break
        total += valor

gen = acumulador()
next(gen)          # inicializar
print(gen.send(10))   # 10
print(gen.send(20))   # 30
print(gen.send(5))    # 35


# ─────────────────────────────────────────
#  Resumen rápido
# ─────────────────────────────────────────
#   yield valor          → pausa y entrega el valor
#   next(gen)            → obtener el siguiente valor
#   for x in gen:        → iterar sobre el generador
#   (x for x in ...)     → generator expression
#   Ventaja principal    → eficiencia de memoria
#   Uso ideal            → grandes volúmenes de datos, streams, pipelines
