def sumar(arg):
    total = 0
    if arg == ([]):
        return "Error: No hay argumentos"

    if type(arg) is str:
        return 0

    if type(arg) is tuple:
        return 0

    for i in arg:
        total += i
    return total


sumar([21,"holamundo",1998])

