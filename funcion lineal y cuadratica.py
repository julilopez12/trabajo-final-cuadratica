import matplotlib.pyplot as plt
import numpy as np

# 1. FÓRMULAS DEL MODELO
def plan_lineal(x):
    return 20 * x + 100

def plan_cuadratico(x):
    return -2 * (x**2) + 80 * x + 100

# Rango de tiempo para las x (de 0 a 45 horas)
horas = np.linspace(0, 45, 400)

# CÁLCULOS
costos_lineal = plan_lineal(horas)
costos_cuadratico = plan_cuadratico(horas)


# ==========================================
# VENTANA 1: GRÁFICO DE LA FUNCIÓN LINEAL
# ==========================================
plt.figure(1, figsize=(9, 5))

# Dibujo de la recta azul
plt.plot(horas, costos_lineal, label="Plan Lineal: $L(x) = 20x + 100$", color="blue", linewidth=2.5)
plt.scatter(0, 100, color="black", s=90, zorder=5) # Ordenada

plt.title("Gráfica 1: Plan Lineal (Compañero)", fontsize=12, fontweight="bold")
plt.xlabel("Horas Contratadas (X)")
plt.ylabel("Costo Total en Pesos (Y)")
plt.xlim(-2, 45)
plt.ylim(0, 1000)
plt.grid(True, linestyle=":", alpha=0.6)
plt.legend(loc="upper left")


# ==========================================
# VENTANA 2: GRÁFICO DE LA FUNCIÓN CUADRÁTICA
# ==========================================
plt.figure(2, figsize=(9, 5))

# Dibujo de tu curva roja
plt.plot(horas, costos_cuadratico, label="Plan Cuadrático: $C(x) = -2x^2 + 80x + 100$", color="red", linewidth=2.5)
plt.scatter(0, 100, color="black", s=90, zorder=5) # Ordenada
plt.scatter(20, 900, color="green", s=100, marker="^", zorder=5) # Vértice

# Líneas punteadas para marcar la cima de la montaña
plt.axvline(x=20, color="gray", linestyle="--", alpha=0.5)
plt.axhline(y=900, color="gray", linestyle="--", alpha=0.5)

plt.title("Gráfica 2: Función Cuadrática (Tu parte)", fontsize=12, fontweight="bold")
plt.xlabel("Horas Contratadas (X)")
plt.ylabel("Costo Total en Pesos (Y)")
plt.xlim(-2, 45)
plt.ylim(0, 1000)
plt.grid(True, linestyle=":", alpha=0.6)
plt.legend(loc="upper right")


# ==========================================
# MOSTRAR LAS DOS VENTANAS
# ==========================================
plt.show()