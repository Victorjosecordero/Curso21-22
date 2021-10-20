

numeroa = int(20)  
numerointentos = 0

for i in range(10):

    numerointentos +=1

    numero = int(input('Introduce un número: '))

    if numero == numeroa:
        print('Has ganado')

    elif numero != numeroa:
        print('Has fallado')
    if numero == numeroa:
        print(f'Has acertado en {numerointentos} intentos')
        break
    else: 
        numero !=numeroa
        print(f'Llevas {numerointentos} intentos')
    if numero < numeroa:
        print('Tu número es menor')

    elif numero > numeroa:
        print('Tu número es mayor')









 