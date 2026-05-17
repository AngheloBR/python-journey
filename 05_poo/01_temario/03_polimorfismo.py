# ══════════════════════════════════════════════════════════════
#  Python Journey — by AngheloBR
#  Módulo 05: POO
#  Tema 03: Polimorfismo
# ══════════════════════════════════════════════════════════════


# ─────────────────────────────────────────
#  ¿Qué es el polimorfismo?
# ─────────────────────────────────────────
# Polimorfismo significa "muchas formas".
# En POO: distintos objetos pueden responder al mismo método
# de formas diferentes.
#
# Analogía:
#   El método "hablar()" en Perro → "¡Guau!"
#   El método "hablar()" en Gato  → "¡Miau!"
#   El método "hablar()" en Pato  → "¡Cuac!"
#   Mismo nombre, comportamiento distinto.


# ─────────────────────────────────────────
#  Polimorfismo con herencia
# ─────────────────────────────────────────
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        pass


class Perro(Animal):
    def hablar(self):
        print(f"{self.nombre} dice: ¡Guau!")


class Gato(Animal):
    def hablar(self):
        print(f"{self.nombre} dice: ¡Miau!")


class Pato(Animal):
    def hablar(self):
        print(f"{self.nombre} dice: ¡Cuac!")


# La magia del polimorfismo — mismo código, distinto resultado
animales = [Perro("Rex"), Gato("Luna"), Pato("Donald")]

for animal in animales:
    animal.hablar()

# Rex dice: ¡Guau!
# Luna dice: ¡Miau!
# Donald dice: ¡Cuac!


# ─────────────────────────────────────────
#  Polimorfismo con funciones
# ─────────────────────────────────────────
# Una función puede recibir distintos tipos de objetos
# siempre que tengan el método esperado.

def hacer_hablar(animal):
    animal.hablar()

hacer_hablar(Perro("Rex"))    # Rex dice: ¡Guau!
hacer_hablar(Gato("Luna"))    # Luna dice: ¡Miau!


# ─────────────────────────────────────────
#  Polimorfismo sin herencia — duck typing
# ─────────────────────────────────────────
# En Python no necesitas heredar de una clase base.
# Si el objeto tiene el método, funciona.
# "Si camina como pato y suena como pato, es un pato."

class Robot:
    def hablar(self):
        print("Beep boop, soy un robot.")

class Humano:
    def hablar(self):
        print("Hola, soy un humano.")

for ser in [Robot(), Humano(), Perro("Max")]:
    ser.hablar()


# ─────────────────────────────────────────
#  Sobrecarga de operadores
# ─────────────────────────────────────────
# Python permite redefinir cómo se comportan los operadores
# (+, -, *, ==, etc.) con tus propias clases.

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, otro):       # define el operador +
        return Vector(self.x + otro.x, self.y + otro.y)

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __eq__(self, otro):        # define el operador ==
        return self.x == otro.x and self.y == otro.y


v1 = Vector(1, 2)
v2 = Vector(3, 4)
v3 = v1 + v2

print(v3)           # (4, 6)
print(v1 == v2)     # False
print(v1 == Vector(1, 2))  # True


# ─────────────────────────────────────────
#  Resumen rápido
# ─────────────────────────────────────────
#   Polimorfismo → mismo método, distinto comportamiento
#   Override     → clase hija redefine método del padre
#   Duck typing  → si tiene el método, funciona (sin herencia)
#   __add__      → sobrecarga del operador +
#   __eq__       → sobrecarga del operador ==
#   __str__      → sobrecarga de print()
