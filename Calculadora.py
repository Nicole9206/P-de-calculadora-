from tkinter import *
import parser

root = Tk()
root.title("calculadora") 
display = Entry(root)
display.grid(row=1, columnspan=6, sticky=W+E)#primera fila, columnas y ancho que barca

i = 0 #el indice comienza en 0

def numeros(n):
    global i 
    display.insert(i, n)
    i+=1 #incrementando en 1 



def operaciones(operator):
    global i
    operator_lenght = len(operator)
    display.insert(i,operator)
    i+=operator_lenght


def borrar():
    display.delete(0, END)

def undo():
    display_state = display.get()
    if len(display_state):
        display_new_state = display_state  [:-1]
        borrar()
        display.insert(0, display_new_state)
    else:
        borrar()
        display.insert(0, 'Error')

def calcular():
    display_state = display.get()
    try:
        expression_mat = parser.expr(display_state).compile()
        resultado = eval(expression_mat)
        borrar()
        display.insert(0, resultado)
    except expression as identifier:
        borrar()
        display.insert(0, 'Error')

#Buttons
Button(root, text="1", command=lambda:numeros(1)). grid(row=2, column=0, sticky=W+E) #posición de la ventana
Button(root, text="2", command=lambda:numeros(2)). grid(row=2, column=1, sticky=W+E) 
Button(root, text="3", command=lambda:numeros(3)). grid(row=2, column=2, sticky=W+E) 

Button(root, text="4", command=lambda:numeros(4)). grid(row=3, column=0, sticky=W+E) 
Button(root, text="5", command=lambda:numeros(5)). grid(row=3, column=1, sticky=W+E) 
Button(root, text="6", command=lambda:numeros(6)). grid(row=3, column=2, sticky=W+E) 

Button(root, text="7", command=lambda:numeros(7)). grid(row=4, column=0, sticky=W+E) 
Button(root, text="8", command=lambda:numeros(8)). grid(row=4, column=1, sticky=W+E) 
Button(root, text="9", command=lambda:numeros(9)). grid(row=4, column=2, sticky=W+E) 

#Buttons parte 2
Button(root, text="AC", command=lambda:borrar()). grid(row=5, column=0, sticky=W+E) 
Button(root, text="0", command=lambda:numeros(0)). grid(row=5, column=1, sticky=W+E) 
Button(root, text="%", command=lambda: operaciones("%")). grid(row=5, column=2, sticky=W+E) 

#Buttons PARTE 3 RELACIONADOS CON LAS OPERACIONES (+-/*)
Button(root, text="+", command=lambda: operaciones("+")). grid(row=2, column=3, sticky=W+E) 
Button(root, text="-", command=lambda: operaciones("-")). grid(row=3, column=3, sticky=W+E) 
Button(root, text="/", command=lambda: operaciones("/")). grid(row=4, column=3, sticky=W+E) 
Button(root, text="*", command=lambda: operaciones("*")). grid(row=5, column=3, sticky=W+E) 

#Buttons PARTE 4
Button(root, text="←", command=lambda: undo()). grid(row=2, column=4, sticky=W+E, columnspan=2) 
Button(root, text="exp", command=lambda: operaciones("**")). grid(row=3, column=4, sticky=W+E) 
Button(root, text="^2", command=lambda: operaciones("**2")). grid(row=3, column=5, sticky=W+E) 
Button(root, text="(", command=lambda: operaciones("(")). grid(row=4, column=4, sticky=W+E) 
Button(root, text=")", command=lambda: operaciones(")")). grid(row=4, column=5, sticky=W+E) 
Button(root, text="=", command = lambda: calcular()). grid(row=5, column=4, sticky=W+E, columnspan=2) 

root.mainloop()