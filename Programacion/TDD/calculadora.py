


def suma(cadena):
    lista = cadena.split(',')
    for l in lista:
        if not l.isdigit():
            return 'Caracter no digito'

    if len(lista)>2:
        return 'Error:Demasiados numeros'
    elif len(lista) == 2:
        return True
   


def mas_de_dos_numeros_da_error():
    return suma("1,2,3")




def dos_numeros_devulve_true():
    return suma('1,2')


def no_numerico():
    return suma ('1,2')
#----------------------------
print(mas_de_dos_numeros_da_error())
print(dos_numeros_devulve_true())
print(no_numerico())