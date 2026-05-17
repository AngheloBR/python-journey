# ══════════════════════════════════════════════════════════════
#  Python Journey — by AngheloBR
#  Módulo 03: Funciones
#  Tema 01: Definición y uso de funciones
# ══════════════════════════════════════════════════════════════


# ─────────────────────────────────────────
#  ¿Qué es una función?
# ─────────────────────────────────────────
# Una función es un bloque de código reutilizable con un nombre.
# En vez de repetir el mismo código, lo encapsulas en una función
# y la llamas cuando la necesitas.


# ─────────────────────────────────────────
#  Definir y llamar una función
# ─────────────────────────────────────────
# Se define con def, un nombre y paréntesis.

def saludar():
    print("¡Hola, mundo!")

saludar()   # ¡Hola, mundo!
saludar()   # puedes llamarla las veces que quieras


# ─────────────────────────────────────────
#  Parámetros — datos de entrada
# ─────────────────────────────────────────
# Los parámetros son variables que recibe la función.

def saludar_a(nombre):
    print(f"¡Hola, {nombre}!")

saludar_a("Ana")    # ¡Hola, Ana!
saludar_a("Luis")   # ¡Hola, Luis!

# Múltiples parámetros
def sumar(a, b):
    print(a + b)

sumar(3, 5)    # 8
sumar(10, 20)  # 30


# ─────────────────────────────────────────
#  return — devolver un valor
# ─────────────────────────────────────────
# return devuelve un valor para usarlo fuera de la función.

def sumar(a, b):
    return a + b

resultado = sumar(3, 5)
print(resultado)          # 8
print(sumar(10, 20) * 2)  # 60

# Sin return, la función devuelve None
def sin_return():
    x = 5

print(sin_return())   # None


# ─────────────────────────────────────────
#  Parámetros por defecto
# ─────────────────────────────────────────
# Puedes definir un valor por defecto para un parámetro.
# Si no se pasa ese argumento, usa el valor por defecto.

def saludar(nombre, mensaje="¡Hola"):
    print(f"{mensaje}, {nombre}!")

saludar("Ana")                  # ¡Hola, Ana!
saludar("Luis", "Buenos días")  # Buenos días, Luis!


# ─────────────────────────────────────────
#  *args — múltiples argumentos
# ─────────────────────────────────────────
# Cuando no sabes cuántos argumentos recibirás.
# Los agrupa en una tupla.

def sumar_todo(*numeros):
    total = 0
    for n in numeros:
        total += n
    return total

print(sumar_todo(1, 2, 3))        # 6
print(sumar_todo(5, 10, 15, 20))  # 50


# ─────────────────────────────────────────
#  **kwargs — argumentos con nombre
# ─────────────────────────────────────────
# Recibe argumentos con nombre como un diccionario.

def mostrar_info(**datos):
    for clave, valor in datos.items():
        print(f"{clave}: {valor}")

mostrar_info(nombre="Ana", edad=20, ciudad="Lima")
# nombre: Ana
# edad: 20
# ciudad: Lima


# ─────────────────────────────────────────
#  Funciones lambda
# ─────────────────────────────────────────
# Funciones anónimas de una sola línea.
# Útiles para operaciones simples y rápidas.

doblar = lambda x: x * 2
print(doblar(5))    # 10

sumar = lambda a, b: a + b
print(sumar(3, 4))  # 7

# Son equivalentes a:
def doblar(x):
    return x * 2


# ─────────────────────────────────────────
#  Resumen rápido
# ─────────────────────────────────────────
#   def nombre():              → define una función
#   def nombre(a, b):          → con parámetros
#   return valor               → devuelve un valor
#   def nombre(a, b=10):       → parámetro con valor por defecto
#   def nombre(*args):         → múltiples argumentos (tupla)
#   def nombre(**kwargs):      → argumentos con nombre (diccionario)
#   lambda x: expresion        → función anónima de una línea
