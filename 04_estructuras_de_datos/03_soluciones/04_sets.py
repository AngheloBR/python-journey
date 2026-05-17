# ══════════════════════════════════════════════════════════════
#  Python Journey — by AngheloBR
#  Módulo 04: Estructuras de datos
#  Soluciones 04: Sets
# ══════════════════════════════════════════════════════════════
#
#  ⚠️  Intenta resolver los ejercicios por tu cuenta primero.
#  Solo revisa esto si ya lo intentaste y no pudiste.
# ══════════════════════════════════════════════════════════════


# ─────────────────────────────────────────
#  Ejercicio 1
# ─────────────────────────────────────────
numeros = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
unicos = set(numeros)

print(f"Números únicos: {unicos}")
print(f"Cantidad: {len(unicos)}")   # 7


# ─────────────────────────────────────────
#  Ejercicio 2
# ─────────────────────────────────────────
idiomas = {"python", "java", "rust"}

idiomas.add("kotlin")
idiomas.add("go")
idiomas.add("python")   # no se duplica
idiomas.remove("java")

print(idiomas)   # {'python', 'rust', 'kotlin', 'go'}


# ─────────────────────────────────────────
#  Ejercicio 3
# ─────────────────────────────────────────
grupo_a = {"Ana", "Luis", "María", "Pedro"}
grupo_b = {"María", "Pedro", "Carlos", "Sofía"}

print(f"En ambos grupos : {grupo_a & grupo_b}")
print(f"Todos           : {grupo_a | grupo_b}")
print(f"Solo en grupo A : {grupo_a - grupo_b}")


# ─────────────────────────────────────────
#  Ejercicio 4
# ─────────────────────────────────────────
primos = {2, 3, 5, 7, 11, 13}
pares  = {2, 4, 6, 8, 10, 12}

print(f"Primo y par: {primos & pares}")   # {2}


# ─────────────────────────────────────────
#  Ejercicio 5
# ─────────────────────────────────────────
palabras = ["sol", "luna", "sol", "mar", "luna", "sol", "río"]
unicas = set(palabras)

print(f"Palabras únicas ({len(unicas)}): {unicas}")


# ─────────────────────────────────────────
#  Ejercicio 6
# ─────────────────────────────────────────
permisos_admin = {"leer", "escribir", "eliminar", "crear"}
permisos_user  = {"leer", "crear"}

print(permisos_user.issubset(permisos_admin))        # True
print(f"Solo admin: {permisos_admin - permisos_user}")  # {'escribir', 'eliminar'}
