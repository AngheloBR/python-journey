# ══════════════════════════════════════════════════════════════
#  Python Journey — by AngheloBR
#  Módulo 08: Módulos
#  Tema 01: Import, pip y entornos virtuales
# ══════════════════════════════════════════════════════════════


# ─────────────────────────────────────────
#  ¿Qué es un módulo?
# ─────────────────────────────────────────
# Un módulo es un archivo .py con funciones, clases y variables
# que puedes reutilizar en otros archivos.
# Python tiene módulos integrados (stdlib) y externos (pip).


# ─────────────────────────────────────────
#  import — importar módulos
# ─────────────────────────────────────────
import math

print(math.pi)           # 3.141592653589793
print(math.sqrt(16))     # 4.0
print(math.floor(3.9))   # 3
print(math.ceil(3.1))    # 4
print(math.pow(2, 8))    # 256.0


# ─────────────────────────────────────────
#  from ... import — importar específico
# ─────────────────────────────────────────
from math import sqrt, pi

print(sqrt(25))   # 5.0  (sin math.)
print(pi)         # 3.14...


# ─────────────────────────────────────────
#  import ... as — alias
# ─────────────────────────────────────────
import math as m

print(m.sqrt(9))   # 3.0

from math import factorial as fact
print(fact(5))     # 120


# ─────────────────────────────────────────
#  Módulos útiles de la stdlib
# ─────────────────────────────────────────

# random — números aleatorios
import random

print(random.randint(1, 10))        # entero aleatorio entre 1 y 10
print(random.random())              # float entre 0.0 y 1.0
print(random.choice(["a", "b", "c"]))  # elemento aleatorio
lista = [1, 2, 3, 4, 5]
random.shuffle(lista)
print(lista)                        # lista mezclada

# datetime — fechas y horas
from datetime import datetime, date

ahora = datetime.now()
print(ahora)                              # 2024-01-15 14:30:00
print(ahora.strftime("%d/%m/%Y %H:%M"))  # 15/01/2024 14:30
hoy = date.today()
print(hoy)                               # 2024-01-15

# os — sistema operativo
import os

print(os.getcwd())           # directorio actual
print(os.listdir("."))       # archivos en el directorio
print(os.path.exists("README.md"))  # True/False

# sys — información del sistema
import sys

print(sys.version)           # versión de Python
print(sys.platform)          # linux / win32 / darwin

# time — tiempo
import time

print(time.time())           # segundos desde 1970
time.sleep(1)                # pausa 1 segundo
print("Pasó 1 segundo.")


# ─────────────────────────────────────────
#  Crear tu propio módulo
# ─────────────────────────────────────────
# Simplemente crea un archivo .py con funciones.
#
# archivo: utilidades.py
# ──────────────────────
# def saludar(nombre):
#     return f"Hola, {nombre}!"
#
# def sumar(a, b):
#     return a + b
# ──────────────────────
#
# En otro archivo:
# import utilidades
# print(utilidades.saludar("Ana"))
# print(utilidades.sumar(3, 5))


# ─────────────────────────────────────────
#  pip — instalar paquetes externos
# ─────────────────────────────────────────
# pip es el gestor de paquetes de Python.
# Se ejecuta desde la terminal, no desde Python.
#
# Comandos principales:
#   pip install requests        → instalar
#   pip uninstall requests      → desinstalar
#   pip list                    → listar instalados
#   pip show requests           → info de un paquete
#   pip freeze > requirements.txt → exportar dependencias
#   pip install -r requirements.txt → instalar desde archivo


# ─────────────────────────────────────────
#  Entornos virtuales
# ─────────────────────────────────────────
# Un entorno virtual aísla las dependencias de cada proyecto.
# Así evitas conflictos entre versiones de paquetes.
#
# Crear y activar:
#   python -m venv env          → crear entorno
#   source env/bin/activate     → activar (Linux/Mac)
#   env\Scripts\activate        → activar (Windows)
#   deactivate                  → desactivar
#
# Una vez activado, pip instala solo en ese entorno.


# ─────────────────────────────────────────
#  __name__ == "__main__"
# ─────────────────────────────────────────
# Permite que un archivo funcione como módulo Y como script.
# El código dentro del if solo se ejecuta cuando corres
# el archivo directamente, no cuando lo importas.

def main():
    print("Ejecutando como script principal.")

if __name__ == "__main__":
    main()


# ─────────────────────────────────────────
#  Resumen rápido
# ─────────────────────────────────────────
#   import modulo              → importar módulo completo
#   from modulo import func    → importar específico
#   import modulo as alias     → con alias
#   math, random, datetime, os, sys, time → stdlib útiles
#   pip install paquete        → instalar externo
#   python -m venv env         → crear entorno virtual
#   if __name__ == "__main__": → solo al ejecutar directo
