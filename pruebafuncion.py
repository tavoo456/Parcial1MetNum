# Pide al usuario que ingrese una función matemática en formato de cadena
funcion_usuario = input("Ingresa una función matemática de x (por ejemplo, 'x**2 + 2*x + 1'): ")

# Define una función que evalúa la expresión ingresada
def funcion(x):
    return eval(funcion_usuario)

# Prueba la función con diferentes valores de x
for x in range(-5, 6):
    print(f"f({x}) = {funcion(x)}")