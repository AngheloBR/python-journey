# ══════════════════════════════════════════════════════════════
#  Python Journey — by AngheloBR
#  Módulo 09: Avanzado
#  Soluciones 03: Generadores
# ══════════════════════════════════════════════════════════════
#
#  ⚠️  Intenta resolver los ejercicios por tu cuenta primero.
#  Solo revisa esto si ya lo intentaste y no pudiste.
# ══════════════════════════════════════════════════════════════

import sys


# ─────────────────────────────────────────
#  Ejercicio 1
# ─────────────────────────────────────────
def pares(n):
    for i in range(0, n + 1, 2):
        yield i

for p in pares(20):
    print(p, end=" ")
# 0 2 4 6 8 10 12 14 16 18 20


# ─────────────────────────────────────────
#  Ejercicio 2
# ─────────────────────────────────────────
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

gen = fibonacci()
for _ in range(10):
    print(next(gen), end=" ")
# 0 1 1 2 3 5 8 13 21 34


# ─────────────────────────────────────────
#  Ejercicio 3
# ─────────────────────────────────────────
def tomar(gen, n):
    for _ in range(n):
        yield next(gen)

gen_fib = fibonacci()
primeros_8 = list(tomar(gen_fib, 8))
print(primeros_8)   # [0, 1, 1, 2, 3, 5, 8, 13]


# ─────────────────────────────────────────
#  Ejercicio 4
# ─────────────────────────────────────────
lista = [x ** 2 for x in range(1, 100_001)]
gen   = (x ** 2 for x in range(1, 100_001))

print(f"Lista    : {sys.getsizeof(lista):,} bytes")
print(f"Generador: {sys.getsizeof(gen)} bytes")
# La diferencia es enorme — el generador es casi constante (~200 bytes)


# ─────────────────────────────────────────
#  Ejercicio 5
# ─────────────────────────────────────────
def numeros(n):
    for i in range(1, n + 1):
        yield i

def multiplos_3(gen):
    for n in gen:
        if n % 3 == 0:
            yield n

def al_cubo(gen):
    for n in gen:
        yield n ** 3

pipeline = al_cubo(multiplos_3(numeros(20)))

for valor in pipeline:
    print(valor, end=" ")
# 27 216 729 1728 3375 5832  (3³ 6³ 9³ 12³ 15³ 18³)
