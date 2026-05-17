# ══════════════════════════════════════════════════════════════
#  Python Journey — by AngheloBR
#  Módulo 01: Fundamentos
#  Tema 02: Tipos de datos
# ══════════════════════════════════════════════════════════════


# ─────────────────────────────────────────
#  ¿Qué es un tipo de dato?
# ─────────────────────────────────────────
# Cada valor en Python tiene un tipo. El tipo define qué clase
# de información guarda y qué operaciones puedes hacer con ella.

# Los tipos básicos (primitivos) en Python son:
#   str   → texto
#   int   → número entero
#   float → número decimal
#   bool  → verdadero o falso


# ─────────────────────────────────────────
#  str — cadena de texto
# ─────────────────────────────────────────
# Se escribe entre comillas simples o dobles (ambas funcionan igual).

nombre = "Anghelo"
ciudad = 'Lima'
frase = "Hola, soy Python"

print(type(nombre))   # <class 'str'>

# Puedes usar las dos comillas si el texto tiene apóstrofe:
mensaje = "It's Python"
print(mensaje)

# Longitud de un string con len()
print(len(nombre))    # 7

# Concatenar strings con +
saludo = "Hola, " + nombre
print(saludo)         # Hola, Anghelo

# Repetir un string con *
linea = "-" * 20
print(linea)          # --------------------


# ─────────────────────────────────────────
#  int — número entero
# ─────────────────────────────────────────
# Sin decimales. Puede ser positivo, negativo o cero.

edad = 21
temperatura = -5
cero = 0

print(type(edad))     # <class 'int'>

# Operaciones básicas
print(10 + 3)         # 13
print(10 - 3)         # 7
print(10 * 3)         # 30
print(10 // 3)        # 3  → división entera (sin decimales)
print(10 % 3)         # 1  → módulo (resto de la división)
print(2 ** 8)         # 256 → potencia


# ─────────────────────────────────────────
#  float — número decimal
# ─────────────────────────────────────────
# Tiene punto decimal. Se usa para medidas, precios, porcentajes.

altura = 1.75
precio = 99.99
pi = 3.14159

print(type(altura))   # <class 'float'>

# División normal siempre devuelve float
print(10 / 3)         # 3.3333333333333335

# Mezclar int y float → resultado siempre es float
print(5 + 2.0)        # 7.0


# ─────────────────────────────────────────
#  bool — booleano
# ─────────────────────────────────────────
# Solo tiene dos valores posibles: True o False
# (con mayúscula inicial — es importante)

es_mayor = True
tiene_cuenta = False

print(type(es_mayor)) # <class 'bool'>

# Los booleanos son el resultado de comparaciones
print(10 > 5)         # True
print(10 < 5)         # False
print(10 == 10)       # True
print(10 != 5)        # True


# ─────────────────────────────────────────
#  Conversión de tipos (casting)
# ─────────────────────────────────────────
# Puedes convertir un tipo en otro con las funciones:
#   int(), float(), str(), bool()

numero_texto = "42"
numero_real = int(numero_texto)
print(type(numero_real))   # <class 'int'>
print(numero_real + 8)     # 50

precio_texto = "19.99"
precio_real = float(precio_texto)
print(precio_real + 0.01)  # 20.0

edad = 21
edad_texto = str(edad)
print("Tengo " + edad_texto + " años")   # Tengo 21 años

# ⚠️ No todo se puede convertir
# int("hola")  → esto lanza un error


# ─────────────────────────────────────────
#  Resumen rápido
# ─────────────────────────────────────────
#   "texto"   → str
#   42        → int
#   3.14      → float
#   True      → bool
#
#   type()    → para saber el tipo
#   int()     → convierte a entero
#   float()   → convierte a decimal
#   str()     → convierte a texto
#   bool()    → convierte a booleano
