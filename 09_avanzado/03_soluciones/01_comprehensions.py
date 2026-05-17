# ══════════════════════════════════════════════════════════════
#  Python Journey — by AngheloBR
#  Módulo 09: Avanzado
#  Soluciones 01: Comprehensions
# ══════════════════════════════════════════════════════════════
#
#  ⚠️  Intenta resolver los ejercicios por tu cuenta primero.
#  Solo revisa esto si ya lo intentaste y no pudiste.
# ══════════════════════════════════════════════════════════════


# ─────────────────────────────────────────
#  Ejercicio 1
# ─────────────────────────────────────────
multiplos_3 = [x * 3 for x in range(1, 11)]
print(multiplos_3)   # [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]

cuadrados_impares = [x ** 2 for x in range(1, 21) if x % 2 != 0]
print(cuadrados_impares)   # [1, 9, 25, 49, 81, 121, 169, 225, 289, 361]


# ─────────────────────────────────────────
#  Ejercicio 2
# ─────────────────────────────────────────
palabras = ["python", "java", "go", "rust", "kotlin", "c"]

mayusculas = [p.upper() for p in palabras]
print(mayusculas)

largas = [p for p in palabras if len(p) > 3]
print(largas)   # ['python', 'java', 'rust', 'kotlin']

longitudes = [len(p) for p in palabras]
print(longitudes)   # [6, 4, 2, 4, 6, 1]


# ─────────────────────────────────────────
#  Ejercicio 3
# ─────────────────────────────────────────
precios = {"laptop": 2500, "mouse": 45, "teclado": 120, "monitor": 800}

con_descuento = {k: round(v * 0.9, 2) for k, v in precios.items()}
print(con_descuento)

caros = {k: v for k, v in precios.items() if v > 100}
print(caros)   # {'laptop': 2500, 'teclado': 120, 'monitor': 800}


# ─────────────────────────────────────────
#  Ejercicio 4
# ─────────────────────────────────────────
letras = ["a", "b", "a", "c", "b", "d", "a"]

unicas_mayus = {l.upper() for l in letras}
print(unicas_mayus)   # {'A', 'B', 'C', 'D'}


# ─────────────────────────────────────────
#  Ejercicio 5
# ─────────────────────────────────────────
total = sum(x for x in range(1, 1001))
print(f"Suma 1-1000: {total}")   # 500500

maximo = max(x ** 2 for x in range(1, 51))
print(f"Máximo cuadrado 1-50: {maximo}")   # 2500


# ─────────────────────────────────────────
#  Ejercicio 6
# ─────────────────────────────────────────
celsius = [0, 10, 20, 30, 40, 100]

fahrenheit = [(c * 9/5) + 32 for c in celsius]
print(fahrenheit)   # [32.0, 50.0, 68.0, 86.0, 104.0, 212.0]
