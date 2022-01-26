from tkinter import *


raiz = Tk()
def datos():
    pass

raiz.title('Formulario')
raiz.geometry('400x300')
raiz.resizable(True,True)
l_nombre = Label(raiz, text = "Nombre")
l_nombre.pack( side = LEFT)
e_nombre = Entry(raiz, bd = 6)
e_nombre.pack(side = RIGHT)
l_apellidos = Label(raiz, text = "Apellidos")
l_apellidos.pack( side = LEFT)
e_apellidos = Entry(raiz, bd = 6)
e_apellidos.pack(side = RIGHT)
button = Button(raiz, text="Enviar Datos",
    command=lambda: datos())
l_nombre.place(x=50,y=100)
e_nombre.place(x=120,y=100)
l_apellidos.place(x=50,y=150)
e_apellidos.place(x=120,y=150)
button.place(x=200, y=200)
#raiz.iconbitmap("/Programacion/OOP/metodos_estaticos/interfaz_grafica/750_logo_name.png")
raiz.mainloop() 