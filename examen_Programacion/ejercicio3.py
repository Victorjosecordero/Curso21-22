#Victor José Peña Cordero
from Ejercicio2 import Persona
def lista_solicita_usuario():
    seguir = 'Y'
    lista_persona = [] 
    while seguir == 'Y':
        Persona.Nombre = input('Nombre: ')
        Persona.Apellidos = input('Apellidos: ')
        Persona.Edad =  input('Edad: ')
        Persona.DNI = input('DNI: ')
        datos_del_usuario = (Persona.Nombre,Persona.Apellidos,Persona.Edad,Persona.DNI)
        lista_persona.append(datos_del_usuario)
        seguir_pregunta = input('¿Quiere seguir metiendo personas?(Y/N)')
        if seguir_pregunta == 'N':
            seguir = 'N'
    print(lista_persona)
   
lista_solicita_usuario()