# ══════════════════════════════════════════════════════════════
#  Python Journey — by AngheloBR
#  Módulo 04: Estructuras de datos
#  Tema 03: Diccionarios
# ══════════════════════════════════════════════════════════════


# ─────────────────────────────────────────
#  ¿Qué es un diccionario?
# ─────────────────────────────────────────
# Un diccionario es una colección de pares clave:valor.
# Cada clave es única y se usa para acceder a su valor.
# Son mutables y no tienen orden garantizado (desde Python 3.7 sí mantienen orden de inserción).

persona = {
    "nombre": "Ana",
    "edad": 20,
    "ciudad": "Lima"
}

print(type(persona))   # <class 'dict'>


# ─────────────────────────────────────────
#  Acceder a valores
# ─────────────────────────────────────────
print(persona["nombre"])          # Ana
print(persona.get("edad"))        # 20
print(persona.get("email", "N/A")) # N/A → valor por defecto si no existe

# ⚠️ persona["email"] lanzaría KeyError si no existe
# persona.get("email") devuelve None sin error


# ─────────────────────────────────────────
#  Agregar y modificar
# ─────────────────────────────────────────
persona["email"] = "ana@mail.com"   # agregar nueva clave
persona["edad"] = 21                # modificar valor existente
print(persona)


# ─────────────────────────────────────────
#  Eliminar elementos
# ─────────────────────────────────────────
del persona["email"]               # elimina la clave
edad = persona.pop("edad")         # elimina y retorna el valor
print(edad)     # 21
persona.clear()                    # vacía el diccionario
print(persona)  # {}


# ─────────────────────────────────────────
#  Métodos principales
# ─────────────────────────────────────────
alumno = {
    "nombre": "Luis",
    "nota": 18,
    "curso": "Python"
}

print(alumno.keys())    # dict_keys(['nombre', 'nota', 'curso'])
print(alumno.values())  # dict_values(['Luis', 18, 'Python'])
print(alumno.items())   # dict_items([('nombre','Luis'), ('nota',18), ('curso','Python')])

# Verificar si una clave existe
print("nota" in alumno)      # True
print("email" in alumno)     # False


# ─────────────────────────────────────────
#  Iterar sobre un diccionario
# ─────────────────────────────────────────
# Solo claves
for clave in alumno:
    print(clave)

# Claves y valores
for clave, valor in alumno.items():
    print(f"{clave}: {valor}")


# ─────────────────────────────────────────
#  Diccionarios anidados
# ─────────────────────────────────────────
estudiantes = {
    "ana": {"nota": 18, "ciudad": "Lima"},
    "luis": {"nota": 14, "ciudad": "Cusco"}
}

print(estudiantes["ana"]["nota"])    # 18
print(estudiantes["luis"]["ciudad"]) # Cusco


# ─────────────────────────────────────────
#  Dict comprehension
# ─────────────────────────────────────────
cuadrados = {x: x ** 2 for x in range(1, 6)}
print(cuadrados)   # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Filtrar un diccionario
notas = {"Ana": 18, "Luis": 11, "María": 16, "Carlos": 9}
aprobados = {nombre: nota for nombre, nota in notas.items() if nota >= 13}
print(aprobados)   # {'Ana': 18, 'María': 16}


# ─────────────────────────────────────────
#  Resumen rápido
# ─────────────────────────────────────────
#   {"clave": valor}       → crear diccionario
#   dic["clave"]           → acceder (KeyError si no existe)
#   dic.get("clave")       → acceder (None si no existe)
#   dic["clave"] = valor   → agregar o modificar
#   del dic["clave"]       → eliminar
#   dic.pop("clave")       → eliminar y retornar valor
#   dic.keys()             → todas las claves
#   dic.values()           → todos los valores
#   dic.items()            → pares clave:valor
#   "clave" in dic         → verificar existencia
#   {k: v for k, v in ...} → dict comprehension
