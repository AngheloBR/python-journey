# ══════════════════════════════════════════════════════════════
#  Python Journey — by AngheloBR
#  Módulo 05: POO
#  Soluciones 03: Polimorfismo
# ══════════════════════════════════════════════════════════════
#
#  ⚠️  Intenta resolver los ejercicios por tu cuenta primero.
#  Solo revisa esto si ya lo intentaste y no pudiste.
# ══════════════════════════════════════════════════════════════


# ─────────────────────────────────────────
#  Ejercicio 1
# ─────────────────────────────────────────
class Instrumento:
    def tocar(self):
        pass

class Guitarra(Instrumento):
    def tocar(self):
        print("Guitarra: ¡Rasgueo!")

class Piano(Instrumento):
    def tocar(self):
        print("Piano: ♪ Do Re Mi ♪")

class Bateria(Instrumento):
    def tocar(self):
        print("Batería: ¡Boom tss boom tss!")

instrumentos = [Guitarra(), Piano(), Bateria()]

for instrumento in instrumentos:
    instrumento.tocar()


# ─────────────────────────────────────────
#  Ejercicio 2
# ─────────────────────────────────────────
def procesar_pago(metodo):
    metodo.pagar()

class Efectivo:
    def pagar(self):
        print("Pagando en efectivo.")

class Tarjeta:
    def pagar(self):
        print("Pagando con tarjeta.")

class Transferencia:
    def pagar(self):
        print("Pagando por transferencia bancaria.")

procesar_pago(Efectivo())
procesar_pago(Tarjeta())
procesar_pago(Transferencia())


# ─────────────────────────────────────────
#  Ejercicio 3
# ─────────────────────────────────────────
class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, otro):
        return Punto(self.x + otro.x, self.y + otro.y)

    def __sub__(self, otro):
        return Punto(self.x - otro.x, self.y - otro.y)

    def __eq__(self, otro):
        return self.x == otro.x and self.y == otro.y

    def __str__(self):
        return f"({self.x}, {self.y})"

p1 = Punto(2, 3)
p2 = Punto(1, 4)

print(p1 + p2)          # (3, 7)
print(p1 - p2)          # (1, -1)
print(p1 == p2)         # False
print(p1 == Punto(2, 3))  # True


# ─────────────────────────────────────────
#  Ejercicio 4
# ─────────────────────────────────────────
class Perro:
    def sonido(self):
        print("¡Guau!")

class Gato:
    def sonido(self):
        print("¡Miau!")

class Vaca:
    def sonido(self):
        print("¡Muuu!")

def escuchar(animal):
    animal.sonido()

escuchar(Perro())
escuchar(Gato())
escuchar(Vaca())
