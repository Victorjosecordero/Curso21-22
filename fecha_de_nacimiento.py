#pedir fecha naciemiento

#25/01/2000
def nacimiento():
    meses = {
     1:'enero',
     2:'febrero',
     3:'marzo',
     4:'abril',
     5:'mayo',
     6:'junio',
     7:'julio',
     8:'agosto',
     9:'septiembre',
     10:'octubre',
     11:'noviembre',
     12:'diciembre'}
    fecha = input('Dime caundo naciste (dd/mm/aaaa): ')
    partes_fecha = fecha.split('/')
    mes = int(partes_fecha[1]) - 1
    mensaje = 'Naciste el dia ' + partes_fecha[0] + ' del mes de ' + meses[int(partes_fecha[1])] + ' del año ' + partes_fecha[2]
    return mensaje

print(nacimiento())

#naciste el dia 25 de enero del año 2000
#print('Naciste el dia ' + DIA +' '+ 'de '+ MES + ' ' + 'del año ' + ANO)