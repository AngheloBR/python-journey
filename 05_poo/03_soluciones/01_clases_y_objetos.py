# ══════════════════════════════════════════════════════════════
#  Python Journey — by AngheloBR
#  Módulo 05: POO
#  Soluciones 01: Clases y objetos
# ══════════════════════════════════════════════════════════════
#
#  ⚠️  Intenta resolver los ejercicios por tu cuenta primero.
#  Solo revisa esto si ya lo intentaste y no pudiste.
# ══════════════════════════════════════════════════════════════


# ─────────────────────────────────────────
#  Ejercicio 1
# ─────────────────────────────────────────
class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2 * (self.base + self.altura)

r1 = Rectangulo(5, 3)
r2 = Rectangulo(10, 4)

print(f"Área r1: {r1.area()}, Perímetro r1: {r1.perimetro()}")
print(f"Área r2: {r2.area()}, Perímetro r2: {r2.perimetro()}")


# ─────────────────────────────────────────
#  Ejercicio 2
# ─────────────────────────────────────────
class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre
        self.notas = []

    def agregar_nota(self, nota):
        self.notas.append(nota)

    def promedio(self):
        if not self.notas:
            return 0
        return sum(self.notas) / len(self.notas)

    def aprobo(self):
        return self.promedio() >= 13

    def __str__(self):
        return f"{self.nombre} — Promedio: {self.promedio():.2f}"

e = Estudiante("Ana")
e.agregar_nota(15)
e.agregar_nota(18)
e.agregar_nota(12)
print(e)
print(f"¿Aprobó? {e.aprobo()}")


# ─────────────────────────────────────────
#  Ejercicio 3
# ─────────────────────────────────────────
class CuentaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, monto):
        self.saldo += monto
        print(f"Depósito de S/. {monto}. Nuevo saldo: S/. {self.saldo}")

    def retirar(self, monto):
        if monto <= self.saldo:
            self.saldo -= monto
            print(f"Retiro de S/. {monto}. Nuevo saldo: S/. {self.saldo}")
        else:
            print("Saldo insuficiente.")

    def ver_saldo(self):
        print(f"Saldo actual: S/. {self.saldo}")

    def __str__(self):
        return f"Cuenta de {self.titular} — S/. {self.saldo}"

cuenta = CuentaBancaria("Ana")
cuenta.depositar(500)
cuenta.retirar(200)
cuenta.retirar(400)
print(cuenta)


# ─────────────────────────────────────────
#  Ejercicio 4
# ─────────────────────────────────────────
class Auto:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.encendido = False

    def encender(self):
        self.encendido = True
        print(f"{self.marca} {self.modelo} encendido.")

    def apagar(self):
        self.encendido = False
        print(f"{self.marca} {self.modelo} apagado.")

    def info(self):
        estado = "Encendido" if self.encendido else "Apagado"
        print(f"{self.marca} {self.modelo} ({self.año}) — {estado}")

auto = Auto("Toyota", "Corolla", 2020)
auto.encender()
auto.info()
auto.apagar()


# ─────────────────────────────────────────
#  Ejercicio 5
# ─────────────────────────────────────────
class Calculadora:
    def __init__(self):
        self.historial = []

    def sumar(self, a, b):
        resultado = a + b
        self.historial.append(f"{a} + {b} = {resultado}")
        return resultado

    def restar(self, a, b):
        resultado = a - b
        self.historial.append(f"{a} - {b} = {resultado}")
        return resultado

    def multiplicar(self, a, b):
        resultado = a * b
        self.historial.append(f"{a} * {b} = {resultado}")
        return resultado

    def dividir(self, a, b):
        if b == 0:
            print("No se puede dividir entre 0.")
            return None
        resultado = a / b
        self.historial.append(f"{a} / {b} = {resultado}")
        return resultado

    def ver_historial(self):
        for operacion in self.historial:
            print(operacion)

calc = Calculadora()
calc.sumar(10, 5)
calc.restar(20, 8)
calc.multiplicar(4, 6)
calc.dividir(15, 3)
calc.ver_historial()
