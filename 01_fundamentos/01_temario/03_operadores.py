# ══════════════════════════════════════════════════════════════
#  Python Journey — by AngheloBR
#  Módulo 01: Fundamentos
#  Tema 03: Operadores
# ══════════════════════════════════════════════════════════════


# ─────────────────────────────────────────
#  ¿Qué es un operador?
# ─────────────────────────────────────────
# Un operador es un símbolo que realiza una operación
# entre uno o más valores. Python tiene varios tipos.


# ─────────────────────────────────────────
#  1. Operadores aritméticos
# ─────────────────────────────────────────
# Para hacer cálculos matemáticos.

print(10 + 3)    # 13  → suma
print(10 - 3)    # 7   → resta
print(10 * 3)    # 30  → multiplicación
print(10 / 3)    # 3.3333... → división (siempre float)
print(10 // 3)   # 3   → división entera (sin decimales)
print(10 % 3)    # 1   → módulo (resto)
print(2 ** 8)    # 256 → potencia


# ─────────────────────────────────────────
#  2. Operadores de comparación
# ─────────────────────────────────────────
# Comparan dos valores y devuelven True o False.

print(10 == 10)   # True  → igual a
print(10 != 5)    # True  → distinto de
print(10 > 5)     # True  → mayor que
print(10 < 5)     # False → menor que
print(10 >= 10)   # True  → mayor o igual que
print(10 <= 9)    # False → menor o igual que


# ─────────────────────────────────────────
#  3. Operadores lógicos
# ─────────────────────────────────────────
# Combinan condiciones booleanas.

# and → True si AMBAS condiciones son True
print(True and True)    # True
print(True and False)   # False

# or → True si AL MENOS UNA condición es True
print(True or False)    # True
print(False or False)   # False

# not → invierte el valor
print(not True)         # False
print(not False)        # True

# Ejemplo práctico
edad = 20
tiene_dni = True

puede_votar = edad >= 18 and tiene_dni
print(puede_votar)      # True


# ─────────────────────────────────────────
#  4. Operadores de asignación
# ─────────────────────────────────────────
# Asignan o modifican el valor de una variable.

x = 10
print(x)    # 10

x += 5      # x = x + 5
print(x)    # 15

x -= 3      # x = x - 3
print(x)    # 12

x *= 2      # x = x * 2
print(x)    # 24

x //= 4     # x = x // 4
print(x)    # 6

x **= 2     # x = x ** 2
print(x)    # 36

x %= 10     # x = x % 10
print(x)    # 6


# ─────────────────────────────────────────
#  5. Operadores de identidad
# ─────────────────────────────────────────
# Comprueban si dos variables apuntan al mismo objeto en memoria.

a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)     # True  → b apunta al mismo objeto que a
print(a is c)     # False → c es una lista distinta aunque tiene los mismos valores
print(a is not c) # True


# ─────────────────────────────────────────
#  6. Operadores de pertenencia
# ─────────────────────────────────────────
# Comprueban si un valor existe dentro de una secuencia.

frutas = ["manzana", "pera", "uva"]

print("pera" in frutas)       # True
print("sandía" in frutas)     # False
print("sandía" not in frutas) # True

# También funciona con strings
nombre = "Anghelo"
print("ghe" in nombre)        # True


# ─────────────────────────────────────────
#  Precedencia de operadores
# ─────────────────────────────────────────
# Python sigue el orden matemático: paréntesis primero,
# luego potencia, luego * / //, luego + -.

print(2 + 3 * 4)      # 14  → primero 3*4, luego +2
print((2 + 3) * 4)    # 20  → primero (2+3), luego *4

# Cuando tengas dudas, usa paréntesis. Es más legible.
