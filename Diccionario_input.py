AFORO_MAXIMO= 8
def introduce():
    personas = {}
    
    for i in range(1200):
        if i == AFORO_MAXIMO:
            break
        nombre = input('Introduce nombre:')
        apellidos = input('Introduce apellidos:')
        dni = input('Introduce DNI:')
        personas[dni] = {'nombre':nombre, 'apellidos':apellidos}
    
    return personas

print(introduce())