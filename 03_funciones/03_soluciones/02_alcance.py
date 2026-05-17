# ══════════════════════════════════════════════════════════════
#  Python Journey — by AngheloBR
#  Módulo 03: Funciones
#  Soluciones 02: Alcance (scope)
# ══════════════════════════════════════════════════════════════
#
#  ⚠️  Intenta resolver los ejercicios por tu cuenta primero.
#  Solo revisa esto si ya lo intentaste y no pudiste.
# ══════════════════════════════════════════════════════════════


# ─────────────────────────────────────────
#  Ejercicio 1
# ─────────────────────────────────────────
# Imprime:
#   10  → la x local dentro de la función
#   5   → la x global no fue modificada

x = 5

def funcion():
    x = 10
    print(x)   # 10

funcion()
print(x)       # 5


# ─────────────────────────────────────────
#  Ejercicio 2
# ─────────────────────────────────────────
idioma = "español"

def mostrar_idioma():
    print(f"Idioma: {idioma}")

mostrar_idioma()   # Idioma: español
print(idioma)      # español


# ─────────────────────────────────────────
#  Ejercicio 3
# ─────────────────────────────────────────
vidas = 3

def perder_vida():
    global vidas
    vidas -= 1

perder_vida()
perder_vida()
print(vidas)   # 1


# ─────────────────────────────────────────
#  Ejercicio 4
# ─────────────────────────────────────────
def perder_vida(vidas):
    return vidas - 1

vidas = 3
vidas = perder_vida(vidas)
vidas = perder_vida(vidas)
print(vidas)   # 1

# Mucho más limpio — sin global, sin efectos secundarios.


# ─────────────────────────────────────────
#  Ejercicio 5
# ─────────────────────────────────────────
# Error: NameError — 'mensaje' no está definido cuando se llama mostrar().
# Python ejecuta mostrar() antes de que mensaje exista.
# Las variables globales deben definirse ANTES de usarse.

# Corrección:
mensaje = "Hola"

def mostrar():
    print(mensaje)

mostrar()   # Hola
