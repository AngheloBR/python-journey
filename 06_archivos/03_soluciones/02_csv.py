# ══════════════════════════════════════════════════════════════
#  Python Journey — by AngheloBR
#  Módulo 06: Archivos
#  Soluciones 02: CSV
# ══════════════════════════════════════════════════════════════
#
#  ⚠️  Intenta resolver los ejercicios por tu cuenta primero.
#  Solo revisa esto si ya lo intentaste y no pudiste.
# ══════════════════════════════════════════════════════════════

import csv


# ─────────────────────────────────────────
#  Ejercicio 1
# ─────────────────────────────────────────
contactos = [
    {"nombre": "Ana",    "telefono": "999111222", "email": "ana@mail.com"},
    {"nombre": "Luis",   "telefono": "999333444", "email": "luis@mail.com"},
    {"nombre": "María",  "telefono": "999555666", "email": "maria@mail.com"},
    {"nombre": "Carlos", "telefono": "999777888", "email": "carlos@mail.com"},
]

with open("contactos.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["nombre", "telefono", "email"])
    writer.writeheader()
    writer.writerows(contactos)

with open("contactos.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for c in reader:
        print(f"{c['nombre']} | {c['telefono']} | {c['email']}")


# ─────────────────────────────────────────
#  Ejercicio 2
# ─────────────────────────────────────────
with open("estudiantes.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    datos = list(reader)

notas = [int(e["nota"]) for e in datos]
promedio = sum(notas) / len(notas)
mejor = max(datos, key=lambda e: int(e["nota"]))

print(f"Promedio general: {promedio:.2f}")
print(f"Mejor estudiante: {mejor['nombre']} con {mejor['nota']}")


# ─────────────────────────────────────────
#  Ejercicio 3
# ─────────────────────────────────────────
productos = []

while True:
    nombre = input("Nombre del producto (o 'fin'): ")
    if nombre == "fin":
        break
    precio = float(input("Precio: "))
    cantidad = int(input("Cantidad: "))
    productos.append({"nombre": nombre, "precio": precio, "cantidad": cantidad})

with open("inventario.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["nombre", "precio", "cantidad"])
    writer.writeheader()
    writer.writerows(productos)

total = 0
with open("inventario.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for p in reader:
        subtotal = float(p["precio"]) * int(p["cantidad"])
        total += subtotal

print(f"Valor total del inventario: S/. {total:.2f}")


# ─────────────────────────────────────────
#  Ejercicio 4
# ─────────────────────────────────────────
ventas_data = [
    {"dia": "Lunes",     "ventas": 1500},
    {"dia": "Martes",    "ventas": 2300},
    {"dia": "Miércoles", "ventas": 980},
    {"dia": "Jueves",    "ventas": 3100},
    {"dia": "Viernes",   "ventas": 2750},
]

with open("ventas.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["dia", "ventas"])
    writer.writeheader()
    writer.writerows(ventas_data)

with open("ventas.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    datos = list(reader)

ventas = [(d["dia"], int(d["ventas"])) for d in datos]
total = sum(v for _, v in ventas)
mejor_dia = max(ventas, key=lambda x: x[1])
peor_dia = min(ventas, key=lambda x: x[1])

print(f"Más ventas   : {mejor_dia[0]} — S/. {mejor_dia[1]}")
print(f"Menos ventas : {peor_dia[0]} — S/. {peor_dia[1]}")
print(f"Total semana : S/. {total}")
