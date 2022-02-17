#Victor Jose Peña Cordero

def añadir(s):
    return ".".join(s)

def quitar(s):
    return s.replace(".", "")


s='prueba'

print(añadir(s))
print(quitar(s))