import math

# Ecuacion diferencial dy/dt = y
def f(t, y):
    return y

# Parametros
h = 0.2
t_final = 1
t = 0

# Condicion inicial
y = 1  

print("t\tEuler\tExacta")
print(t, "\t", round(y, 4), "\t", round(math.exp(t), 4))

# Metodo de Euler
while t < t_final:
    y = y + h * f(t, y)
    t = t + h
    print(round(t, 1), "\t", round(y, 4), "\t", round(math.exp(t), 4))
