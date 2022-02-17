def contar_letras(cadena):
    return {l: cadena.count(l) for l in cadena}

def is_anagram(cadena1, cadena2):
    return contar_letras(cadena1) == contar_letras(cadena2)


print(is_anagram('prueba','preaub'))