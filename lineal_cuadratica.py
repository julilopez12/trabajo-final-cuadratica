import matplotlib.pyplot as plt
import numpy as np

# ==========================================
# 1. DEFINICIÓN DE LAS FUNCIONES
# ==========================================

# Rango de valores para X (de -10 a 10)
x = np.linspace(-10, 10, 400)

# Función Lineal: y = 2x + 3
y_lineal = 2 * x + 3

# Función Cuadrática: y = x² - 4x - 5
# (a = 1, b = -4, c = -5)
y_cuadratica = x**2 - 4 * x - 5

# ==========================================
# 2. CÁLCULOS DE LA FUNCIÓN CUADRÁTICA
# ==========================================
# Vértice (Xv = -b / 2a)
xv = -(-4) / (2 * 1)
yv = xv**2 - 4 * xv - 5

print("=== ANÁLISIS DE LA FUNCIÓN CUADRÁTICA ===")
print(f"Vértice de la parábola: V = ({xv}, {yv})")

# Raíces usando la fórmula de Bhaskara
discriminante = (-4)**2 - 4 * 1 * (-5)

if discriminante >= 0:
    x1 = (-(-4) + (discriminante)**0.5) / (2 * 1)
    x2 = (-(-4) - (discriminante)**0.5) / (2 * 1)
    print(f"Raíces (cortes con eje X): x1 = {x1}, x2 = {x2}")
else:
    print("La función no tiene raíces reales (no corta el eje X).")

print("\n" + "="*40 + "\n")

# ==========================================
# 3. CONFIGURACIÓN DE LA GRÁFICA
# ==========================================
plt.figure(figsize=(10, 6))

# Dibujar las funciones
plt.plot(x, y_lineal, label="Línea Recta: y = 2x + 3", color="blue", linewidth=2)
plt.plot(x, y_cuadratica, label="Parábola: y = x² - 4x - 5", color="red", linewidth=2)

# Marcar el vértice en el gráfico
plt.plot(xv, yv, marker='o', color='black', label=f'Vértice ({xv}, {yv})')

# Títulos y etiquetas
plt.title("Gráfico de Función Lineal y Cuadrática", fontsize=12, fontweight='bold')
plt.xlabel("Eje X", fontsize=10)
plt.ylabel("Eje Y", fontsize=10)

# Líneas de los ejes cartesianos (X=0 e Y=0)
plt.axhline(0, color='black', linestyle='-', linewidth=1)
plt.axvline(0, color='black', linestyle='-', linewidth=1)

# Cuadrícula de fondo y límites
plt.grid(True, linestyle=":", alpha=0.6)
plt.xlim(-8, 8)
plt.ylim(-10, 20)
plt.legend()

# Mostrar la ventana con el gráfico
plt.show()