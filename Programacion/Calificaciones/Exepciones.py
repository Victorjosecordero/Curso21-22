def dividir(a,b):
    #1-Comprobar que b no sea 0
    #2-dividir y controlar el error

    #if b == 0:
        #return None
    #else:
        #return a/b
        resultado = None
        try:
            #lista de instrucciones
            resultado = a/b
        except ZeroDivisionError:
            #Instrucciones si hay error
            print('Se ha producido un error en la division')
        except TypeError:
            print('Solo se pueden dividir datos numericos')
        else:
            print('Esta es la parte else')

        return resultado

print(dividir(5,'dos'))