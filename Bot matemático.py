import operator
import math
import re

def realizar_operacion(operador, numeros):
    operaciones = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv,
        '^': operator.pow,
        'sqrt': math.sqrt,
        'sin': math.sin,
        'cos': math.cos,
        'tan': math.tan
    }
    if operador in operaciones:
        try:
            resultado = numeros[0]
            for i in range(1, len(numeros)):
                resultado = operaciones[operador](resultado, numeros[i])
            return resultado
        except ZeroDivisionError:
            return "Error: División por cero"
        except ValueError:
            return "Error: Valor inválido para operación"
    else:
        return "Operación inválida"

def evaluar_expresion(expresion):
    partes = re.split(r'(\+|\-|\*|\/|\^)', expresion)
    partes = [parte.strip() for parte in partes if parte.strip()]
    
    if len(partes) < 3 or len(partes) % 2 == 0:
        return "Expresión inválida"
    
    numeros = []
    operadores = []
    
    for i, parte in enumerate(partes):
        if i % 2 == 0:
            numeros.append(float(parte))
        else:
            operadores.append(parte)
    
    resultado = numeros[0]
    
    for i in range(1, len(numeros)):
        resultado = realizar_operacion(operadores[i-1], [resultado, numeros[i]])
    
    return resultado

print("¡Bienvenido al Bot Matemático!")
while True:
    operacion = input("Ingrese la operación en el formato 'num1 operador num2 operador num3 ...': ")
    
    resultado = evaluar_expresion(operacion)
    
    print("Resultado:", resultado)
    
    opcion = input("¿Desea realizar otra operación? (S/N): ")
    if opcion.lower() != 's':
        break

print("¡Gracias por usar el Bot Matemático!")
