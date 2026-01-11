# Método de Euler y Separación de Variables

## Descripción del problema
Se resuelve la ecuación diferencial separable:

dy/dt = y, con condición inicial y(0) = 1

Primero se obtiene la solución analítica usando el método de separación de variables y luego se aproxima la solución usando el método de Euler.

## Solución analítica
Separando variables:

1/y dy = dt

Integrando:

ln(y) = t + C

Aplicando la condición inicial y(0)=1, se obtiene:

y(t) = e^t

## Método de Euler
Se aplica el método de Euler en el intervalo t ∈ [0,1] con paso h = 0.2 usando la fórmula:

y_{n+1} = y_n + h f(t_n, y_n)

## Archivos
- euler_method.py: Implementación del método de Euler y comparación con la solución exacta.

## Conclusión
El método de Euler proporciona una aproximación razonable para pasos pequeños, aunque presenta error numérico comparado con la solución exacta.
