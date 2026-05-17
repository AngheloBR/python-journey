# ══════════════════════════════════════════════════════════════
#  Python Journey — by AngheloBR
#  Módulo 03: Funciones
#  Soluciones 01: Definición y uso de funciones
# ══════════════════════════════════════════════════════════════
#
#  ⚠️  Intenta resolver los ejercicios por tu cuenta primero.
#  Solo revisa esto si ya lo intentaste y no pudiste.
# ══════════════════════════════════════════════════════════════


# ─────────────────────────────────────────
#  Ejercicio 1
# ─────────────────────────────────────────
def presentarse(nombre, edad):
    print(f"Me llamo {nombre} y tengo {edad} años.")

presentarse("Ana", 20)


# ─────────────────────────────────────────
#  Ejercicio 2
# ─────────────────────────────────────────
def calcular_area_rectangulo(base, altura):
    return base * altura

area = calcular_area_rectangulo(5, 3)
print(f"Área: {area}")   # Área: 15


# ─────────────────────────────────────────
#  Ejercicio 3
# ─────────────────────────────────────────
def es_par(numero):
    return numero % 2 == 0

print(es_par(4))    # True
print(es_par(7))    # False


# ─────────────────────────────────────────
#  Ejercicio 4
# ─────────────────────────────────────────
def saludar(nombre, saludo="Hola"):
    print(f"{saludo}, {nombre}!")

saludar("Ana")                  # Hola, Ana!
saludar("Luis", "Buenos días")  # Buenos días, Luis!


# ─────────────────────────────────────────
#  Ejercicio 5
# ─────────────────────────────────────────
def promedio(*numeros):
    return sum(numeros) / len(numeros)

print(promedio(10, 20, 30))        # 20.0
print(promedio(5, 7, 9, 11, 13))   # 9.0


# ─────────────────────────────────────────
#  Ejercicio 6
# ─────────────────────────────────────────
cuadrado = lambda x: x ** 2
es_mayor_de_edad = lambda edad: edad >= 18
saludar = lambda nombre: f"Hola, {nombre}!"

print(cuadrado(5))              # 25
print(es_mayor_de_edad(20))     # True
print(es_mayor_de_edad(15))     # False
print(saludar("Ana"))           # Hola, Ana!
