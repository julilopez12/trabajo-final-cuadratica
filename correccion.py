import matplotlib.pyplot as plt

# ==========================================
# 1. GENERACIÓN DE PUNTOS PARA UNA CURVA SUAVE
# ==========================================
# Creamos listas vacías para el gráfico de alta precisión
x_curva = []
costos_A = []
costos_B = []
costos_C = []

# Usamos un ciclo básico que avance de a 0.1 para que la parábola sea perfecta
# Como range solo usa enteros, vamos de 0 a 500 y dividimos por 10
for i in range(501):
    x = i / 10.0
    x_curva.append(x)
    costos_A.append(40 * x + 200)               # Plan A [cite: 114]
    costos_B.append(70 * x + 50)                # Plan B [cite: 115]
    costos_C.append(-2 * (x ** 2) + 80 * x + 100) # Plan C 

# ==========================================
# 2. EVALUACIÓN DE LOS VALORES REQUERIDOS (Para el informe)
# ==========================================
valores_requeridos = [0, 5, 10, 15, 20, 25, 30, 40, 50] [cite: 133]
print("X \t Plan A \t Plan B \t Plan C")
print("-" * 45)
for xr in valores_requeridos:
    cA = 40 * xr + 200 [cite: 114]
    cB = 70 * xr + 50 [cite: 115]
    cC = -2 * (xr ** 2) + 80 * xr + 100 [cite: 116]
    print(f"{xr} \t {cA} \t\t {cB} \t\t {cC}")

# ==========================================
# 3. DISEÑO Y CONFIGURACIÓN DEL GRÁFICO
# ==========================================
plt.figure(figsize=(11, 6.5))

# Graficamos usando las listas de alta precisión (x_curva)
plt.plot(x_curva, costos_A, label="Plan A: 40x + 200", color="blue", linewidth=2.5) [cite: 114]
plt.plot(x_curva, costos_B, label="Plan B: 70x + 50", color="green", linewidth=2.5) [cite: 115]
plt.plot(x_curva, costos_C, label="Plan C: -2x² + 80x + 100", color="red", linewidth=2.5) [cite: 116]

# Dibujamos pelotitas en los puntos específicos que pide la consigna para demostrar consistencia
costos_C_puntos = []
for xr in valores_requeridos:
    costos_C_puntos.append(-2 * (xr ** 2) + 80 * xr + 100) [cite: 116]
plt.scatter(valores_requeridos, costos_C_puntos, color="darkred", zorder=5, label="Puntos evaluados C(x)")

# Configuración estricta del dominio y copete visual
plt.title("Comparativa de Modelos de Costos e Intersecciones", fontsize=14, fontweight='bold')
plt.xlabel("Horas Contratadas Mensuales (X)", fontsize=11)
plt.ylabel("Costo Total en Pesos (Y)", fontsize=11)

# Límites del gráfico: Dominio exacto [0, 50] y el Y permite ver el negativo
plt.xlim(0, 50) [cite: 117]
plt.ylim(-150, 1000)

# Líneas de los ejes cartesianos principales
plt.axhline(0, color='black', linestyle='-', linewidth=1, alpha=0.6)
plt.axvline(0, color='black', linestyle='-', linewidth=1, alpha=0.6)

# Cuadrícula de fondo
plt.grid(True, linestyle=":", alpha=0.6)
plt.legend(loc="upper right", fontsize=10)

# Mostrar el resultado final
plt.show()