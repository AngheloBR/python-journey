# ══════════════════════════════════════════════════════════════
#  Python Journey — by AngheloBR
#  Módulo 01: Fundamentos
#  Soluciones 03: Operadores
# ══════════════════════════════════════════════════════════════
#
#  ⚠️  Intenta resolver los ejercicios por tu cuenta primero.
#  Solo revisa esto si ya lo intentaste y no pudiste.
# ══════════════════════════════════════════════════════════════


# ─────────────────────────────────────────
#  Ejercicio 1
# ─────────────────────────────────────────
a = 15
b = 4

print(a + b)    # 19
print(a - b)    # 11
print(a * b)    # 60
print(a / b)    # 3.75
print(a // b)   # 3
print(a % b)    # 3
print(a ** b)   # 50625


# ─────────────────────────────────────────
#  Ejercicio 2
# ─────────────────────────────────────────
precio = 100

precio += 50    # 150
precio *= 2     # 300
precio -= 30    # 270
precio //= 4    # 67

print(precio)   # 67


# ─────────────────────────────────────────
#  Ejercicio 3
# ─────────────────────────────────────────
edad = 22
tiene_trabajo = False

print(edad >= 18 and tiene_trabajo)    # False
print(edad >= 18 or tiene_trabajo)     # True
print(not tiene_trabajo)               # True


# ─────────────────────────────────────────
#  Ejercicio 4
# ─────────────────────────────────────────
# Respuestas antes de ejecutar:
#   print(2 + 3 * 2)             → 8   (primero 3*2, luego +2)
#   print((2 + 3) * 2)           → 10  (primero paréntesis)
#   print(10 % 3 == 1)           → True (10%3 es 1, 1==1 es True)
#   print(5 ** 2 > 20 and 10 // 3 == 3) → True (25>20 es True, 3==3 es True)

print(2 + 3 * 2)                        # 8
print((2 + 3) * 2)                      # 10
print(10 % 3 == 1)                      # True
print(5 ** 2 > 20 and 10 // 3 == 3)    # True


# ─────────────────────────────────────────
#  Ejercicio 5
# ─────────────────────────────────────────
colores = ["rojo", "verde", "azul"]

print("verde" in colores)        # True
print("amarillo" not in colores) # True


# ─────────────────────────────────────────
#  Ejercicio 6
# ─────────────────────────────────────────
temperatura = 38

print(temperatura >= 36 and temperatura <= 37.5)   # False
