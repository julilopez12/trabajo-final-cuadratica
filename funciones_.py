import matplotlib.pyplot as plt

# ==========================================
# 1. GENERACIÓN DE DATOS Y LÓGICA DEL PROYECTO
# ==========================================
x_curva = list(range(0, 51))

costos_A = []
costos_B = []
costos_C = []

for x in x_curva:
    y_a = 40 * x + 200
    costos_A.append(y_a)
    
    y_b = 70 * x + 50
    costos_B.append(y_b)
   # funcion cuadratica - juliana 
    
    y_c = -2 * (x ** 2) + 80 * x + 100
    costos_C.append(y_c)

# ==========================================
# 2. MOSTRAR TABLA DE COSTOS EN CONSOLA
# ==========================================
print(f"{'Horas (X)':<10} | {'Plan A ($)':<12} | {'Plan B ($)':<12} | {'Plan C ($)':<12}")
print("-" * 55)

for i in range(0, 51, 5):
    print(f"{x_curva[i]:<10} | ${costos_A[i]:<11} | ${costos_B[i]:<11} | ${costos_C[i]:<11}")

print("\n" + "="*55 + "\n")

# ==========================================
# 3. CONFIGURACIÓN Y APERTURA DE LA GRÁFICA
# ==========================================
plt.figure(figsize=(10, 6))

plt.plot(x_curva, costos_A, label="Plan A: 40x + 200", color="blue", linewidth=2)
plt.plot(x_curva, costos_B, label="Plan B: 70x + 50", color="green", linewidth=2)
plt.plot(x_curva, costos_C, label="Plan C: -2x² + 80x + 100", color="red", linewidth=2)

plt.title("Comparativa de Modelos de Costos de Desarrollo", fontsize=12, fontweight='bold')
plt.xlabel("Horas Contratadas Mensuales (X)", fontsize=10)
plt.ylabel("Costo Total en Pesos (Y)", fontsize=10)

plt.xlim(0, 50)
plt.ylim(-150, 1000)

plt.axhline(0, color='black', linestyle='-', linewidth=0.8, alpha=0.5)
plt.axvline(0, color='black', linestyle='-', linewidth=0.8, alpha=0.5)
plt.grid(True, linestyle=":", alpha=0.6)
plt.legend()

plt.show()