# v1 = [1,2]
# v2 = [7,8]
# resultado = 0
# # v1*v2

# for x in range(len(v1)):
#     resultado += v1[x] * v2[x]
#     print(resultado)

origen = [1,2,3,4,5,'Jose', 'Alan', 'Fernando']
numeros = []
alumnos = []

for x in origen:
    if type(x) == str:
        alumnos.append(x)
    else:
        numeros.append(x)

print(origen)
print(alumnos)
print(numeros)

