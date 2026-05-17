# ══════════════════════════════════════════════════════════════
#  Python Journey — by AngheloBR
#  Módulo 02: Control de flujo
#  Soluciones 01: Condicionales
# ══════════════════════════════════════════════════════════════
#
#  ⚠️  Intenta resolver los ejercicios por tu cuenta primero.
#  Solo revisa esto si ya lo intentaste y no pudiste.
# ══════════════════════════════════════════════════════════════


# ─────────────────────────────────────────
#  Ejercicio 1
# ─────────────────────────────────────────
numero = int(input("Ingresa un número: "))

if numero > 0:
    print("Positivo")
elif numero < 0:
    print("Negativo")
else:
    print("Cero")


# ─────────────────────────────────────────
#  Ejercicio 2
# ─────────────────────────────────────────
nota = int(input("Ingresa tu nota (0-100): "))

if nota >= 90:
    print("Excelente")
elif nota >= 70:
    print("Aprobado")
elif nota >= 50:
    print("Regular")
else:
    print("Reprobado")


# ─────────────────────────────────────────
#  Ejercicio 3
# ─────────────────────────────────────────
edad = int(input("¿Cuántos años tienes? "))
licencia = input("¿Tienes licencia? (s/n) ")

if edad >= 18 and licencia == "s":
    print("Puedes manejar.")
else:
    print("No puedes manejar.")


# ─────────────────────────────────────────
#  Ejercicio 4
# ─────────────────────────────────────────
numero = int(input("Ingresa un número: "))
resultado = "par" if numero % 2 == 0 else "impar"
print(f"El número {numero} es {resultado}.")


# ─────────────────────────────────────────
#  Ejercicio 5
# ─────────────────────────────────────────
hora = int(input("¿Qué hora es? (0-23) "))

if hora < 12:
    print("Buenos días")
elif hora < 18:
    print("Buenas tardes")
else:
    print("Buenas noches")


# ─────────────────────────────────────────
#  Ejercicio 6
# ─────────────────────────────────────────
nota1 = float(input("Ingresa la primera nota: "))
nota2 = float(input("Ingresa la segunda nota: "))
nota3 = float(input("Ingresa la tercera nota: "))

promedio = (nota1 + nota2 + nota3) / 3

if promedio >= 70:
    print(f"Aprobó el curso. Promedio: {promedio:.2f}")
else:
    faltaron = 70 - promedio
    print(f"Reprobó el curso. Promedio: {promedio:.2f}. Le faltaron {faltaron:.2f} puntos.")
