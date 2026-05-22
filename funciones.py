import matplotlib.pyplot as plt
import numpy as np

# 1. VALORES Y FÓRMULAS DEL MODELO
# Plan Lineal (Compañero): L(x) = 20x + 100
def plan_lineal(x):
    return 20 * x + 100

# Plan Cuadrático (Tu parte): C(x) = -2x^2 + 80x + 100
def plan_cuadratico(x):
    return -2 * (x**2) + 80 * x + 100

# Rango de tiempo para el eje X (de 0 a 45 horas)
horas = np.linspace(0, 45, 400)

# 2. CÁLCULO DE COSTOS (EJE Y)
costos_lineal = plan_lineal(horas)
costos_cuadratico = plan_cuadratico(horas)

# 3. ARMADO DE LA GRÁFICA
plt.figure(figsize=(10, 6))

# Dibujo de las curvas
plt.plot(horas, costos_lineal, label="Plan Lineal: $L(x) = 20x + 100$", color="#2b6cb0", linewidth=2.5)
plt.plot(horas, costos_cuadratico, label="Plan Cuadrático: $C(x) = -2x^2 + 80x + 100$", color="#e53e3e", linewidth=2.5)

# Puntos clave del análisis matemático
plt.scatter(0, 100, color="#2b364a", s=90, zorder=5, label="Ordenada al origen (0, 100)")
plt.scatter(20, 900, color="#2f855a", s=100, marker="^", zorder=5, label="Vértice Máximo (20, 900)")
plt.scatter(30, 700, color="#d69e2e", s=90, marker="o", zorder=5, label="Intersección (30, 700)")

# Líneas guía para el vértice
plt.axvline(x=20, color="#718096", linestyle="--", alpha=0.5)
plt.axhline(y=900, color="#718096", linestyle="--", alpha=0.5)

# Títulos y formato de pantalla
plt.title("Comparativa de Modelos: Plan Lineal vs. Plan Cuadrático", fontsize=12, fontweight="bold")
plt.xlabel("Horas Contratadas (X)")
plt.ylabel("Costo Total en Pesos (Y)")
plt.xlim(-2, 45)
plt.ylim(0, 1000)
plt.grid(True, linestyle=":", alpha=0.6)
plt.legend(loc="upper right")

# Ejecutar gráfico
plt.show()