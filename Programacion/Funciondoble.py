# def funcionDoble(numero):
#     if type(numero) in [int, float, complex]:
#         return numero*2
#     else:
#         return None
# print(funcionDoble('Hola'))
# print(funcionDoble(5))
# print(funcionDoble(2.4687))
# print(funcionDoble(2+8j))

# cadena = input('Dime una palabra:')

def limpiar(cadena):
    s = cadena.lower()
    s = s.replace(" ","")
    s = s.replace(",","")
    s = s.replace(".","")
    s = s.replace(";","")
    s = s.replace("-","")
    s = s.replace("_","")
    s = s.replace("à","a")
    s = s.replace("é","e")
    s = s.replace("í","i")
    s = s.replace("ó","o")
    s = s.replace("ù","u")
    return s



def palindromo(s):
    s =limpiar(s)
    return s == s[::-1]

print(palindromo('No subas, abusón'))
   


