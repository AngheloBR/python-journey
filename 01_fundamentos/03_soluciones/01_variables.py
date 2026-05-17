# ══════════════════════════════════════════════════════════════
#  Python Journey — by AngheloBR
#  Módulo 01: Fundamentos
#  Soluciones 01: Variables
# ══════════════════════════════════════════════════════════════
#
#  ⚠️  Intenta resolver los ejercicios por tu cuenta primero.
#  Solo revisa esto si ya lo intentaste y no pudiste.
# ══════════════════════════════════════════════════════════════


# ─────────────────────────────────────────
#  Ejercicio 1
# ─────────────────────────────────────────
# Crea tres variables:
#   - tu nombre (texto)
#   - tu edad (número entero)
#   - si te gusta programar (True o False)
# Luego imprime cada una.

nombre = "Ana"
edad = 20
le_gusta_programar = True

print(nombre)
print(edad)
print(le_gusta_programar)


# ─────────────────────────────────────────
#  Ejercicio 2
# ─────────────────────────────────────────
# Crea una variable llamada "puntaje" con valor 0.
# Imprimela.
# Luego cambia su valor a 50 e imprímela de nuevo.
# Luego súmale 25 más e imprímela una última vez.

puntaje = 0
print(puntaje)   # 0

puntaje = 50
print(puntaje)   # 50

puntaje = puntaje + 25
print(puntaje)   # 75


# ─────────────────────────────────────────
#  Ejercicio 3
# ─────────────────────────────────────────
# En una sola línea, crea tres variables:
#   ciudad = "Lima", pais = "Perú", continente = "América"
# Luego imprime las tres juntas con un solo print().

ciudad, pais, continente = "Lima", "Perú", "América"
print(ciudad, pais, continente)


# ─────────────────────────────────────────
#  Ejercicio 4
# ─────────────────────────────────────────
# Crea una variable con tu nombre.
# Usa type() para imprimir qué tipo de dato es.
# Haz lo mismo con tu edad.

nombre = "Ana"
edad = 20

print(type(nombre))   # <class 'str'>
print(type(edad))     # <class 'int'>


# ─────────────────────────────────────────
#  Ejercicio 5
# ─────────────────────────────────────────
# Los siguientes nombres de variables tienen errores.
# Corrígelos y asígnales cualquier valor.

# ❌ 1nombre = "error"       → empieza con número
nombre_1 = "corregido"

# ❌ mi ciudad = "error"     → tiene espacio
mi_ciudad = "corregido"

# ❌ for = "error"           → palabra reservada de Python
mi_for = "corregido"

print(nombre_1, mi_ciudad, mi_for)
