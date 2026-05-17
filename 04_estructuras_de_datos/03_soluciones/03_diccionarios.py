# ══════════════════════════════════════════════════════════════
#  Python Journey — by AngheloBR
#  Módulo 04: Estructuras de datos
#  Soluciones 03: Diccionarios
# ══════════════════════════════════════════════════════════════
#
#  ⚠️  Intenta resolver los ejercicios por tu cuenta primero.
#  Solo revisa esto si ya lo intentaste y no pudiste.
# ══════════════════════════════════════════════════════════════


# ─────────────────────────────────────────
#  Ejercicio 1
# ─────────────────────────────────────────
producto = {
    "nombre": "Laptop",
    "precio": 2999.99,
    "stock": 10,
    "disponible": True
}

print(producto["nombre"])
print(producto["precio"])
print(producto["stock"])
print(producto["disponible"])


# ─────────────────────────────────────────
#  Ejercicio 2
# ─────────────────────────────────────────
contacto = {"nombre": "Luis", "telefono": "999888777"}

contacto["email"] = "luis@mail.com"
contacto["ciudad"] = "Lima"
contacto["telefono"] = "111222333"
del contacto["ciudad"]

print(contacto)


# ─────────────────────────────────────────
#  Ejercicio 3
# ─────────────────────────────────────────
notas = {"Ana": 18, "Luis": 11, "María": 16, "Carlos": 9, "Pedro": 14}

print(list(notas.keys()))
print(list(notas.values()))

for nombre, nota in notas.items():
    print(f"{nombre}: {nota}")


# ─────────────────────────────────────────
#  Ejercicio 4
# ─────────────────────────────────────────
notas = {"Ana": 18, "Luis": 11, "María": 16, "Carlos": 9, "Pedro": 14}

aprobados = 0
reprobados = 0

for nota in notas.values():
    if nota >= 13:
        aprobados += 1
    else:
        reprobados += 1

print(f"Aprobados : {aprobados}")
print(f"Reprobados: {reprobados}")


# ─────────────────────────────────────────
#  Ejercicio 5
# ─────────────────────────────────────────
paridad = {x: "par" if x % 2 == 0 else "impar" for x in range(1, 9)}
print(paridad)


# ─────────────────────────────────────────
#  Ejercicio 6
# ─────────────────────────────────────────
inventario = {
    "laptop":  {"precio": 2500, "stock": 5},
    "mouse":   {"precio": 45,   "stock": 20},
    "teclado": {"precio": 120,  "stock": 12}
}

total = 0

for producto, datos in inventario.items():
    subtotal = datos["precio"] * datos["stock"]
    total += subtotal
    print(f"{producto:<10} → S/. {datos['precio']} x {datos['stock']} = S/. {subtotal}")

print(f"\nValor total del inventario: S/. {total}")
