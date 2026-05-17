# ══════════════════════════════════════════════════════════════
#  Python Journey — by AngheloBR
#  Módulo 05: POO
#  Soluciones 02: Herencia
# ══════════════════════════════════════════════════════════════
#
#  ⚠️  Intenta resolver los ejercicios por tu cuenta primero.
#  Solo revisa esto si ya lo intentaste y no pudiste.
# ══════════════════════════════════════════════════════════════


# ─────────────────────────────────────────
#  Ejercicio 1
# ─────────────────────────────────────────
class Vehiculo:
    def __init__(self, marca, velocidad_max):
        self.marca = marca
        self.velocidad_max = velocidad_max

    def moverse(self):
        print(f"El {self.marca} se está moviendo.")

    def info(self):
        print(f"{self.marca} — Velocidad máx: {self.velocidad_max} km/h")


class Moto(Vehiculo):
    def __init__(self, marca, velocidad_max, tipo):
        super().__init__(marca, velocidad_max)
        self.tipo = tipo

    def wheelie(self):
        print(f"¡La {self.marca} hace un wheelie!")


moto = Moto("Yamaha", 200, "deportiva")
moto.info()
moto.moverse()
moto.wheelie()


# ─────────────────────────────────────────
#  Ejercicio 2
# ─────────────────────────────────────────
class Empleado:
    def __init__(self, nombre, salario_base):
        self.nombre = nombre
        self.salario_base = salario_base

    def calcular_pago(self):
        return self.salario_base

    def __str__(self):
        return f"{self.nombre} — Pago: S/. {self.calcular_pago()}"


class Gerente(Empleado):
    def __init__(self, nombre, salario_base, bono):
        super().__init__(nombre, salario_base)
        self.bono = bono

    def calcular_pago(self):
        return self.salario_base + self.bono


emp = Empleado("Luis", 2000)
ger = Gerente("Ana", 3000, 1500)

print(emp)   # Luis — Pago: S/. 2000
print(ger)   # Ana  — Pago: S/. 4500


# ─────────────────────────────────────────
#  Ejercicio 3
# ─────────────────────────────────────────
class Figura:
    def area(self):
        return 0

    def perimetro(self):
        return 0

    def describir(self):
        print(f"Área: {self.area():.2f} | Perímetro: {self.perimetro():.2f}")


class Rectangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2 * (self.base + self.altura)


class Triangulo(Figura):
    def __init__(self, base, altura, lado1, lado2, lado3):
        self.base = base
        self.altura = altura
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def area(self):
        return (self.base * self.altura) / 2

    def perimetro(self):
        return self.lado1 + self.lado2 + self.lado3


class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return 3.14159 * self.radio ** 2

    def perimetro(self):
        return 2 * 3.14159 * self.radio


Rectangulo(5, 3).describir()
Triangulo(4, 3, 3, 4, 5).describir()
Circulo(7).describir()


# ─────────────────────────────────────────
#  Ejercicio 4
# ─────────────────────────────────────────
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad


class Estudiante(Persona):
    def __init__(self, nombre, edad, carrera):
        super().__init__(nombre, edad)
        self.carrera = carrera

    def estudiar(self):
        print(f"{self.nombre} está estudiando {self.carrera}.")


class Profesor(Persona):
    def __init__(self, nombre, edad, materia):
        super().__init__(nombre, edad)
        self.materia = materia

    def enseñar(self):
        print(f"{self.nombre} está enseñando {self.materia}.")


alumno = Estudiante("Ana", 20, "Ingeniería")
profe  = Profesor("Luis", 40, "Matemáticas")

alumno.estudiar()
profe.enseñar()

print(isinstance(alumno, Estudiante))  # True
print(isinstance(alumno, Persona))     # True
print(isinstance(profe, Profesor))     # True
print(isinstance(profe, Persona))      # True
print(isinstance(alumno, Profesor))    # False
