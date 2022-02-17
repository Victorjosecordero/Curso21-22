def only_ints(v1, v2):

    if type(v1) == int and type(v2) == int:
        return True
    else: 
        return False

print(only_ints(1, 2)) 