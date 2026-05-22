import matplotlib.pyplot as plt
import numpy as np

# 1. DEFINICIÓN DE LA FUNCIÓN DE COSTOS
# C(x) = -2x^2 + 80x + 100
def calcular_costo(x):
    return -2 * (x**2) + 80 * x + 100


# 2. CONFIGURACIÓN DEL DOMINIO (HORAS)
# Creamos un vector de horas que va desde 0 hasta 45 horas para ver bien la montaña
# El número 400 indica que genera 400 puntos intermedios para que la curva salga suave
horas = np.linspace(0, 45, 400)

# Calculamos los costos (variable dependiente Y) pasando el vector de horas por la función
costos = calcular_costo(horas)

# 3. CÁLCULO ANALÍTICO DEL VÉRTICE (PUNTOS CRÍTICOS)
# Fórmula del eje de simetría: xv = -b / (2a)
a = -2
b = 80
x_v = -b / (2 * a)  # Esto da 20 horas
y_v = calcular_costo(x_v)  # Esto da $900 (Costo máximo)

# 4. DISEÑO DEL GRÁFICO (MATPLOTLIB)
plt.figure(figsize=(10, 6))

# Dibujamos la curva principal de la parábola en color rojo
plt.plot(
    horas, costos, label="Función de Costos $C(x) = -2x^2 + 80x + 100$", color="#e53e3e", linewidth=2.5
)

# Marcamos el punto de la Ordenada al Origen (0, 100) -> Costo Fijo
plt.scatter(0, 100, color="#2b6cb0", s=80, zorder=5)
plt.text(
    1,
    110,
    "Ordenada al origen (0, 100)\nCosto Fijo Inicial",
    color="#2b6cb0",
    fontsize=10,
    fontweight="bold",
)

# Marcamos el punto del Vértice (20, 900) -> Costo Máximo
plt.scatter(x_v, y_v, color="#3b835f", s=100, marker="^", zorder=5)
plt.text(
    x_v + 1,
    y_v - 30,
    f"Vértice ({int(x_v)}, ${int(y_v)})\nCosto Máximo Absoluto",
    color="#2f855a",
    fontsize=10,
    fontweight="bold",
)

# Líneas punteadas de guía para el vértice
plt.axvline(x=x_v, color="#718096", linestyle="--", alpha=0.6)
plt.axhline(y=y_v, color="#718096", linestyle="--", alpha=0.6)

# 5. CONFIGURACIÓN DE EJES, TÍTULOS Y RECUADROS
plt.title(
    "Análisis Geométrico del Modelo de Costos (Función Cuadrática)",
    fontsize=14,
    fontweight="bold",
    pad=15,
)
plt.xlabel("Horas Contratadas (Variable Independiente X)", fontsize=11)
plt.ylabel("Costo Total en Pesos (Variable Dependiente Y)", fontsize=11)

# Activamos la cuadrícula de fondo para que sea más fácil leer los valores
plt.grid(True, linestyle=":", alpha=0.6)
plt.legend(loc="upper right", fontsize=10)

# Ajustamos los límites de visualización en pantalla
plt.xlim(-2, 45)
plt.ylim(0, 1000)

# 6. MOSTRAR EL GRÁFICO FINAL
plt.show()