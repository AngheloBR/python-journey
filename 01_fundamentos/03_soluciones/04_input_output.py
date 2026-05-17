# ══════════════════════════════════════════════════════════════
#  Python Journey — by AngheloBR
#  Módulo 01: Fundamentos
#  Soluciones 04: Input / Output
# ══════════════════════════════════════════════════════════════
#
#  ⚠️  Intenta resolver los ejercicios por tu cuenta primero.
#  Solo revisa esto si ya lo intentaste y no pudiste.
# ══════════════════════════════════════════════════════════════


# ─────────────────────────────────────────
#  Ejercicio 1
# ─────────────────────────────────────────
producto = "Laptop"
precio = 2999.99
disponible = True

print(f"Producto  : {producto}")
print(f"Precio    : {precio}")
print(f"Disponible: {disponible}")


# ─────────────────────────────────────────
#  Ejercicio 2
# ─────────────────────────────────────────
print(1, 2, 3, 4, 5, sep="-")   # 1-2-3-4-5


# ─────────────────────────────────────────
#  Ejercicio 3
# ─────────────────────────────────────────
nombre = input("¿Cómo te llamas? ")
anio = int(input("¿En qué año naciste? "))
edad = 2025 - anio

print(f"Hola {nombre}, tienes aproximadamente {edad} años.")


# ─────────────────────────────────────────
#  Ejercicio 4
# ─────────────────────────────────────────
a = float(input("Ingresa el primer número: "))
b = float(input("Ingresa el segundo número: "))

print(f"Suma        : {a + b}")
print(f"Resta       : {a - b}")
print(f"Multiplicación: {a * b}")
print(f"División    : {a / b:.2f}")


# ─────────────────────────────────────────
#  Ejercicio 5
# ─────────────────────────────────────────
promedio = 16.6666666
print(f"Tu promedio es: {promedio:.2f}")   # Tu promedio es: 16.67


# ─────────────────────────────────────────
#  Ejercicio 6
# ─────────────────────────────────────────
nombre = input("¿Cómo te llamas? ")
ciudad = input("¿De qué ciudad eres? ")
hobby = input("¿Cuál es tu hobby favorito? ")

print()
print("══════════════════════════")
print(f"  Nombre : {nombre}")
print(f"  Ciudad : {ciudad}")
print(f"  Hobby  : {hobby}")
print("══════════════════════════")
