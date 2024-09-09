
from tkinter import *
import math

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: División por cero."

def factorial(n):
    if isinstance(n, int) and n >= 0:
        return math.factorial(n)
    else:
        return "El factorial no está definido para números negativos o no enteros."

def mcm(a, b):
    return abs(a * b) // math.gcd(a, b)

def mcd(a, b):
    return math.gcd(a, b)

def valor_absoluto(n):
    return abs(n)

def calcular():
    operacion_seleccionada = operacion.get()
    try:
        primer_numero = int(entry_a.get())
        segundo_numero = int(entry_b.get())

        if operacion_seleccionada == 'suma':
            resultado = suma(primer_numero, segundo_numero)
        elif operacion_seleccionada == 'resta':
            resultado = resta(primer_numero, segundo_numero)
        elif operacion_seleccionada == 'multiplicacion':
            resultado = multiplicacion(primer_numero, segundo_numero)
        elif operacion_seleccionada == 'division':
            resultado = division(primer_numero, segundo_numero)
        elif operacion_seleccionada == 'mcm':
            resultado = mcm(primer_numero, segundo_numero)
        elif operacion_seleccionada == 'mcd':
            resultado = mcd(primer_numero, segundo_numero)
        elif operacion_seleccionada == 'abs':
            resultado = valor_absoluto(primer_numero)
        else:
            resultado = "Opción no válida."

        result_label.config(text=f"Resultado: {resultado}")

        if isinstance(resultado, (int, float)) and resultado == int(resultado):
            fact_resultado = factorial(int(resultado))
            factorial_label.config(text=f"Factorial de {int(resultado)} = {fact_resultado}")
        else:
            factorial_label.config(text="")

    except ValueError:
        result_label.config(text="Error: Entrada no válida.")

def salir():
    ventana.quit()

ventana = Tk()
ventana.title("Calculadora")

Label(ventana, text="Primer número:").grid(row=0, column=0)
entry_a = Entry(ventana)
entry_a.grid(row=0, column=1)

Label(ventana, text="Segundo número:").grid(row=1, column=0)
entry_b = Entry(ventana)
entry_b.grid(row=1, column=1)

Label(ventana, text="Operación:").grid(row=2, column=0)
operacion = StringVar()
operacion.set('suma')  # Valor por defecto
OptionMenu(ventana, operacion, 'suma', 'resta', 'multiplicacion', 'division', 'mcm', 'mcd', 'abs').grid(row=2, column=1)

Button(ventana, text="Calcular", command=calcular).grid(row=3, column=0)
Button(ventana, text="Salir", command=salir).grid(row=3, column=1)

result_label = Label(ventana, text="")
result_label.grid(row=4, columnspan=2)

factorial_label = Label(ventana, text="")
factorial_label.grid(row=5, columnspan=2)

ventana.mainloop()
