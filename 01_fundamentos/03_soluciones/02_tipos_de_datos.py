# ══════════════════════════════════════════════════════════════
#  Python Journey — by AngheloBR
#  Módulo 01: Fundamentos
#  Soluciones 02: Tipos de datos
# ══════════════════════════════════════════════════════════════
#
#  ⚠️  Intenta resolver los ejercicios por tu cuenta primero.
#  Solo revisa esto si ya lo intentaste y no pudiste.
# ══════════════════════════════════════════════════════════════


# ─────────────────────────────────────────
#  Ejercicio 1
# ─────────────────────────────────────────
# Crea una variable de cada tipo:
#   - str, int, float, bool
# Imprime el valor y el tipo de cada una con type().

nombre = "Ana"
edad = 20
altura = 1.65
activo = True

print(nombre, type(nombre))     # Ana <class 'str'>
print(edad, type(edad))         # 20 <class 'int'>
print(altura, type(altura))     # 1.65 <class 'float'>
print(activo, type(activo))     # True <class 'bool'>


# ─────────────────────────────────────────
#  Ejercicio 2
# ─────────────────────────────────────────
# Tienes esta variable:
#   precio = "59.90"
# Conviértela a float y súmale 10.10.
# Imprime el resultado.

precio = "59.90"
precio_real = float(precio)
print(precio_real + 10.10)      # 70.0


# ─────────────────────────────────────────
#  Ejercicio 3
# ─────────────────────────────────────────
# Crea dos variables numéricas y realiza estas operaciones:
#   - suma, resta, multiplicación, división entera, módulo, potencia

a = 10
b = 3

print(a + b)    # 13
print(a - b)    # 7
print(a * b)    # 30
print(a // b)   # 3
print(a % b)    # 1
print(a ** b)   # 1000


# ─────────────────────────────────────────
#  Ejercicio 4
# ─────────────────────────────────────────
# Tienes esta variable:
#   edad = 17
# Usando una comparación, imprime si la persona es mayor de edad (>=18).

edad = 17
print(edad >= 18)   # False


# ─────────────────────────────────────────
#  Ejercicio 5
# ─────────────────────────────────────────
# Crea una variable con tu nombre.
# Imprime cuántos caracteres tiene usando len().
# Luego imprime tu nombre concatenado con " es programador/a".

nombre = "Ana"
print(len(nombre))                      # 3
print(nombre + " es programador/a")     # Ana es programador/a


# ─────────────────────────────────────────
#  Ejercicio 6
# ─────────────────────────────────────────
# Convierte los siguientes valores al tipo indicado e imprime el resultado.

print(int("100"))       # 100
print(float("3.14"))    # 3.14
print(bool(0))          # False
print(bool(1))          # True
