# ══════════════════════════════════════════════════════════════
#  Python Journey — by AngheloBR
#  Módulo 09: Avanzado
#  Tema 02: Decoradores
# ══════════════════════════════════════════════════════════════


# ─────────────────────────────────────────
#  ¿Qué es un decorador?
# ─────────────────────────────────────────
# Un decorador es una función que envuelve otra función
# para agregar comportamiento extra sin modificarla.
# Se usa con el símbolo @ antes de la función.
#
# Analogía:
#   Tienes una función "hacer_cafe()".
#   Un decorador es como agregarle una cápsula —
#   la función sigue siendo la misma, pero ahora
#   también registra el tiempo, verifica permisos, etc.


# ─────────────────────────────────────────
#  Funciones como objetos — base para entender decoradores
# ─────────────────────────────────────────
# En Python las funciones son objetos — se pueden pasar como argumentos.

def saludar():
    print("¡Hola!")

def ejecutar(funcion):
    print("Antes...")
    funcion()
    print("Después...")

ejecutar(saludar)
# Antes...
# ¡Hola!
# Después...


# ─────────────────────────────────────────
#  Crear un decorador
# ─────────────────────────────────────────
def mi_decorador(funcion):
    def wrapper():
        print("━━ Inicio ━━")
        funcion()
        print("━━ Fin ━━")
    return wrapper

def saludar():
    print("¡Hola!")

saludar_decorada = mi_decorador(saludar)
saludar_decorada()
# ━━ Inicio ━━
# ¡Hola!
# ━━ Fin ━━


# ─────────────────────────────────────────
#  Sintaxis con @ — la forma pythónica
# ─────────────────────────────────────────
def mi_decorador(funcion):
    def wrapper():
        print("━━ Inicio ━━")
        funcion()
        print("━━ Fin ━━")
    return wrapper

@mi_decorador
def saludar():
    print("¡Hola!")

saludar()   # equivale a: saludar = mi_decorador(saludar)


# ─────────────────────────────────────────
#  Decorador con argumentos — *args, **kwargs
# ─────────────────────────────────────────
# Para decorar funciones que reciben parámetros.

def mi_decorador(funcion):
    def wrapper(*args, **kwargs):
        print("Ejecutando...")
        resultado = funcion(*args, **kwargs)
        print("Listo.")
        return resultado
    return wrapper

@mi_decorador
def sumar(a, b):
    return a + b

print(sumar(3, 5))
# Ejecutando...
# Listo.
# 8


# ─────────────────────────────────────────
#  Decoradores útiles — ejemplos reales
# ─────────────────────────────────────────

# 1. Medir tiempo de ejecución
import time

def cronometro(funcion):
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = funcion(*args, **kwargs)
        fin = time.time()
        print(f"{funcion.__name__} tardó {fin - inicio:.4f}s")
        return resultado
    return wrapper

@cronometro
def operacion_lenta():
    total = sum(range(1_000_000))
    return total

operacion_lenta()


# 2. Verificar autenticación
def requiere_login(funcion):
    def wrapper(usuario, *args, **kwargs):
        if not usuario.get("autenticado"):
            print("Acceso denegado. Inicia sesión.")
            return
        return funcion(usuario, *args, **kwargs)
    return wrapper

@requiere_login
def ver_panel(usuario):
    print(f"Bienvenido al panel, {usuario['nombre']}.")

ver_panel({"nombre": "Ana", "autenticado": True})
ver_panel({"nombre": "Luis", "autenticado": False})


# ─────────────────────────────────────────
#  Apilar decoradores
# ─────────────────────────────────────────
def negrita(funcion):
    def wrapper():
        print(f"**{funcion()}**")
    return wrapper

def mayusculas(funcion):
    def wrapper():
        return funcion().upper()
    return wrapper

@negrita
@mayusculas
def mensaje():
    return "hola mundo"

mensaje()   # **HOLA MUNDO**


# ─────────────────────────────────────────
#  Resumen rápido
# ─────────────────────────────────────────
#   def decorador(func):        → define el decorador
#       def wrapper(*args, **kwargs): → envuelve la función
#           # código extra
#           return func(*args, **kwargs)
#       return wrapper
#
#   @decorador                  → aplica el decorador
#   def mi_funcion(): ...
#
#   Casos de uso: logging, autenticación, caché, cronómetro
