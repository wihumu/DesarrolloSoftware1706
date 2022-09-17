
a=float(input("Ingresa el Coeficiente 'a' : "))
b=float(input("Ingresa el Coeficiente 'b' : "))
c=float(input("Ingresa el Coeficiente 'c' : "))
x1=0.0
x2=0.0
def funcionCuadratica(a,b,c):
    
    validarexpresion = (( b ** 2) - 4 * a * c)

    if validarexpresion < 0:
        print("La ecuación no tiene soluciones reales.")
         
    else:
        raiz = validarexpresion**0.5
        x1 = (-b + raiz) / (2 * a) 
        if (( b ** 2) - 4 * a * c) != 0:
            x2 = (-b - raiz) / (2 * a)
            print(x1,x2)
        else:
            print(x1) 
        
            
funcionCuadratica(a,b,c)











""" from math import sqrt

# mostramos un mensaje de bienvenida
print('¡Hola! Vamos a resolver una ecuación de segundo grado:')
print('    ax² + bx + c = 0\n')

# pedimos los coeficientes al usuario
a=float(input("Ingresa el Coeficiente 'a' : "))
b=float(input("Ingresa el Coeficiente 'b' : "))
c=float(input("Ingresa el Coeficiente 'c' : "))

def funcionCuadratica(a,b,c):
    
    # calculamos el discriminante
    discriminante =  b * b - 4 * a * c

    if discriminante < 0: # comprobamos si no existen soluciones reales
        print("La ecuación no tiene soluciones reales.")
    else:
        raiz = sqrt(discriminante)      # calculamos la raíz
        x_1 = (-b + raiz) / (2 * a)     # calculamos una primera solución
        if discriminante != 0:          # comprobamos si hay otra solución
            x_2 = (-b - raiz) / (2 * a) # calculamos la segunda solución
            print(x_1,x_2) # mostramos las dos soluciones
        else:
            print(x_1) # mostramos la única solución
            
funcionCuadratica(a,b,c) """