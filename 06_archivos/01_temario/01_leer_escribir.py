# ══════════════════════════════════════════════════════════════
#  Python Journey — by AngheloBR
#  Módulo 06: Archivos
#  Tema 01: Leer y escribir archivos
# ══════════════════════════════════════════════════════════════


# ─────────────────────────────────────────
#  ¿Por qué trabajar con archivos?
# ─────────────────────────────────────────
# Los datos en variables desaparecen al cerrar el programa.
# Los archivos permiten guardar y recuperar información
# de forma permanente.


# ─────────────────────────────────────────
#  open() — abrir un archivo
# ─────────────────────────────────────────
# Sintaxis: open(ruta, modo)
#
# Modos:
#   "r"  → leer (por defecto) — error si no existe
#   "w"  → escribir — crea si no existe, sobreescribe si existe
#   "a"  → agregar al final — crea si no existe
#   "x"  → crear — error si ya existe
#   "r+" → leer y escribir


# ─────────────────────────────────────────
#  Escribir un archivo
# ─────────────────────────────────────────
# Siempre cierra el archivo con close() o usa with.

archivo = open("notas.txt", "w")
archivo.write("Primera línea\n")
archivo.write("Segunda línea\n")
archivo.write("Tercera línea\n")
archivo.close()


# ─────────────────────────────────────────
#  with — la forma recomendada
# ─────────────────────────────────────────
# Cierra el archivo automáticamente al salir del bloque.

with open("notas.txt", "w") as archivo:
    archivo.write("Primera línea\n")
    archivo.write("Segunda línea\n")
    archivo.write("Tercera línea\n")

# Al salir del with, el archivo ya está cerrado.


# ─────────────────────────────────────────
#  Leer un archivo
# ─────────────────────────────────────────
# read()      → lee todo el contenido como string
# readline()  → lee una sola línea
# readlines() → lee todas las líneas como lista

with open("notas.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)

# Leer línea por línea (eficiente para archivos grandes)
with open("notas.txt", "r") as archivo:
    for linea in archivo:
        print(linea.strip())   # strip() elimina el \n

# readlines() → lista de líneas
with open("notas.txt", "r") as archivo:
    lineas = archivo.readlines()
    print(lineas)   # ['Primera línea\n', 'Segunda línea\n', ...]


# ─────────────────────────────────────────
#  Agregar contenido sin sobreescribir
# ─────────────────────────────────────────
with open("notas.txt", "a") as archivo:
    archivo.write("Cuarta línea\n")


# ─────────────────────────────────────────
#  writelines() — escribir lista de líneas
# ─────────────────────────────────────────
lineas = ["manzana\n", "pera\n", "uva\n"]

with open("frutas.txt", "w") as archivo:
    archivo.writelines(lineas)


# ─────────────────────────────────────────
#  Manejo de errores al abrir archivos
# ─────────────────────────────────────────
try:
    with open("no_existe.txt", "r") as archivo:
        print(archivo.read())
except FileNotFoundError:
    print("El archivo no existe.")


# ─────────────────────────────────────────
#  encoding — caracteres especiales
# ─────────────────────────────────────────
# Siempre especifica encoding="utf-8" para evitar problemas
# con tildes, ñ y otros caracteres especiales.

with open("español.txt", "w", encoding="utf-8") as archivo:
    archivo.write("Ñoño con tíldes y todo\n")

with open("español.txt", "r", encoding="utf-8") as archivo:
    print(archivo.read())


# ─────────────────────────────────────────
#  Resumen rápido
# ─────────────────────────────────────────
#   open(ruta, "r")          → leer
#   open(ruta, "w")          → escribir (sobreescribe)
#   open(ruta, "a")          → agregar al final
#   with open(...) as f:     → forma recomendada
#   f.read()                 → todo el contenido
#   f.readline()             → una línea
#   f.readlines()            → lista de líneas
#   f.write(texto)           → escribir texto
#   f.writelines(lista)      → escribir lista
#   encoding="utf-8"         → siempre usarlo
