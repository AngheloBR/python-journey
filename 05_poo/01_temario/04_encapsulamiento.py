# ══════════════════════════════════════════════════════════════
#  Python Journey — by AngheloBR
#  Módulo 05: POO
#  Tema 04: Encapsulamiento
# ══════════════════════════════════════════════════════════════


# ─────────────────────────────────────────
#  ¿Qué es el encapsulamiento?
# ─────────────────────────────────────────
# Encapsulamiento significa proteger los datos internos
# de una clase y controlar cómo se accede a ellos.
# Evita que el código externo modifique atributos directamente
# sin pasar por los métodos de la clase.


# ─────────────────────────────────────────
#  Niveles de acceso en Python
# ─────────────────────────────────────────
# Python no tiene acceso privado real como Java o C++.
# Usa convenciones de nombres:
#
#   atributo         → público    (accesible desde cualquier lugar)
#   _atributo        → protegido  (convención: no acceder desde fuera)
#   __atributo       → privado    (name mangling — difícil de acceder)


# ─────────────────────────────────────────
#  Atributo público
# ─────────────────────────────────────────
class Persona:
    def __init__(self, nombre):
        self.nombre = nombre   # público

p = Persona("Ana")
print(p.nombre)       # Ana
p.nombre = "Luis"     # se puede modificar directamente
print(p.nombre)       # Luis


# ─────────────────────────────────────────
#  Atributo protegido (_)
# ─────────────────────────────────────────
# Un guión bajo indica "no deberías acceder desde fuera".
# Es solo una convención — Python no lo bloquea.

class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self._saldo = saldo    # protegido

    def ver_saldo(self):
        return self._saldo

cuenta = CuentaBancaria("Ana", 1000)
print(cuenta.ver_saldo())   # 1000
print(cuenta._saldo)        # funciona, pero no se recomienda


# ─────────────────────────────────────────
#  Atributo privado (__)
# ─────────────────────────────────────────
# Dos guiones bajos activan name mangling.
# Python renombra el atributo internamente.

class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo   # privado

    def ver_saldo(self):
        return self.__saldo

    def depositar(self, monto):
        if monto > 0:
            self.__saldo += monto

    def retirar(self, monto):
        if 0 < monto <= self.__saldo:
            self.__saldo -= monto
        else:
            print("Operación no válida.")

cuenta = CuentaBancaria("Ana", 1000)
print(cuenta.ver_saldo())    # 1000
# print(cuenta.__saldo)      # ❌ AttributeError
cuenta.depositar(500)
cuenta.retirar(200)
print(cuenta.ver_saldo())    # 1300


# ─────────────────────────────────────────
#  Getters y Setters
# ─────────────────────────────────────────
# Métodos para leer y modificar atributos privados con control.

class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        if isinstance(nombre, str) and len(nombre) > 0:
            self.__nombre = nombre
        else:
            print("Nombre no válido.")

    def get_edad(self):
        return self.__edad

    def set_edad(self, edad):
        if isinstance(edad, int) and 0 < edad < 120:
            self.__edad = edad
        else:
            print("Edad no válida.")

p = Persona("Ana", 20)
print(p.get_nombre())   # Ana
p.set_nombre("Luis")
p.set_edad(200)         # Edad no válida.
print(p.get_nombre())   # Luis


# ─────────────────────────────────────────
#  @property — la forma pythónica
# ─────────────────────────────────────────
# Permite acceder a métodos como si fueran atributos.

class Temperatura:
    def __init__(self, celsius):
        self.__celsius = celsius

    @property
    def celsius(self):
        return self.__celsius

    @celsius.setter
    def celsius(self, valor):
        if valor >= -273.15:
            self.__celsius = valor
        else:
            print("Temperatura por debajo del cero absoluto.")

    @property
    def fahrenheit(self):
        return self.__celsius * 9/5 + 32


t = Temperatura(25)
print(t.celsius)      # 25    → como atributo, no t.celsius()
print(t.fahrenheit)   # 77.0
t.celsius = 100
print(t.fahrenheit)   # 212.0
t.celsius = -300      # Temperatura por debajo del cero absoluto.


# ─────────────────────────────────────────
#  Resumen rápido
# ─────────────────────────────────────────
#   atributo    → público, accesible desde fuera
#   _atributo   → protegido (convención, no bloqueado)
#   __atributo  → privado (name mangling)
#   get_x()     → getter: leer atributo privado
#   set_x(v)    → setter: modificar con validación
#   @property   → acceder a método como atributo
#   @x.setter   → setter con @property
