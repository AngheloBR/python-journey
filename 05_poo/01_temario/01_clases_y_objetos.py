# ══════════════════════════════════════════════════════════════
#  Python Journey — by AngheloBR
#  Módulo 05: POO
#  Tema 01: Clases y objetos
# ══════════════════════════════════════════════════════════════


# ─────────────────────────────────────────
#  ¿Qué es la POO?
# ─────────────────────────────────────────
# La Programación Orientada a Objetos organiza el código
# en clases — plantillas que definen atributos y comportamientos.
# Un objeto es una instancia de una clase.
#
# Analogía:
#   Clase  → plano de una casa
#   Objeto → la casa construida con ese plano


# ─────────────────────────────────────────
#  Definir una clase
# ─────────────────────────────────────────
class Persona:
    pass   # clase vacía por ahora

# Crear objetos (instancias)
p1 = Persona()
p2 = Persona()

print(type(p1))   # <class '__main__.Persona'>


# ─────────────────────────────────────────
#  __init__ — el constructor
# ─────────────────────────────────────────
# Se ejecuta automáticamente al crear un objeto.
# Define los atributos iniciales.

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre   # atributo de instancia
        self.edad = edad

p1 = Persona("Ana", 20)
p2 = Persona("Luis", 25)

print(p1.nombre)   # Ana
print(p2.edad)     # 25


# ─────────────────────────────────────────
#  Métodos — funciones de la clase
# ─────────────────────────────────────────
# Los métodos reciben self como primer parámetro.
# self hace referencia al objeto que llama el método.

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años.")

    def es_mayor_de_edad(self):
        return self.edad >= 18

p = Persona("Ana", 20)
p.saludar()                      # Hola, soy Ana y tengo 20 años.
print(p.es_mayor_de_edad())      # True


# ─────────────────────────────────────────
#  Modificar atributos
# ─────────────────────────────────────────
p = Persona("Luis", 17)
print(p.edad)    # 17

p.edad = 18
print(p.edad)    # 18

p.saludar()      # Hola, soy Luis y tengo 18 años.


# ─────────────────────────────────────────
#  __str__ — representación en texto
# ─────────────────────────────────────────
# Define qué se muestra cuando haces print(objeto).

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f"Persona({self.nombre}, {self.edad})"

p = Persona("Ana", 20)
print(p)   # Persona(Ana, 20)


# ─────────────────────────────────────────
#  Atributos de clase
# ─────────────────────────────────────────
# Compartidos por todas las instancias de la clase.

class Contador:
    total = 0   # atributo de clase

    def __init__(self, nombre):
        self.nombre = nombre
        Contador.total += 1

c1 = Contador("uno")
c2 = Contador("dos")
c3 = Contador("tres")

print(Contador.total)   # 3


# ─────────────────────────────────────────
#  Ejemplo completo
# ─────────────────────────────────────────
class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def esta_disponible(self):
        return self.stock > 0

    def vender(self, cantidad):
        if cantidad <= self.stock:
            self.stock -= cantidad
            print(f"Vendidos {cantidad} unidades de {self.nombre}.")
        else:
            print("Stock insuficiente.")

    def __str__(self):
        return f"{self.nombre} — S/. {self.precio} | Stock: {self.stock}"


laptop = Producto("Laptop", 2500, 5)
print(laptop)                  # Laptop — S/. 2500 | Stock: 5
print(laptop.esta_disponible()) # True
laptop.vender(2)               # Vendidos 2 unidades de Laptop.
print(laptop)                  # Laptop — S/. 2500 | Stock: 3


# ─────────────────────────────────────────
#  Resumen rápido
# ─────────────────────────────────────────
#   class Nombre:           → define una clase
#   def __init__(self, ...) → constructor
#   self.atributo = valor   → atributo de instancia
#   def metodo(self):       → método
#   def __str__(self):      → representación en texto
#   Clase.atributo          → atributo de clase
#   objeto = Clase(args)    → crear instancia
