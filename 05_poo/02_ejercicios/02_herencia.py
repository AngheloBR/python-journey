# ══════════════════════════════════════════════════════════════
#  Python Journey — by AngheloBR
#  Módulo 05: POO
#  Ejercicios 02: Herencia
# ══════════════════════════════════════════════════════════════
#
#  Lee cada enunciado, escribe tu solución debajo.
#  Si no puedes, revisa el temario primero.
#  Si aún no puedes, revisa soluciones/02_herencia.py
# ══════════════════════════════════════════════════════════════


# ─────────────────────────────────────────
#  Ejercicio 1
# ─────────────────────────────────────────
# Crea una clase "Vehiculo" con:
#   - atributos: marca, velocidad_max
#   - método moverse(): imprime "El {marca} se está moviendo."
#   - método info(): imprime marca y velocidad máxima
#
# Crea una clase "Moto" que herede de Vehiculo y agregue:
#   - atributo: tipo (deportiva, clásica, etc.)
#   - método wheelie(): imprime "¡La {marca} hace un wheelie!"
#
# Crea una instancia y prueba todos los métodos.

# TU CÓDIGO AQUÍ ↓


# ─────────────────────────────────────────
#  Ejercicio 2
# ─────────────────────────────────────────
# Crea una clase "Empleado" con:
#   - atributos: nombre, salario_base
#   - método calcular_pago(): retorna salario_base
#   - __str__: nombre y pago
#
# Crea una clase "Gerente" que herede de Empleado y:
#   - agregue atributo: bono
#   - sobreescriba calcular_pago(): retorna salario_base + bono
#
# Crea un empleado y un gerente, imprime su pago.

# TU CÓDIGO AQUÍ ↓


# ─────────────────────────────────────────
#  Ejercicio 3
# ─────────────────────────────────────────
# Crea una clase base "Figura" con:
#   - método area(): retorna 0
#   - método perimetro(): retorna 0
#   - método describir(): imprime área y perímetro
#
# Crea tres clases hijas: Rectangulo, Triangulo, Circulo
# Cada una sobreescribe area() y perimetro() con su fórmula.
# Crea una instancia de cada una y llama describir().

# TU CÓDIGO AQUÍ ↓


# ─────────────────────────────────────────
#  Ejercicio 4
# ─────────────────────────────────────────
# Crea una clase "Persona" con nombre y edad.
# Crea una clase "Estudiante" que herede de Persona y agregue:
#   - atributo: carrera
#   - método estudiar(): imprime "{nombre} está estudiando {carrera}."
#
# Crea una clase "Profesor" que herede de Persona y agregue:
#   - atributo: materia
#   - método enseñar(): imprime "{nombre} está enseñando {materia}."
#
# Verifica con isinstance() que:
#   - el estudiante es instancia de Estudiante y de Persona
#   - el profesor es instancia de Profesor y de Persona
#   - el estudiante NO es instancia de Profesor

# TU CÓDIGO AQUÍ ↓
