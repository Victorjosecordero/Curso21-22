#funcion para calcular precio del parking
#teniendo en cuenta:
#1semana: 100€
#1 dia: 42€
#si estoy 35 dias cuanto pagare
#-----------------------------------------
#calcular las semanas
#calcular los dias restantes
#costes por semanas
#costes por dias
#calculo del total

from constantes_parking import P_DIAS,P_SEMANA,SEMANA
dias = int(input('Cuantos dias vas a estar: '))


def calcular_precio(dias):
    
    semana = dias // SEMANA
    dias_restantes = dias % SEMANA
    costes_semanal = semana * P_SEMANA
    costes_dias = dias_restantes * P_DIAS
    total = costes_semanal + costes_dias
    
    return total
print(calcular_precio(dias))