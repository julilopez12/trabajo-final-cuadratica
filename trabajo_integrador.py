

# --- APARTADO 1: DEFINICIÓN DE DATOS ---
valores_x = [0, 5, 10, 15, 20, 25, 30, 40, 50]
costos_calculados = []

print("==================================================")
print("   EVALUACIÓN PUNTO POR PUNTO DEL PLAN DE COSTOS  ")
print("==================================================")

# --- APARTADO 2: CÁLCULO MEDIANTE BUCLES NATIVOS ---
for i in range(9):
    x = valores_x[i]
    
    # Evaluación polinómica manual: -2x^2 + 80x + 100
    costo_total = (-2 * (x * x)) + (80 * x) + 100
    
    # Asignación secuencial (Alternativa a .append prohibido)
    costos_calculados += [costo_total]
    
    print(f"Horas contratadas: {x}h  |  Costo resultante: ${costo_total}")


# --- APARTADO 3: BÚSQUEDA DEL MÁXIMO (SIMULACIÓN DE MAX()) ---
max_costo = costos_calculados[0]
hora_del_maximo = valores_x[0]

for i in range(9):
    if costos_calculados[i] > max_costo:
        max_costo = costos_calculados[i]
        hora_del_maximo = valores_x[i]

print("\n==================================================")
print("        ANÁLISIS DE EXTREMOS (VÉRTICE)            ")
print("==================================================")
print(f"Analíticamente, el costo máximo detectado es: ${max_costo}")
print(f"Este pico de gasto se alcanza a las: {hora_del_maximo} horas de desarrollo.")


# --- APARTADO 4: DETECCIÓN DE INCONSISTENCIAS ---
print("\n==================================================")
print("     AUDITORÍA DE VALORES FUERA DE RANGO REAL     ")
print("==================================================")

for i in range(9):
    if costos_calculados[i] < 0:
        print(f"¡ALERTA CRÍTICA! A las {valores_x[i]} horas el costo da: ${costos_calculados[i]}")


# =====================================================================
# SECCIÓN DE INVESTIGACIÓN: GENERACIÓN DE GRÁFICOS (MATPLOTLIB)
# =====================================================================
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))

# Generación de curva suave continua
x_continua = []
y_continua = []
for h in range(0, 51):
    x_continua += [h]
    y_continua += [(-2 * (h ** 2)) + (80 * h) + 100]

# Dibujo de componentes matemáticas
plt.plot(x_continua, y_continua, color='blue', label='Modelo C(x) = -2x² + 80x + 100')
plt.scatter(valores_x, costos_calculados, color='red', zorder=5, label='Puntos Evaluados')
plt.scatter(20, 900, color='green', s=100, marker='^', zorder=6, label='Vértice Máximo (20h, $900)')
plt.axhline(0, color='black', linestyle='--', linewidth=1)

# Estética de la gráfica
plt.title('Optimización de Costos Mensuales (Función Cuadrática)', fontsize=12, fontweight='bold')
plt.xlabel('Cantidad de Horas Mensuales (x)')
plt.ylabel('Costo en Dólares (C)')
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend()

# Mostrar el gráfico en pantalla
plt.show()
