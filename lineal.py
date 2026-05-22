import matplotlib.pyplot as plt
import numpy as np

# 1. FÓRMULA DE LA FUNCIÓN LINEAL (Plan Estándar)
# Pendiente m = 20 | Ordenada al origen b = 100
def plan_lineal(x):
    return 20 * x + 100

# Rango de tiempo para el eje X (de 0 a 45 horas)
horas = np.linspace(0, 45, 100)

# Cálculo de los costos (Eje Y)
costos_lineal = plan_lineal(horas)

# 2. ARMADO DE LA GRÁFICA
plt.figure(figsize=(10, 6))

# Dibujo de la recta en color azul
plt.plot(horas, costos_lineal, label="Plan Lineal: $L(x) = 20x + 100$", color="blue", linewidth=2.5)

# Marcamos la Ordenada al Origen (Costo Fijo inicial en el 100)
plt.scatter(0, 100, color="black", s=90, zorder=5, label="Ordenada al origen (0, 100)")

# 3. TÍTULOS Y FORMATO DE PANTALLA
plt.title("Análisis Geométrico: Plan Lineal (Costo Constante)", fontsize=12, fontweight="bold")
plt.xlabel("Horas Contratadas (X)")
plt.ylabel("Costo Total en Pesos (Y)")
plt.xlim(-2, 45)
plt.ylim(0, 1000)
plt.grid(True, linestyle=":", alpha=0.6)
plt.legend(loc="upper left")

# Ejecutar gráfico
plt.show()