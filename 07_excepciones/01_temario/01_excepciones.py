# ══════════════════════════════════════════════════════════════
#  Python Journey — by AngheloBR
#  Módulo 07: Excepciones
#  Tema 01: Manejo de excepciones
# ══════════════════════════════════════════════════════════════


# ─────────────────────────────────────────
#  ¿Qué es una excepción?
# ─────────────────────────────────────────
# Una excepción es un error que ocurre durante la ejecución.
# Si no se maneja, el programa se detiene.
# Python tiene muchos tipos de excepciones integradas.


# ─────────────────────────────────────────
#  Excepciones comunes
# ─────────────────────────────────────────
# ZeroDivisionError  → dividir entre 0
# TypeError          → operación con tipo incorrecto
# ValueError         → valor incorrecto para el tipo
# NameError          → variable no definida
# IndexError         → índice fuera de rango
# KeyError           → clave no existe en diccionario
# FileNotFoundError  → archivo no encontrado
# AttributeError     → atributo no existe
# ImportError        → módulo no encontrado


# ─────────────────────────────────────────
#  try / except — capturar errores
# ─────────────────────────────────────────
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("No se puede dividir entre cero.")

# El programa sigue ejecutándose


# ─────────────────────────────────────────
#  Capturar múltiples excepciones
# ─────────────────────────────────────────
def dividir(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Error: división entre cero.")
    except TypeError:
        print("Error: los valores deben ser números.")

dividir(10, 0)
dividir(10, "dos")
print(dividir(10, 2))   # 5.0


# ─────────────────────────────────────────
#  except Exception as e — capturar el mensaje
# ─────────────────────────────────────────
try:
    lista = [1, 2, 3]
    print(lista[10])
except IndexError as e:
    print(f"Error de índice: {e}")


# ─────────────────────────────────────────
#  else — si NO hubo error
# ─────────────────────────────────────────
try:
    numero = int("42")
except ValueError:
    print("No es un número válido.")
else:
    print(f"Conversión exitosa: {numero}")   # se ejecuta solo si no hubo error


# ─────────────────────────────────────────
#  finally — siempre se ejecuta
# ─────────────────────────────────────────
try:
    archivo = open("datos.txt", "r")
    contenido = archivo.read()
except FileNotFoundError:
    print("El archivo no existe.")
finally:
    print("Operación terminada.")   # se ejecuta siempre


# ─────────────────────────────────────────
#  try / except / else / finally completo
# ─────────────────────────────────────────
def leer_numero(texto):
    try:
        numero = int(texto)
    except ValueError as e:
        print(f"Error: {e}")
        return None
    else:
        print("Conversión exitosa.")
        return numero
    finally:
        print("Intento de conversión terminado.")

leer_numero("42")
leer_numero("abc")


# ─────────────────────────────────────────
#  raise — lanzar excepciones manualmente
# ─────────────────────────────────────────
def validar_edad(edad):
    if edad < 0:
        raise ValueError("La edad no puede ser negativa.")
    if edad > 120:
        raise ValueError("La edad no puede ser mayor a 120.")
    return edad

try:
    validar_edad(-5)
except ValueError as e:
    print(f"Error: {e}")


# ─────────────────────────────────────────
#  Excepciones personalizadas
# ─────────────────────────────────────────
class SaldoInsuficiente(Exception):
    def __init__(self, saldo, monto):
        super().__init__(f"Saldo insuficiente. Tienes S/. {saldo}, intentas retirar S/. {monto}.")

def retirar(saldo, monto):
    if monto > saldo:
        raise SaldoInsuficiente(saldo, monto)
    return saldo - monto

try:
    retirar(100, 200)
except SaldoInsuficiente as e:
    print(e)


# ─────────────────────────────────────────
#  Resumen rápido
# ─────────────────────────────────────────
#   try:                  → bloque que puede fallar
#   except Error:         → captura el error
#   except Error as e:    → captura con mensaje
#   except (E1, E2):      → captura varios tipos
#   else:                 → se ejecuta si NO hubo error
#   finally:              → se ejecuta SIEMPRE
#   raise Error("msg")    → lanzar error manualmente
#   class MiError(Exception): → excepción personalizada
