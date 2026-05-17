# ══════════════════════════════════════════════════════════════
#  Python Journey — by AngheloBR
#  Módulo 03: Funciones
#  Soluciones 04: Recursividad
# ══════════════════════════════════════════════════════════════
#
#  ⚠️  Intenta resolver los ejercicios por tu cuenta primero.
#  Solo revisa esto si ya lo intentaste y no pudiste.
# ══════════════════════════════════════════════════════════════


# ─────────────────────────────────────────
#  Ejercicio 1
# ─────────────────────────────────────────
def contar(n, actual=1):
    if actual > n:      # caso base
        return
    print(actual, end=" ")
    contar(n, actual + 1)

contar(5)   # 1 2 3 4 5


# ─────────────────────────────────────────
#  Ejercicio 2
# ─────────────────────────────────────────
def potencia(base, exponente):
    if exponente == 0:     # caso base
        return 1
    return base * potencia(base, exponente - 1)

print(potencia(2, 4))   # 16
print(potencia(3, 3))   # 27


# ─────────────────────────────────────────
#  Ejercicio 3
# ─────────────────────────────────────────
def sumar_digitos(n):
    if n < 10:          # caso base — un solo dígito
        return n
    return n % 10 + sumar_digitos(n // 10)

print(sumar_digitos(123))    # 6
print(sumar_digitos(9999))   # 36


# ─────────────────────────────────────────
#  Ejercicio 4
# ─────────────────────────────────────────
def invertir_string(s):
    if len(s) == 0:     # caso base
        return ""
    return s[-1] + invertir_string(s[:-1])

print(invertir_string("Python"))   # nohtyP
print(invertir_string("hola"))     # aloh


# ─────────────────────────────────────────
#  Ejercicio 5
# ─────────────────────────────────────────
def es_palindromo(s):
    if len(s) <= 1:              # caso base
        return True
    if s[0] != s[-1]:            # primero y último distintos
        return False
    return es_palindromo(s[1:-1])  # compara el resto

print(es_palindromo("radar"))    # True
print(es_palindromo("python"))   # False
print(es_palindromo("anilina"))  # True
