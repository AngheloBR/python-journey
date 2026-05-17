# ══════════════════════════════════════════════════════════════
#  Python Journey — by AngheloBR
#  Módulo 08: Módulos
#  Soluciones 01: Import, pip y entornos virtuales
# ══════════════════════════════════════════════════════════════
#
#  ⚠️  Intenta resolver los ejercicios por tu cuenta primero.
#  Solo revisa esto si ya lo intentaste y no pudiste.
# ══════════════════════════════════════════════════════════════

import math
import random
import os
import time
from datetime import datetime


# ─────────────────────────────────────────
#  Ejercicio 1
# ─────────────────────────────────────────
hipotenusa = math.sqrt(3**2 + 4**2)
print(f"Hipotenusa: {hipotenusa}")          # 5.0

print(f"Log natural de 100: {math.log(100):.4f}")  # 4.6052

print(f"Pi con 10 decimales: {math.pi:.10f}")       # 3.1415926536


# ─────────────────────────────────────────
#  Ejercicio 2
# ─────────────────────────────────────────
print("Lanzamientos del dado:")
for _ in range(10):
    print(random.randint(1, 6), end=" ")
print()

participantes = ["Ana", "Luis", "María", "Carlos", "Pedro"]
ganador = random.choice(participantes)
print(f"Ganador: {ganador}")

random.shuffle(participantes)
print(f"Lista mezclada: {participantes}")


# ─────────────────────────────────────────
#  Ejercicio 3
# ─────────────────────────────────────────
ahora = datetime.now()

print(ahora.strftime("%d/%m/%Y %H:%M:%S"))
print(f"Año actual: {ahora.year}")
print(f"Día de la semana: {ahora.weekday()}")  # 0=lunes, 6=domingo


# ─────────────────────────────────────────
#  Ejercicio 4
# ─────────────────────────────────────────
print(f"Directorio actual: {os.getcwd()}")
print(f"Archivos: {os.listdir('.')}")
print(f"¿Existe README.md? {os.path.exists('README.md')}")


# ─────────────────────────────────────────
#  Ejercicio 5
# ─────────────────────────────────────────
# Primero crea el archivo calculadora.py con este contenido:
#
# def sumar(a, b):      return a + b
# def restar(a, b):     return a - b
# def multiplicar(a, b): return a * b
# def dividir(a, b):    return a / b if b != 0 else None
#
# Luego descomenta estas líneas:

# import calculadora
# print(calculadora.sumar(10, 5))
# print(calculadora.restar(10, 5))
# print(calculadora.multiplicar(10, 5))
# print(calculadora.dividir(10, 5))


# ─────────────────────────────────────────
#  Ejercicio 6
# ─────────────────────────────────────────
inicio = time.time()

total = sum(range(1, 1_000_001))

fin = time.time()

print(f"Suma: {total}")
print(f"Tiempo: {fin - inicio:.4f} segundos")
