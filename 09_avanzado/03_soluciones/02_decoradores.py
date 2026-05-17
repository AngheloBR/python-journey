# ══════════════════════════════════════════════════════════════
#  Python Journey — by AngheloBR
#  Módulo 09: Avanzado
#  Soluciones 02: Decoradores
# ══════════════════════════════════════════════════════════════
#
#  ⚠️  Intenta resolver los ejercicios por tu cuenta primero.
#  Solo revisa esto si ya lo intentaste y no pudiste.
# ══════════════════════════════════════════════════════════════

import time


# ─────────────────────────────────────────
#  Ejercicio 1
# ─────────────────────────────────────────
def logger(funcion):
    def wrapper(*args, **kwargs):
        print(f"▶ Ejecutando: {funcion.__name__}")
        resultado = funcion(*args, **kwargs)
        print(f"✓ Terminó: {funcion.__name__}")
        return resultado
    return wrapper

@logger
def saludar():
    print("¡Hola!")

@logger
def sumar(a, b):
    return a + b

saludar()
print(sumar(3, 5))


# ─────────────────────────────────────────
#  Ejercicio 2
# ─────────────────────────────────────────
def validar_positivos(funcion):
    def wrapper(*args, **kwargs):
        for arg in args:
            if isinstance(arg, (int, float)) and arg <= 0:
                print(f"Error: todos los valores deben ser positivos. Recibido: {arg}")
                return None
        return funcion(*args, **kwargs)
    return wrapper

@validar_positivos
def calcular_area(base, altura):
    return base * altura

print(calcular_area(5, 3))    # 15
print(calcular_area(-2, 3))   # error


# ─────────────────────────────────────────
#  Ejercicio 3
# ─────────────────────────────────────────
def cronometro(funcion):
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = funcion(*args, **kwargs)
        fin = time.time()
        print(f"{funcion.__name__} tardó {fin - inicio:.6f} segundos")
        return resultado
    return wrapper

@cronometro
def suma_grande():
    return sum(range(1, 500_001))

print(suma_grande())


# ─────────────────────────────────────────
#  Ejercicio 4
# ─────────────────────────────────────────
def repetir(n):
    def decorador(funcion):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                funcion(*args, **kwargs)
        return wrapper
    return decorador

@repetir(3)
def saludar():
    print("¡Hola!")

saludar()
# ¡Hola!
# ¡Hola!
# ¡Hola!
