# ══════════════════════════════════════════════════════════════
#  Python Journey — by AngheloBR
#  Módulo 09: Avanzado
#  Tema 01: Comprehensions
# ══════════════════════════════════════════════════════════════


# ─────────────────────────────────────────
#  ¿Qué son las comprehensions?
# ─────────────────────────────────────────
# Son una forma compacta y pythónica de crear
# listas, diccionarios y sets en una sola línea.
# Más legibles y eficientes que un bucle for equivalente.


# ─────────────────────────────────────────
#  List comprehension
# ─────────────────────────────────────────
# Sintaxis: [expresion for item in iterable if condicion]

# Sin comprehension
cuadrados = []
for x in range(1, 6):
    cuadrados.append(x ** 2)

# Con comprehension
cuadrados = [x ** 2 for x in range(1, 6)]
print(cuadrados)   # [1, 4, 9, 16, 25]

# Con condición
pares = [x for x in range(1, 21) if x % 2 == 0]
print(pares)       # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# Transformar strings
nombres = ["ana", "luis", "maría"]
mayus = [n.capitalize() for n in nombres]
print(mayus)       # ['Ana', 'Luis', 'María']

# Anidado — tabla de multiplicar
tabla = [f"{i}x{j}={i*j}" for i in range(1, 4) for j in range(1, 4)]
print(tabla)


# ─────────────────────────────────────────
#  Dict comprehension
# ─────────────────────────────────────────
# Sintaxis: {clave: valor for item in iterable if condicion}

cuadrados = {x: x ** 2 for x in range(1, 6)}
print(cuadrados)   # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Invertir clave y valor
original = {"a": 1, "b": 2, "c": 3}
invertido = {v: k for k, v in original.items()}
print(invertido)   # {1: 'a', 2: 'b', 3: 'c'}

# Filtrar diccionario
notas = {"Ana": 18, "Luis": 11, "María": 16, "Carlos": 9}
aprobados = {k: v for k, v in notas.items() if v >= 13}
print(aprobados)   # {'Ana': 18, 'María': 16}


# ─────────────────────────────────────────
#  Set comprehension
# ─────────────────────────────────────────
# Sintaxis: {expresion for item in iterable}

letras = {letra.lower() for letra in "Python Journey"}
print(letras)   # conjunto de letras únicas sin espacios


# ─────────────────────────────────────────
#  Generator expression
# ─────────────────────────────────────────
# Como list comprehension pero con () en vez de [].
# No crea la lista completa en memoria — genera un elemento a la vez.
# Ideal para grandes volúmenes de datos.

generador = (x ** 2 for x in range(1, 6))
print(generador)          # <generator object ...>
print(list(generador))    # [1, 4, 9, 16, 25]

# Muy útil con sum(), max(), min()
total = sum(x ** 2 for x in range(1, 101))
print(total)   # 338350


# ─────────────────────────────────────────
#  Cuándo usar comprehension vs for
# ─────────────────────────────────────────
# ✅ Comprehension → transformación o filtrado simple
# ❌ Comprehension → lógica compleja con varios if/else anidados
#                    (usa for para que sea legible)

# Legible
pares = [x for x in range(20) if x % 2 == 0]

# Demasiado complejo para comprehension → mejor for
# resultado = [f(x) if condicion1 else g(x) if condicion2 else h(x) for x in lista if otra_condicion]


# ─────────────────────────────────────────
#  Resumen rápido
# ─────────────────────────────────────────
#   [x for x in lista]              → list comprehension
#   [x for x in lista if cond]      → con filtro
#   {k: v for k, v in dic.items()}  → dict comprehension
#   {x for x in lista}              → set comprehension
#   (x for x in lista)              → generator expression
