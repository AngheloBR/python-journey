# ══════════════════════════════════════════════════════════════
#  Python Journey — by AngheloBR
#  Módulo 06: Archivos
#  Tema 02: CSV
# ══════════════════════════════════════════════════════════════


# ─────────────────────────────────────────
#  ¿Qué es un CSV?
# ─────────────────────────────────────────
# CSV = Comma Separated Values (valores separados por comas).
# Es un formato simple para guardar datos tabulares.
# Se puede abrir con Excel, Google Sheets, etc.
#
# Ejemplo de archivo CSV:
#   nombre,edad,ciudad
#   Ana,20,Lima
#   Luis,25,Cusco


import csv


# ─────────────────────────────────────────
#  Escribir un CSV
# ─────────────────────────────────────────
estudiantes = [
    ["nombre", "edad", "nota"],
    ["Ana", 20, 18],
    ["Luis", 22, 14],
    ["María", 21, 16],
    ["Carlos", 23, 11]
]

with open("estudiantes.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(estudiantes)

# newline="" es importante en Windows para evitar líneas en blanco


# ─────────────────────────────────────────
#  Leer un CSV
# ─────────────────────────────────────────
with open("estudiantes.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    for fila in reader:
        print(fila)

# ['nombre', 'edad', 'nota']
# ['Ana', '20', '18']
# ...

# ⚠️ csv.reader devuelve todo como strings
# Si necesitas números, convierte con int() o float()


# ─────────────────────────────────────────
#  DictWriter — escribir con encabezados
# ─────────────────────────────────────────
# Más legible — usa diccionarios en vez de listas

productos = [
    {"nombre": "Laptop",  "precio": 2500, "stock": 5},
    {"nombre": "Mouse",   "precio": 45,   "stock": 20},
    {"nombre": "Teclado", "precio": 120,  "stock": 12}
]

with open("productos.csv", "w", newline="", encoding="utf-8") as f:
    campos = ["nombre", "precio", "stock"]
    writer = csv.DictWriter(f, fieldnames=campos)
    writer.writeheader()     # escribe la fila de encabezados
    writer.writerows(productos)


# ─────────────────────────────────────────
#  DictReader — leer como diccionarios
# ─────────────────────────────────────────
# Cada fila se convierte en un diccionario
# usando la primera fila como claves.

with open("productos.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for fila in reader:
        print(f"{fila['nombre']} — S/. {fila['precio']}")

# Laptop  — S/. 2500
# Mouse   — S/. 45
# Teclado — S/. 120


# ─────────────────────────────────────────
#  Ejemplo práctico — filtrar datos
# ─────────────────────────────────────────
with open("estudiantes.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    aprobados = [fila for fila in reader if int(fila["nota"]) >= 13]

print("Aprobados:")
for e in aprobados:
    print(f"  {e['nombre']}: {e['nota']}")


# ─────────────────────────────────────────
#  Resumen rápido
# ─────────────────────────────────────────
#   import csv
#   csv.writer(f)              → escritor de listas
#   writer.writerow(lista)     → escribir una fila
#   writer.writerows(listas)   → escribir varias filas
#   csv.reader(f)              → lector de filas como listas
#   csv.DictWriter(f, fields)  → escritor con diccionarios
#   writer.writeheader()       → escribir encabezados
#   csv.DictReader(f)          → lector como diccionarios
#   newline=""                 → siempre en modo escritura
#   encoding="utf-8"           → siempre especificarlo
