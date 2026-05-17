# ══════════════════════════════════════════════════════════════
#  Python Journey — by AngheloBR
#  Módulo 10: Proyecto Final
#  Sistema de Gestión de Estudiantes
# ══════════════════════════════════════════════════════════════
#
#  Este proyecto aplica todo lo aprendido en el curso:
#   ✓ Variables y tipos de datos     (módulo 01)
#   ✓ Control de flujo               (módulo 02)
#   ✓ Funciones                      (módulo 03)
#   ✓ Listas y diccionarios          (módulo 04)
#   ✓ Clases y POO                   (módulo 05)
#   ✓ Archivos JSON                  (módulo 06)
#   ✓ Manejo de excepciones          (módulo 07)
#   ✓ Módulos                        (módulo 08)
#   ✓ Comprehensions                 (módulo 09)
# ══════════════════════════════════════════════════════════════

import json
import os
from datetime import datetime


# ─────────────────────────────────────────
#  Clase Estudiante
# ─────────────────────────────────────────
class Estudiante:
    def __init__(self, nombre: str, carrera: str, notas: list = None):
        self.nombre = nombre
        self.carrera = carrera
        self.notas = notas if notas else []
        self.fecha_registro = datetime.now().strftime("%Y-%m-%d")

    def agregar_nota(self, nota: float):
        if not 0 <= nota <= 20:
            raise ValueError("La nota debe estar entre 0 y 20.")
        self.notas.append(nota)

    def promedio(self) -> float:
        if not self.notas:
            return 0.0
        return sum(self.notas) / len(self.notas)

    def aprobo(self) -> bool:
        return self.promedio() >= 13

    def to_dict(self) -> dict:
        return {
            "nombre": self.nombre,
            "carrera": self.carrera,
            "notas": self.notas,
            "fecha_registro": self.fecha_registro
        }

    @classmethod
    def from_dict(cls, data: dict):
        e = cls(data["nombre"], data["carrera"], data["notas"])
        e.fecha_registro = data.get("fecha_registro", "N/A")
        return e

    def __str__(self):
        estado = "✓ Aprobado" if self.aprobo() else "✗ Reprobado"
        return f"{self.nombre:<20} | {self.carrera:<20} | Promedio: {self.promedio():.2f} | {estado}"


# ─────────────────────────────────────────
#  Clase GestorEstudiantes
# ─────────────────────────────────────────
class GestorEstudiantes:
    ARCHIVO = "estudiantes.json"

    def __init__(self):
        self.estudiantes: list[Estudiante] = []
        self.cargar()

    def cargar(self):
        try:
            with open(self.ARCHIVO, "r", encoding="utf-8") as f:
                datos = json.load(f)
                self.estudiantes = [Estudiante.from_dict(d) for d in datos]
        except FileNotFoundError:
            self.estudiantes = []

    def guardar(self):
        with open(self.ARCHIVO, "w", encoding="utf-8") as f:
            json.dump([e.to_dict() for e in self.estudiantes], f, indent=4, ensure_ascii=False)

    def agregar_estudiante(self, nombre: str, carrera: str) -> Estudiante:
        if self.buscar(nombre):
            raise ValueError(f"Ya existe un estudiante con el nombre '{nombre}'.")
        e = Estudiante(nombre, carrera)
        self.estudiantes.append(e)
        self.guardar()
        return e

    def buscar(self, nombre: str):
        nombre = nombre.lower()
        return next((e for e in self.estudiantes if e.nombre.lower() == nombre), None)

    def eliminar(self, nombre: str) -> bool:
        e = self.buscar(nombre)
        if e:
            self.estudiantes.remove(e)
            self.guardar()
            return True
        return False

    def listar(self):
        return sorted(self.estudiantes, key=lambda e: e.promedio(), reverse=True)

    def aprobados(self):
        return [e for e in self.estudiantes if e.aprobo()]

    def reprobados(self):
        return [e for e in self.estudiantes if not e.aprobo()]

    def estadisticas(self) -> dict:
        if not self.estudiantes:
            return {}
        promedios = [e.promedio() for e in self.estudiantes]
        return {
            "total": len(self.estudiantes),
            "aprobados": len(self.aprobados()),
            "reprobados": len(self.reprobados()),
            "promedio_general": sum(promedios) / len(promedios),
            "mejor": max(self.estudiantes, key=lambda e: e.promedio()).nombre,
            "peor": min(self.estudiantes, key=lambda e: e.promedio()).nombre,
        }


# ─────────────────────────────────────────
#  Interfaz de consola
# ─────────────────────────────────────────
def limpiar():
    os.system("clear" if os.name == "posix" else "cls")

def separador():
    print("─" * 55)

def encabezado(titulo: str):
    limpiar()
    print("═" * 55)
    print(f"  🎓 Python Journey — Gestión de Estudiantes")
    print(f"  {titulo}")
    print("═" * 55)

def pausar():
    input("\nPresiona Enter para continuar...")


def menu_principal():
    print("\n  1. Agregar estudiante")
    print("  2. Agregar nota a estudiante")
    print("  3. Buscar estudiante")
    print("  4. Listar todos los estudiantes")
    print("  5. Ver aprobados / reprobados")
    print("  6. Estadísticas")
    print("  7. Eliminar estudiante")
    print("  0. Salir")
    separador()
    return input("  Opción: ").strip()


def accion_agregar(gestor: GestorEstudiantes):
    encabezado("Agregar estudiante")
    nombre = input("  Nombre   : ").strip()
    carrera = input("  Carrera  : ").strip()
    try:
        e = gestor.agregar_estudiante(nombre, carrera)
        print(f"\n  ✓ Estudiante '{e.nombre}' registrado correctamente.")
    except ValueError as err:
        print(f"\n  ✗ Error: {err}")
    pausar()


def accion_agregar_nota(gestor: GestorEstudiantes):
    encabezado("Agregar nota")
    nombre = input("  Nombre del estudiante: ").strip()
    e = gestor.buscar(nombre)
    if not e:
        print(f"\n  ✗ No se encontró a '{nombre}'.")
        pausar()
        return
    try:
        nota = float(input(f"  Nota para {e.nombre} (0-20): "))
        e.agregar_nota(nota)
        gestor.guardar()
        print(f"\n  ✓ Nota {nota} agregada. Promedio actual: {e.promedio():.2f}")
    except ValueError as err:
        print(f"\n  ✗ Error: {err}")
    pausar()


def accion_buscar(gestor: GestorEstudiantes):
    encabezado("Buscar estudiante")
    nombre = input("  Nombre: ").strip()
    e = gestor.buscar(nombre)
    if not e:
        print(f"\n  ✗ No se encontró a '{nombre}'.")
    else:
        separador()
        print(f"  Nombre   : {e.nombre}")
        print(f"  Carrera  : {e.carrera}")
        print(f"  Notas    : {e.notas}")
        print(f"  Promedio : {e.promedio():.2f}")
        print(f"  Estado   : {'✓ Aprobado' if e.aprobo() else '✗ Reprobado'}")
        print(f"  Registro : {e.fecha_registro}")
    pausar()


def accion_listar(gestor: GestorEstudiantes):
    encabezado("Todos los estudiantes")
    estudiantes = gestor.listar()
    if not estudiantes:
        print("  No hay estudiantes registrados.")
    else:
        separador()
        for e in estudiantes:
            print(f"  {e}")
        separador()
        print(f"  Total: {len(estudiantes)} estudiante(s)")
    pausar()


def accion_aprobados_reprobados(gestor: GestorEstudiantes):
    encabezado("Aprobados / Reprobados")
    aprobados = gestor.aprobados()
    reprobados = gestor.reprobados()

    print(f"\n  ✓ APROBADOS ({len(aprobados)})")
    separador()
    for e in aprobados:
        print(f"  {e.nombre:<20} | Promedio: {e.promedio():.2f}")

    print(f"\n  ✗ REPROBADOS ({len(reprobados)})")
    separador()
    for e in reprobados:
        print(f"  {e.nombre:<20} | Promedio: {e.promedio():.2f}")
    pausar()


def accion_estadisticas(gestor: GestorEstudiantes):
    encabezado("Estadísticas")
    stats = gestor.estadisticas()
    if not stats:
        print("  No hay datos suficientes.")
    else:
        separador()
        print(f"  Total estudiantes : {stats['total']}")
        print(f"  Aprobados         : {stats['aprobados']}")
        print(f"  Reprobados        : {stats['reprobados']}")
        print(f"  Promedio general  : {stats['promedio_general']:.2f}")
        print(f"  Mejor promedio    : {stats['mejor']}")
        print(f"  Menor promedio    : {stats['peor']}")
        separador()
    pausar()


def accion_eliminar(gestor: GestorEstudiantes):
    encabezado("Eliminar estudiante")
    nombre = input("  Nombre: ").strip()
    confirmacion = input(f"  ¿Eliminar a '{nombre}'? (s/n): ").strip().lower()
    if confirmacion == "s":
        if gestor.eliminar(nombre):
            print(f"\n  ✓ '{nombre}' eliminado correctamente.")
        else:
            print(f"\n  ✗ No se encontró a '{nombre}'.")
    else:
        print("  Operación cancelada.")
    pausar()


# ─────────────────────────────────────────
#  Main
# ─────────────────────────────────────────
def main():
    gestor = GestorEstudiantes()

    acciones = {
        "1": accion_agregar,
        "2": accion_agregar_nota,
        "3": accion_buscar,
        "4": accion_listar,
        "5": accion_aprobados_reprobados,
        "6": accion_estadisticas,
        "7": accion_eliminar,
    }

    while True:
        encabezado("Menú principal")
        opcion = menu_principal()

        if opcion == "0":
            limpiar()
            print("\n  Hasta luego. ¡Sigue aprendiendo! 🐍\n")
            break
        elif opcion in acciones:
            acciones[opcion](gestor)
        else:
            print("\n  ✗ Opción no válida.")
            pausar()


if __name__ == "__main__":
    main()
