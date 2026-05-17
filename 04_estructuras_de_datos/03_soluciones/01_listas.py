# ══════════════════════════════════════════════════════════════
#  Python Journey — by AngheloBR
#  Módulo 04: Estructuras de datos
#  Soluciones 01: Listas
# ══════════════════════════════════════════════════════════════
#
#  ⚠️  Intenta resolver los ejercicios por tu cuenta primero.
#  Solo revisa esto si ya lo intentaste y no pudiste.
# ══════════════════════════════════════════════════════════════


# ─────────────────────────────────────────
#  Ejercicio 1
# ─────────────────────────────────────────
numeros = [10, 20, 30, 40, 50]

print(numeros[0])            # 10
print(numeros[-1])           # 50
print(numeros[len(numeros) // 2])  # 30


# ─────────────────────────────────────────
#  Ejercicio 2
# ─────────────────────────────────────────
letras = ["a", "b", "c", "d", "e", "f", "g"]

print(letras[:3])     # ['a', 'b', 'c']
print(letras[-3:])    # ['e', 'f', 'g']
print(letras[::2])    # ['a', 'c', 'e', 'g']


# ─────────────────────────────────────────
#  Ejercicio 3
# ─────────────────────────────────────────
compras = []
compras.append("leche")
compras.append("pan")
compras.append("huevos")
compras.append("arroz")
compras.append("aceite")

compras.pop(1)   # elimina "pan" (índice 1)
print(compras)   # ['leche', 'huevos', 'arroz', 'aceite']


# ─────────────────────────────────────────
#  Ejercicio 4
# ─────────────────────────────────────────
notas = [14, 18, 11, 16, 9, 20, 13]

print(f"Más alta : {max(notas)}")
print(f"Más baja : {min(notas)}")
print(f"Promedio : {sum(notas)/len(notas):.2f}")
print(f"Ordenadas: {sorted(notas, reverse=True)}")


# ─────────────────────────────────────────
#  Ejercicio 5
# ─────────────────────────────────────────
cubos = [x ** 3 for x in range(1, 6)]
print(cubos)   # [1, 8, 27, 64, 125]

divisibles = [x for x in range(1, 21) if x % 4 == 0]
print(divisibles)   # [4, 8, 12, 16, 20]


# ─────────────────────────────────────────
#  Ejercicio 6
# ─────────────────────────────────────────
palabras = ["python", "java", "rust", "go", "kotlin"]

largas = [p for p in palabras if len(p) > 4]
print(largas)   # ['python', 'kotlin']
