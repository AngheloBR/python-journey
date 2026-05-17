# ══════════════════════════════════════════════════════════════
#  Python Journey — by AngheloBR
#  Módulo 06: Archivos
#  Tema 03: JSON
# ══════════════════════════════════════════════════════════════


# ─────────────────────────────────────────
#  ¿Qué es JSON?
# ─────────────────────────────────────────
# JSON = JavaScript Object Notation.
# Es el formato más usado para intercambiar datos
# entre aplicaciones y APIs web.
# Se parece mucho a los diccionarios de Python.
#
# Ejemplo JSON:
# {
#   "nombre": "Ana",
#   "edad": 20,
#   "activo": true,
#   "cursos": ["Python", "Redes"]
# }


import json


# ─────────────────────────────────────────
#  json.dumps() — Python → string JSON
# ─────────────────────────────────────────
persona = {
    "nombre": "Ana",
    "edad": 20,
    "activo": True,
    "cursos": ["Python", "Redes"]
}

texto_json = json.dumps(persona)
print(texto_json)
print(type(texto_json))   # <class 'str'>

# Con formato legible
texto_bonito = json.dumps(persona, indent=4, ensure_ascii=False)
print(texto_bonito)


# ─────────────────────────────────────────
#  json.loads() — string JSON → Python
# ─────────────────────────────────────────
texto = '{"nombre": "Luis", "edad": 25, "activo": false}'
datos = json.loads(texto)

print(datos["nombre"])   # Luis
print(type(datos))       # <class 'dict'>


# ─────────────────────────────────────────
#  json.dump() — escribir JSON a archivo
# ─────────────────────────────────────────
usuarios = [
    {"nombre": "Ana",   "edad": 20, "ciudad": "Lima"},
    {"nombre": "Luis",  "edad": 25, "ciudad": "Cusco"},
    {"nombre": "María", "edad": 22, "ciudad": "Arequipa"}
]

with open("usuarios.json", "w", encoding="utf-8") as f:
    json.dump(usuarios, f, indent=4, ensure_ascii=False)


# ─────────────────────────────────────────
#  json.load() — leer JSON de archivo
# ─────────────────────────────────────────
with open("usuarios.json", "r", encoding="utf-8") as f:
    datos = json.load(f)

for usuario in datos:
    print(f"{usuario['nombre']} — {usuario['ciudad']}")


# ─────────────────────────────────────────
#  Tipos de datos — Python vs JSON
# ─────────────────────────────────────────
# Python       → JSON
# dict         → object {}
# list, tuple  → array []
# str          → string ""
# int, float   → number
# True/False   → true/false
# None         → null


# ─────────────────────────────────────────
#  Ejemplo práctico — guardar configuración
# ─────────────────────────────────────────
config = {
    "app": "python-journey",
    "version": "1.0",
    "idioma": "es",
    "tema": "oscuro"
}

with open("config.json", "w", encoding="utf-8") as f:
    json.dump(config, f, indent=4)

with open("config.json", "r", encoding="utf-8") as f:
    config_cargado = json.load(f)

print(f"App    : {config_cargado['app']}")
print(f"Versión: {config_cargado['version']}")
print(f"Tema   : {config_cargado['tema']}")


# ─────────────────────────────────────────
#  Resumen rápido
# ─────────────────────────────────────────
#   import json
#   json.dumps(obj)          → Python a string JSON
#   json.dumps(obj, indent=4)→ con formato legible
#   json.loads(texto)        → string JSON a Python
#   json.dump(obj, f)        → escribir JSON a archivo
#   json.load(f)             → leer JSON de archivo
#   ensure_ascii=False       → permite tildes y ñ
