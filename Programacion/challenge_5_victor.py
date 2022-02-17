def double_letters(letras):
    for l in range(len(letras)-1):
        if letras[l] == letras[l+1]:
            return True
    return False

print(double_letters("prueba"))