# ══════════════════════════════════════════════════════════════
#  Python Journey — by AngheloBR
#  Módulo 07: Excepciones
#  Soluciones 01: Manejo de excepciones
# ══════════════════════════════════════════════════════════════
#
#  ⚠️  Intenta resolver los ejercicios por tu cuenta primero.
#  Solo revisa esto si ya lo intentaste y no pudiste.
# ══════════════════════════════════════════════════════════════

import json


# ─────────────────────────────────────────
#  Ejercicio 1
# ─────────────────────────────────────────
try:
    a = float(input("Primer número: "))
    b = float(input("Segundo número: "))
    print(f"Resultado: {a / b}")
except ZeroDivisionError:
    print("Error: no se puede dividir entre cero.")
except ValueError:
    print("Error: debes ingresar números válidos.")


# ─────────────────────────────────────────
#  Ejercicio 2
# ─────────────────────────────────────────
def buscar_elemento(lista, indice):
    try:
        return lista[indice]
    except IndexError:
        print(f"Error: índice {indice} fuera de rango.")
    except TypeError:
        print("Error: el índice debe ser un número entero.")

print(buscar_elemento([10, 20, 30], 1))    # 20
print(buscar_elemento([10, 20, 30], 10))   # error índice
print(buscar_elemento([10, 20, 30], "a"))  # error tipo


# ─────────────────────────────────────────
#  Ejercicio 3
# ─────────────────────────────────────────
def obtener_valor(diccionario, clave):
    if clave not in diccionario:
        raise KeyError(f"La clave '{clave}' no existe en el diccionario.")
    return diccionario[clave]

datos = {"nombre": "Ana", "edad": 20}

try:
    print(obtener_valor(datos, "nombre"))
    print(obtener_valor(datos, "email"))
except KeyError as e:
    print(f"Error: {e}")


# ─────────────────────────────────────────
#  Ejercicio 4
# ─────────────────────────────────────────
class EdadInvalida(Exception):
    pass

def registrar_usuario(nombre, edad):
    if edad < 0 or edad > 120:
        raise EdadInvalida(f"Edad {edad} no válida. Debe estar entre 0 y 120.")
    print(f"Usuario {nombre} registrado.")

try:
    registrar_usuario("Ana", 25)
    registrar_usuario("Luis", -5)
except EdadInvalida as e:
    print(f"Error: {e}")


# ─────────────────────────────────────────
#  Ejercicio 5
# ─────────────────────────────────────────
total = 0

while True:
    entrada = input("Ingresa un número (o 'fin'): ")
    if entrada == "fin":
        break
    try:
        numero = float(entrada)
        total += numero
    except ValueError:
        print(f"'{entrada}' no es un número válido. Intenta de nuevo.")

print(f"Suma total: {total}")


# ─────────────────────────────────────────
#  Ejercicio 6
# ─────────────────────────────────────────
def leer_json_seguro(ruta):
    try:
        with open(ruta, "r", encoding="utf-8") as f:
            datos = json.load(f)
            print("Archivo leído correctamente.")
            return datos
    except FileNotFoundError:
        print(f"Error: el archivo '{ruta}' no existe.")
    except json.JSONDecodeError as e:
        print(f"Error: el archivo no tiene formato JSON válido. {e}")
    finally:
        print("Operación terminada.")

leer_json_seguro("usuarios.json")
leer_json_seguro("no_existe.json")
