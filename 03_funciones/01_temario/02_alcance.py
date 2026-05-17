# ══════════════════════════════════════════════════════════════
#  Python Journey — by AngheloBR
#  Módulo 03: Funciones
#  Tema 02: Alcance (scope)
# ══════════════════════════════════════════════════════════════


# ─────────────────────────────────────────
#  ¿Qué es el alcance?
# ─────────────────────────────────────────
# El alcance (scope) define desde dónde puedes acceder
# a una variable. En Python hay dos tipos principales:
#   Local  → existe solo dentro de una función
#   Global → existe en todo el archivo


# ─────────────────────────────────────────
#  Variable local
# ─────────────────────────────────────────
# Se crea dentro de una función y solo existe ahí.

def mi_funcion():
    mensaje = "Soy local"
    print(mensaje)

mi_funcion()    # Soy local
# print(mensaje)  # ❌ Error — mensaje no existe fuera de la función


# ─────────────────────────────────────────
#  Variable global
# ─────────────────────────────────────────
# Se crea fuera de cualquier función y es accesible desde cualquier lugar.

nombre = "Ana"   # variable global

def saludar():
    print(f"Hola, {nombre}!")   # puede leerla

saludar()       # Hola, Ana!
print(nombre)   # Ana


# ─────────────────────────────────────────
#  Modificar una variable global dentro de una función
# ─────────────────────────────────────────
# Por defecto, no puedes modificar una variable global desde una función.
# Necesitas declarar global dentro de la función.

contador = 0

def incrementar():
    global contador
    contador += 1

incrementar()
incrementar()
incrementar()
print(contador)   # 3

# ⚠️ Usa global con moderación — hace el código difícil de seguir.
# Es mejor pasar variables como parámetros y usar return.


# ─────────────────────────────────────────
#  Local vs Global — mismo nombre
# ─────────────────────────────────────────
# Si una variable local tiene el mismo nombre que una global,
# dentro de la función se usa la local.

x = 10   # global

def mostrar():
    x = 99   # local — no afecta a la global
    print(x)

mostrar()   # 99
print(x)    # 10 — la global no cambió


# ─────────────────────────────────────────
#  Buena práctica — parámetros en vez de global
# ─────────────────────────────────────────
# En vez de esto:
total = 0

def agregar(n):
    global total
    total += n

# Mejor esto:
def agregar(total, n):
    return total + n

total = 0
total = agregar(total, 5)
total = agregar(total, 10)
print(total)   # 15


# ─────────────────────────────────────────
#  Resumen rápido
# ─────────────────────────────────────────
#   Local  → variable creada dentro de una función
#   Global → variable creada fuera de toda función
#   global → palabra clave para modificar una global desde una función
#
#   Regla de oro: prefiere parámetros y return sobre variables globales
