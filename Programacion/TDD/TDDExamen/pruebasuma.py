def sumalista(arg):
    total = 0
    for i in arg:
        total = total + i
    return total

print(sumalista([6,3,1,7]))