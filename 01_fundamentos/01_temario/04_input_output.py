# ══════════════════════════════════════════════════════════════
#  Python Journey — by AngheloBR
#  Módulo 01: Fundamentos
#  Tema 04: Input / Output
# ══════════════════════════════════════════════════════════════


# ─────────────────────────────────────────
#  ¿Qué es input y output?
# ─────────────────────────────────────────
# Output → mostrar información al usuario (print)
# Input  → recibir información del usuario (input)


# ─────────────────────────────────────────
#  print() — output
# ─────────────────────────────────────────
# Ya lo usamos, pero tiene más opciones.

print("Hola, mundo")

# Imprimir varios valores separados por coma
print("Nombre:", "Ana", "Edad:", 20)   # Nombre: Ana Edad: 20

# Cambiar el separador con sep=
print("Lima", "Perú", "América", sep=" | ")   # Lima | Perú | América

# Cambiar el final de línea con end=
print("Hola", end=" ")
print("mundo")    # Hola mundo  (en la misma línea)

# Por defecto end="\n" que significa salto de línea


# ─────────────────────────────────────────
#  f-strings — la forma moderna de formatear texto
# ─────────────────────────────────────────
# Permiten insertar variables directamente dentro de un string.
# Se escriben con f antes de las comillas y {} para las variables.

nombre = "Ana"
edad = 20
altura = 1.65

print(f"Me llamo {nombre} y tengo {edad} años.")
print(f"Mido {altura} metros.")

# Puedes hacer operaciones dentro de {}
print(f"El doble de mi edad es {edad * 2}.")
print(f"El año que viene tendré {edad + 1} años.")

# Formato de decimales
pi = 3.14159
print(f"Pi aproximado: {pi:.2f}")    # Pi aproximado: 3.14 (2 decimales)


# ─────────────────────────────────────────
#  input() — recibir datos del usuario
# ─────────────────────────────────────────
# Detiene el programa y espera que el usuario escriba algo.
# Siempre devuelve un string, sin importar lo que se escriba.

# Ejemplo básico:
# nombre = input("¿Cómo te llamas? ")
# print(f"Hola, {nombre}!")

# ⚠️ input() siempre devuelve str
# Si necesitas un número, debes convertirlo.

# edad = input("¿Cuántos años tienes? ")
# print(type(edad))   # <class 'str'>

# edad = int(input("¿Cuántos años tienes? "))
# print(type(edad))   # <class 'int'>


# ─────────────────────────────────────────
#  Ejemplo completo con input y output
# ─────────────────────────────────────────

# nombre = input("¿Cómo te llamas? ")
# edad = int(input("¿Cuántos años tienes? "))
# altura = float(input("¿Cuánto mides? (ej: 1.75) "))
#
# print()   # línea en blanco
# print("══════════════════")
# print(f"  Nombre : {nombre}")
# print(f"  Edad   : {edad} años")
# print(f"  Altura : {altura} m")
# print("══════════════════")

# Los input() están comentados para que el archivo
# no se detenga al ejecutarse. Descoméntalos para probarlo.


# ─────────────────────────────────────────
#  Resumen rápido
# ─────────────────────────────────────────
#   print()        → mostrar en pantalla
#   print(sep=" ") → cambiar separador
#   print(end=" ") → cambiar fin de línea
#   f"texto {var}" → formatear strings
#   input("msg")   → recibir texto del usuario
#   int(input())   → recibir número entero
#   float(input()) → recibir número decimal
