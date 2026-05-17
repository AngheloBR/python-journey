# ══════════════════════════════════════════════════════════════
#  Python Journey — by AngheloBR
#  Módulo 02: Control de flujo
#  Tema 01: Condicionales
# ══════════════════════════════════════════════════════════════


# ─────────────────────────────────────────
#  ¿Qué es un condicional?
# ─────────────────────────────────────────
# Un condicional permite ejecutar código solo si se cumple
# una condición. Es la base de toda lógica en programación.


# ─────────────────────────────────────────
#  if — si
# ─────────────────────────────────────────
# Si la condición es True, ejecuta el bloque indentado.

edad = 20

if edad >= 18:
    print("Eres mayor de edad.")

# Si edad fuera 15, no imprimiría nada.


# ─────────────────────────────────────────
#  if / else — si / sino
# ─────────────────────────────────────────
# else se ejecuta cuando la condición del if es False.

edad = 15

if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")


# ─────────────────────────────────────────
#  if / elif / else — si / sino si / sino
# ─────────────────────────────────────────
# elif permite evaluar más condiciones.
# Solo se ejecuta el primer bloque cuya condición sea True.

nota = 75

if nota >= 90:
    print("Excelente")
elif nota >= 70:
    print("Aprobado")
elif nota >= 50:
    print("Regular")
else:
    print("Reprobado")

# Resultado: Aprobado


# ─────────────────────────────────────────
#  Condiciones con operadores lógicos
# ─────────────────────────────────────────
edad = 22
tiene_dni = True

if edad >= 18 and tiene_dni:
    print("Puede votar.")

temperatura = 38.5

if temperatura < 36 or temperatura > 37.5:
    print("Temperatura fuera de rango normal.")

usuario = "admin"

if not usuario == "bloqueado":
    print("Acceso permitido.")


# ─────────────────────────────────────────
#  Condicionales anidados
# ─────────────────────────────────────────
# Puedes poner un if dentro de otro if.
# Úsalo con moderación — demasiados niveles dificultan la lectura.

edad = 20
es_miembro = True

if edad >= 18:
    if es_miembro:
        print("Acceso VIP.")
    else:
        print("Acceso estándar.")
else:
    print("Acceso denegado — menor de edad.")


# ─────────────────────────────────────────
#  Condicional en una línea (ternario)
# ─────────────────────────────────────────
# Para casos simples, Python permite escribir el if en una sola línea.
# Sintaxis: valor_si_true if condicion else valor_si_false

edad = 20
estado = "mayor" if edad >= 18 else "menor"
print(estado)   # mayor

# Es útil para asignaciones rápidas, no abuses de él en lógica compleja.


# ─────────────────────────────────────────
#  Ejemplo práctico
# ─────────────────────────────────────────
# hora = int(input("¿Qué hora es? (0-23) "))
#
# if hora < 12:
#     saludo = "Buenos días"
# elif hora < 18:
#     saludo = "Buenas tardes"
# else:
#     saludo = "Buenas noches"
#
# print(f"{saludo}!")


# ─────────────────────────────────────────
#  Resumen rápido
# ─────────────────────────────────────────
#   if condicion:          → si se cumple
#   elif otra_condicion:   → sino, si se cumple esto
#   else:                  → sino (ninguna anterior se cumplió)
#
#   and  → ambas condiciones deben ser True
#   or   → al menos una debe ser True
#   not  → invierte la condición
#
#   x if condicion else y  → ternario (una línea)
