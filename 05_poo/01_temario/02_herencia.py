# ══════════════════════════════════════════════════════════════
#  Python Journey — by AngheloBR
#  Módulo 05: POO
#  Tema 02: Herencia
# ══════════════════════════════════════════════════════════════


# ─────────────────────────────────────────
#  ¿Qué es la herencia?
# ─────────────────────────────────────────
# La herencia permite crear una clase nueva basada en otra.
# La clase hija hereda atributos y métodos de la clase padre.
# Evita repetir código y permite extender funcionalidad.
#
# Analogía:
#   Padre → Animal (tiene nombre, puede comer)
#   Hijo  → Perro  (todo lo de Animal + puede ladrar)


# ─────────────────────────────────────────
#  Sintaxis básica
# ─────────────────────────────────────────
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def comer(self):
        print(f"{self.nombre} está comiendo.")

    def __str__(self):
        return f"Animal: {self.nombre}"


class Perro(Animal):   # Perro hereda de Animal
    def ladrar(self):
        print(f"{self.nombre} dice: ¡Guau!")


p = Perro("Rex")
p.comer()    # heredado de Animal → Rex está comiendo.
p.ladrar()   # propio de Perro   → Rex dice: ¡Guau!
print(p)     # Animal: Rex


# ─────────────────────────────────────────
#  super() — llamar al constructor del padre
# ─────────────────────────────────────────
# Cuando la clase hija tiene su propio __init__,
# usa super() para no perder los atributos del padre.

class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def info(self):
        print(f"{self.nombre}, {self.edad} años.")


class Gato(Animal):
    def __init__(self, nombre, edad, color):
        super().__init__(nombre, edad)   # llama al __init__ del padre
        self.color = color               # atributo propio

    def maullar(self):
        print(f"{self.nombre} dice: ¡Miau!")

    def info(self):
        super().info()   # llama al método del padre
        print(f"Color: {self.color}")


g = Gato("Luna", 3, "negro")
g.info()
g.maullar()


# ─────────────────────────────────────────
#  Sobreescribir métodos (override)
# ─────────────────────────────────────────
# La clase hija puede redefinir métodos del padre.

class Figura:
    def area(self):
        return 0

    def describir(self):
        print(f"Soy una figura con área {self.area()}")


class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def area(self):   # sobreescribe el método del padre
        return 3.14159 * self.radio ** 2


class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado

    def area(self):   # sobreescribe el método del padre
        return self.lado ** 2


c = Circulo(5)
q = Cuadrado(4)

c.describir()   # Soy una figura con área 78.53...
q.describir()   # Soy una figura con área 16


# ─────────────────────────────────────────
#  isinstance() — verificar herencia
# ─────────────────────────────────────────
print(isinstance(c, Circulo))   # True
print(isinstance(c, Figura))    # True — Circulo hereda de Figura
print(isinstance(c, Cuadrado))  # False


# ─────────────────────────────────────────
#  Herencia múltiple
# ─────────────────────────────────────────
# Python permite heredar de más de una clase.
# Úsala con cuidado — puede volverse compleja.

class Volador:
    def volar(self):
        print("Estoy volando.")

class Nadador:
    def nadar(self):
        print("Estoy nadando.")

class Pato(Volador, Nadador):
    def __init__(self, nombre):
        self.nombre = nombre

donald = Pato("Donald")
donald.volar()   # Estoy volando.
donald.nadar()   # Estoy nadando.


# ─────────────────────────────────────────
#  Resumen rápido
# ─────────────────────────────────────────
#   class Hijo(Padre):         → herencia simple
#   super().__init__(args)     → llamar constructor del padre
#   super().metodo()           → llamar método del padre
#   def metodo(self): ...      → sobreescribir método del padre
#   isinstance(obj, Clase)     → verificar si es instancia
#   class Hijo(Padre1, Padre2) → herencia múltiple
