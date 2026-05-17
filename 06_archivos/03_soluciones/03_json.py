# ══════════════════════════════════════════════════════════════
#  Python Journey — by AngheloBR
#  Módulo 06: Archivos
#  Soluciones 03: JSON
# ══════════════════════════════════════════════════════════════
#
#  ⚠️  Intenta resolver los ejercicios por tu cuenta primero.
#  Solo revisa esto si ya lo intentaste y no pudiste.
# ══════════════════════════════════════════════════════════════

import json


# ─────────────────────────────────────────
#  Ejercicio 1
# ─────────────────────────────────────────
perfil = {
    "nombre": "Anghelo",
    "edad": 21,
    "ciudad": "Lima",
    "hobbies": ["programar", "fútbol", "música"],
    "activo": True
}

texto = json.dumps(perfil, indent=4, ensure_ascii=False)
print(texto)

recuperado = json.loads(texto)
print(type(recuperado))   # <class 'dict'>
print(recuperado["nombre"])


# ─────────────────────────────────────────
#  Ejercicio 2
# ─────────────────────────────────────────
libros = [
    {"titulo": "El Principito",    "autor": "Saint-Exupéry", "año": 1943, "leido": True},
    {"titulo": "1984",             "autor": "Orwell",        "año": 1949, "leido": False},
    {"titulo": "Clean Code",       "autor": "Martin",        "año": 2008, "leido": True},
    {"titulo": "The Pragmatic",    "autor": "Hunt & Thomas", "año": 1999, "leido": False},
]

with open("libros.json", "w", encoding="utf-8") as f:
    json.dump(libros, f, indent=4, ensure_ascii=False)

with open("libros.json", "r", encoding="utf-8") as f:
    datos = json.load(f)

print("Libros leídos:")
for libro in datos:
    if libro["leido"]:
        print(f"  - {libro['titulo']} ({libro['autor']})")


# ─────────────────────────────────────────
#  Ejercicio 3
# ─────────────────────────────────────────
try:
    with open("mis_notas.json", "r", encoding="utf-8") as f:
        notas = json.load(f)
except FileNotFoundError:
    notas = []

nueva_nota = input("Escribe una nota: ")
notas.append(nueva_nota)

with open("mis_notas.json", "w", encoding="utf-8") as f:
    json.dump(notas, f, indent=4, ensure_ascii=False)

print(f"\nNotas guardadas ({len(notas)}):")
for i, nota in enumerate(notas, 1):
    print(f"  {i}. {nota}")


# ─────────────────────────────────────────
#  Ejercicio 4
# ─────────────────────────────────────────
datos = '[{"producto": "Laptop", "precio": 2500}, {"producto": "Mouse", "precio": 45}]'
productos = json.loads(datos)

total = sum(p["precio"] for p in productos)
print(f"Total: S/. {total}")   # S/. 2545


# ─────────────────────────────────────────
#  Ejercicio 5
# ─────────────────────────────────────────
config = {
    "idioma": "es",
    "tema": "oscuro",
    "notificaciones": True,
    "volumen": 75
}

with open("preferencias.json", "w", encoding="utf-8") as f:
    json.dump(config, f, indent=4)

with open("preferencias.json", "r", encoding="utf-8") as f:
    cfg = json.load(f)

for clave, valor in cfg.items():
    print(f"{clave}: {valor}")

cfg["tema"] = "claro"

with open("preferencias.json", "w", encoding="utf-8") as f:
    json.dump(cfg, f, indent=4)

print("\nTema actualizado a:", cfg["tema"])
