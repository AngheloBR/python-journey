# ══════════════════════════════════════════════════════════════
#  Python Journey — by AngheloBR
#  Módulo 06: Archivos
#  Soluciones 01: Leer y escribir archivos
# ══════════════════════════════════════════════════════════════
#
#  ⚠️  Intenta resolver los ejercicios por tu cuenta primero.
#  Solo revisa esto si ya lo intentaste y no pudiste.
# ══════════════════════════════════════════════════════════════


# ─────────────────────────────────────────
#  Ejercicio 1
# ─────────────────────────────────────────
with open("mi_lista.txt", "w", encoding="utf-8") as f:
    f.write("Aprender redes\n")
    f.write("Certificación CCNA\n")
    f.write("Mejorar en Python\n")
    f.write("Practicar en Packet Tracer\n")
    f.write("Leer más libros técnicos\n")

with open("mi_lista.txt", "r", encoding="utf-8") as f:
    print(f.read())


# ─────────────────────────────────────────
#  Ejercicio 2
# ─────────────────────────────────────────
nombres = []
for i in range(3):
    nombre = input(f"Nombre {i+1}: ")
    nombres.append(nombre + "\n")

with open("nombres.txt", "w", encoding="utf-8") as f:
    f.writelines(nombres)

with open("nombres.txt", "r", encoding="utf-8") as f:
    lineas = f.readlines()
    print(f"Hay {len(lineas)} nombres guardados.")


# ─────────────────────────────────────────
#  Ejercicio 3
# ─────────────────────────────────────────
try:
    with open("contador.txt", "r", encoding="utf-8") as f:
        count = int(f.read())
except FileNotFoundError:
    count = 0

count += 1

with open("contador.txt", "w", encoding="utf-8") as f:
    f.write(str(count))

print(f"El programa se ha ejecutado {count} veces.")


# ─────────────────────────────────────────
#  Ejercicio 4
# ─────────────────────────────────────────
from datetime import datetime

try:
    with open("contador_log.txt", "r", encoding="utf-8") as f:
        numero = len(f.readlines()) + 1
except FileNotFoundError:
    numero = 1

fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open("log.txt", "a", encoding="utf-8") as f:
    f.write(f"Ejecución: {numero} | Fecha: {fecha}\n")

print(f"Log actualizado — Ejecución #{numero}")


# ─────────────────────────────────────────
#  Ejercicio 5
# ─────────────────────────────────────────
try:
    with open("fantasma.txt", "r", encoding="utf-8") as f:
        print(f.read())
except FileNotFoundError:
    print("El archivo no existía. Creándolo...")
    with open("fantasma.txt", "w", encoding="utf-8") as f:
        f.write("Este archivo fue creado automáticamente.\n")
    print("Archivo creado.")
