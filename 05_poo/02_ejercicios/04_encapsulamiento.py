# ══════════════════════════════════════════════════════════════
#  Python Journey — by AngheloBR
#  Módulo 05: POO
#  Ejercicios 04: Encapsulamiento
# ══════════════════════════════════════════════════════════════
#
#  Lee cada enunciado, escribe tu solución debajo.
#  Si no puedes, revisa el temario primero.
#  Si aún no puedes, revisa soluciones/04_encapsulamiento.py
# ══════════════════════════════════════════════════════════════


# ─────────────────────────────────────────
#  Ejercicio 1
# ─────────────────────────────────────────
# Crea una clase "Usuario" con atributos privados:
#   __nombre y __password
# Agrega:
#   - getter para nombre (sin getter para password)
#   - setter para password que verifique que tenga al menos 8 caracteres
#   - método verificar_password(pwd) que retorne True/False

# TU CÓDIGO AQUÍ ↓


# ─────────────────────────────────────────
#  Ejercicio 2
# ─────────────────────────────────────────
# Crea una clase "Producto" con:
#   - __nombre (privado)
#   - __precio (privado)
#   - __stock  (privado)
# Usa @property para acceder a los tres como atributos.
# Usa @precio.setter que valide que el precio sea positivo.
# Usa @stock.setter que valide que el stock no sea negativo.

# TU CÓDIGO AQUÍ ↓


# ─────────────────────────────────────────
#  Ejercicio 3
# ─────────────────────────────────────────
# Crea una clase "CajaFuerte" con:
#   - __contenido (lista privada, vacía por defecto)
#   - __clave (privada)
#   - método guardar(item, clave): agrega item si la clave es correcta
#   - método abrir(clave): muestra el contenido si la clave es correcta
#   - si la clave es incorrecta imprime "Acceso denegado."

# TU CÓDIGO AQUÍ ↓


# ─────────────────────────────────────────
#  Ejercicio 4
# ─────────────────────────────────────────
# Crea una clase "Circulo" con:
#   - __radio privado
#   - @property radio que retorne el radio
#   - @radio.setter que valide que sea positivo
#   - @property area que calcule el área (solo lectura)
#   - @property diametro que calcule el diámetro (solo lectura)
# Prueba cambiar el radio y observa cómo cambian área y diámetro.

# TU CÓDIGO AQUÍ ↓
