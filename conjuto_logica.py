# ==========================================
# UNIDAD 1: CONJUNTOS Y LÓGICA
# ==========================================

# Definimos el Universo de usuarios registrados (por ID o nombre)
universo_usuarios = {"Ana", "Beto", "Carlos", "Damián", "Elena", "Federico"}

# Conjunto A: Usuarios que ingresaron la clave correcta
conjunto_A = {"Ana", "Beto", "Carlos", "Damián"}

# Conjunto B: Usuarios que tienen la cuenta en estado Activo
conjunto_B = {"Ana", "Beto", "Elena", "Federico"}

# --- OPERACIÓN DE CONJUNTOS ---
# Calculamos la Intersección (A ∩ B) para el acceso seguro
usuarios_autorizados = conjunto_A.intersection(conjunto_B)

print("--- CONTROL DE ACCESO (TEORÍA DE CONJUNTOS) ---")
print(f"Universo total de la plataforma: {universo_usuarios}")
print(f"Usuarios con clave correcta (Conjunto A): {conjunto_A}")
print(f"Usuarios en estado activo (Conjunto B): {conjunto_B}")
print(f"-> INTERSECCIÓN (Acceso Concedido A ∩ B): {usuarios_autorizados}\n")


# --- EVALUACIÓN LÓGICA (Tabla de Verdad individual) ---
# Simulamos la función que evalúa la proposición: (p ∧ q) -> r
def evaluar_login(nombre, tiene_clave, esta_activo):
    p = tiene_clave  # Proposición p
    q = esta_activo  # Proposición q

    conjuncion = p and q  # (p ∧ q)

    # El condicional (p -> q) en programación se evalúa como (not p or q)
    r = conjuncion  # En este sistema, el acceso (r) se da si la conjunción es verdadera
    resultado_condicional = (not conjuncion) or r

    print(f"Usuario: {nombre:<8} | p (Clave): {str(p):<5} | q (Activo): {str(q):<5} | (p ∧ q): {str(conjuncion):<5} | r (Ingreso): {str(r):<5} | Condicional: {resultado_condicional}")


print("--- SIMULACIÓN LÓGICA PROPOSICIONAL ---")
# Probamos las combinaciones con usuarios reales
evaluar_login("Ana", tiene_clave=True, esta_activo=True)  # V y V -> V
evaluar_login("Carlos", tiene_clave=True, esta_activo=False)  # V y F -> F (Bloqueado)
evaluar_login("Elena", tiene_clave=False, esta_activo=True)  # F y V -> F (Bloqueado)