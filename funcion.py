#Las funciones son:
#A(𝑥) = 40𝑥 +200 
#B(𝑥) = 70𝑥+50
#C(𝑥) = −2𝑥2 +80𝑥+100 
                                     #Se trabajará en el siguiente dominio: 𝐷𝑓 = 0 ≤ 𝑥 ≤ 50
print("\n========== CONSIGNA 2 ==========")


def A_funcion(x):
    return 40 * x + 200

def B_funcion(x):
    return 70 * x + 50

def C_funcion(x):
    return -2 * (x ** 2) + 80 * x + 100


print("Pendiente A:", 40)
print("Ordenada A:", 200)

print("Pendiente B:", 70)
print("Ordenada B:", 50)


if 40 == 70:
    print("Las rectas son paralelas")
else:
    print("Las rectas NO son paralelas")

    x_interseccion = 5
y_interseccion = A_funcion(x_interseccion)

print("Punto de interseccion:", (x_interseccion, y_interseccion))


xv = -80 / (2 * -2)
yv = C_funcion(xv)

print("Vertice de C:", (xv, yv))
import math

a = -2
b = 80
c = 100

delta = b**2 - 4*a*c

x1 = (-b + math.sqrt(delta)) / (2*a)
x2 = (-b - math.sqrt(delta)) / (2*a)

print("Raiz 1:", x1)
print("Raiz 2:", x2)


valores_x = [0, 5, 10, 15, 20, 25, 30, 40, 50]

print("\nIMPLEMENTACIÓN-ANALISIS")

for x in valores_x:

    print("x =", x)

    print("A(x) =", A_funcion(x))
    print("B(x) =", B_funcion(x))
    print("C(x) =", C_funcion(x))

    print()

#ANALISIS

def plan_mas_barato(x):

    a = A_funcion(x)
    b = B_funcion(x)
    c = C_funcion(x)

    menor = min(a, b, c)

    if menor == a:
        return "Plan A"

    elif menor == b:
        return "Plan B"

    else:
        return "Plan C"

print("Plan mas economico para x=10:", plan_mas_barato(10))

# Valores negativos de C
print("\nValores negativos de C")

for x in range(0, 51):

    if C_funcion(x) < 0:
        print("x =", x, "->", C_funcion(x))