# ══════════════════════════════════════════════════════════════
#  Python Journey — by AngheloBR
#  Módulo 05: POO
#  Soluciones 04: Encapsulamiento
# ══════════════════════════════════════════════════════════════
#
#  ⚠️  Intenta resolver los ejercicios por tu cuenta primero.
#  Solo revisa esto si ya lo intentaste y no pudiste.
# ══════════════════════════════════════════════════════════════


# ─────────────────────────────────────────
#  Ejercicio 1
# ─────────────────────────────────────────
class Usuario:
    def __init__(self, nombre, password):
        self.__nombre = nombre
        self.__password = password

    def get_nombre(self):
        return self.__nombre

    def set_password(self, pwd):
        if len(pwd) >= 8:
            self.__password = pwd
            print("Contraseña actualizada.")
        else:
            print("La contraseña debe tener al menos 8 caracteres.")

    def verificar_password(self, pwd):
        return self.__password == pwd


u = Usuario("Ana", "secreta123")
print(u.get_nombre())              # Ana
print(u.verificar_password("mal")) # False
print(u.verificar_password("secreta123"))  # True
u.set_password("corta")            # error
u.set_password("nuevaclave99")     # actualizada


# ─────────────────────────────────────────
#  Ejercicio 2
# ─────────────────────────────────────────
class Producto:
    def __init__(self, nombre, precio, stock):
        self.__nombre = nombre
        self.__precio = precio
        self.__stock = stock

    @property
    def nombre(self):
        return self.__nombre

    @property
    def precio(self):
        return self.__precio

    @precio.setter
    def precio(self, valor):
        if valor > 0:
            self.__precio = valor
        else:
            print("El precio debe ser positivo.")

    @property
    def stock(self):
        return self.__stock

    @stock.setter
    def stock(self, valor):
        if valor >= 0:
            self.__stock = valor
        else:
            print("El stock no puede ser negativo.")


p = Producto("Laptop", 2500, 10)
print(p.nombre)    # Laptop
print(p.precio)    # 2500
p.precio = -100    # error
p.stock = 5
print(p.stock)     # 5


# ─────────────────────────────────────────
#  Ejercicio 3
# ─────────────────────────────────────────
class CajaFuerte:
    def __init__(self, clave):
        self.__clave = clave
        self.__contenido = []

    def guardar(self, item, clave):
        if clave == self.__clave:
            self.__contenido.append(item)
            print(f"'{item}' guardado.")
        else:
            print("Acceso denegado.")

    def abrir(self, clave):
        if clave == self.__clave:
            print(f"Contenido: {self.__contenido}")
        else:
            print("Acceso denegado.")


caja = CajaFuerte("1234")
caja.guardar("documento", "1234")
caja.guardar("dinero", "0000")    # denegado
caja.abrir("1234")
caja.abrir("5678")                # denegado


# ─────────────────────────────────────────
#  Ejercicio 4
# ─────────────────────────────────────────
class Circulo:
    def __init__(self, radio):
        self.__radio = radio

    @property
    def radio(self):
        return self.__radio

    @radio.setter
    def radio(self, valor):
        if valor > 0:
            self.__radio = valor
        else:
            print("El radio debe ser positivo.")

    @property
    def area(self):
        return 3.14159 * self.__radio ** 2

    @property
    def diametro(self):
        return self.__radio * 2


c = Circulo(5)
print(f"Radio   : {c.radio}")
print(f"Área    : {c.area:.2f}")
print(f"Diámetro: {c.diametro}")

c.radio = 10
print(f"\nRadio   : {c.radio}")
print(f"Área    : {c.area:.2f}")
print(f"Diámetro: {c.diametro}")
