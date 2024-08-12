# Pide al usuario que ingrese una función matemática en formato de cadena
funcion_usuario = input("Ingresa una función matemática de x (por ejemplo, 'x**2 + 2*x + 1'): ")

# Define una función que evalúa la expresión ingresada
def funcion(x):
    return eval(funcion_usuario)

# Prueba la función con diferentes valores de x
for x in range(-5, 6):
    print(f"f({x}) = {funcion(x)}")
    
import sympy as sp


print("derivada")
x = sp.symbols('x', real=True)
f_expr = x**3+2*x-2
f_der_expr = sp.diff(f_expr,x)
resultado = round(eval(str(f_der_expr), {"x": 2}), 7)
print(f_der_expr)
print(resultado)