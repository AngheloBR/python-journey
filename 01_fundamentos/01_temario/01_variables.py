# ══════════════════════════════════════════════════════════════
#  Python Journey — by AngheloBR
#  Módulo 01: Fundamentos
#  Tema 01: Variables
# ══════════════════════════════════════════════════════════════


# ─────────────────────────────────────────
#  ¿Qué es una variable?
# ─────────────────────────────────────────
# Una variable es un espacio en memoria donde guardamos un valor.
# Piénsalo como una caja con un nombre — adentro puedes poner lo que quieras.

nombre = "Anghelo"
edad = 21
altura = 1.75
es_estudiante = True

# La sintaxis siempre es:
#   nombre_variable = valor


# ─────────────────────────────────────────
#  Reglas para nombrar variables
# ─────────────────────────────────────────
# ✅ Puede contener letras, números y guión bajo (_)
# ✅ Debe empezar con letra o guión bajo
# ✅ Se recomienda usar snake_case (palabras separadas por _)
# ❌ No puede empezar con número
# ❌ No puede tener espacios
# ❌ No puede ser una palabra reservada de Python (if, for, while, etc.)

mi_nombre = "Ana"        # ✅ correcto
nombre2 = "Luis"         # ✅ correcto
_temporal = 99           # ✅ correcto
# 2nombre = "error"      # ❌ incorrecto — empieza con número
# mi nombre = "error"    # ❌ incorrecto — tiene espacio


# ─────────────────────────────────────────
#  Imprimir variables con print()
# ─────────────────────────────────────────
print(nombre)            # Anghelo
print(edad)              # 21
print(altura)            # 1.75
print(es_estudiante)     # True


# ─────────────────────────────────────────
#  Cambiar el valor de una variable
# ─────────────────────────────────────────
# Las variables pueden cambiar de valor en cualquier momento.

puntaje = 0
print(puntaje)   # 0

puntaje = 100
print(puntaje)   # 100

puntaje = puntaje + 50
print(puntaje)   # 150


# ─────────────────────────────────────────
#  Asignación múltiple
# ─────────────────────────────────────────
# Puedes asignar varios valores en una sola línea.

x, y, z = 10, 20, 30
print(x, y, z)   # 10 20 30

# O el mismo valor a varias variables.

a = b = c = 0
print(a, b, c)   # 0 0 0


# ─────────────────────────────────────────
#  type() — conocer el tipo de una variable
# ─────────────────────────────────────────
# Python es dinámico: no declaras el tipo, él lo detecta solo.

print(type(nombre))        # <class 'str'>
print(type(edad))          # <class 'int'>
print(type(altura))        # <class 'float'>
print(type(es_estudiante)) # <class 'bool'>


# ─────────────────────────────────────────
#  Buenas prácticas
# ─────────────────────────────────────────
# - Usa nombres descriptivos: edad es mejor que e
# - Snake case: nombre_completo, no nombreCompleto
# - No uses nombres genéricos como data, info, temp (a menos que sea temporal de verdad)

# ✅ Claro
nombre_usuario = "Carlos"
precio_total = 99.99

# ❌ Confuso
x2 = "Carlos"
pt = 99.99
