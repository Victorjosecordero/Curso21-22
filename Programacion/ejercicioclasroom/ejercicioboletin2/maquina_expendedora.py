while True:
 n=input("Seleccione una acción:")
 if n=='r':
   l=input('Ingrese la cantidad de bienes:')
   v=l.split('-')
   numA1=int(v[0])
   numA2=int(v[1])
   numA3=int(v[2])
   numA4=int(v[3])
   numA5=int(v[4])
   numA6=int(v[5])
   t=input('Ingrese el número de monedas:')
   u=t.split('-')
   yiyuan=int(u[0])
   liangyuan=int(u[1])
   wuyuan=int(u[2])
   shiyuan=int(u[3])
   print('S001:Initialization is successful')
 elif n=='q':
     print('Gestión de miembros'.center(50,'*'))

     print("""
                               Directorio de operaciones
                               0-excedente de carga
                               1-Caja de dinero """)
     while True:
       c=input()
       if c=='0':

         print('A1 %d A2 %d A3 %d A4%d A5 %d A6 %d' %(numA1,numA2,numA3,numA4,numA5,numA6))
       elif c=='1':
         print('1yuan coin number=%d 2yuan coin number=%d 5yuan coin number=%d 10 yuan coin number=%d' %(yiyuan,liangyuan,wuyuan,shiyuan))
 elif n=='p':
  counname=input('Seleccione un producto:')
  if counname=='1':
    if numA1<=0:
            print('E007:The goods sold out')
    else:
         m=input('Ingrese efectivo:')
         if m=='1':
            print('S003:Buy success,balance=1')
            print('E009:Work failure')
            numA1-=1
            yiyuan+=1
         elif m=='2':
            print('S003:Buy success,balance=1')
            numA1-=1
            liangyuan+=1
            yiyuan-=1
            print('Encontrarte un yuan')
         elif m=='5':
             if yiyuan*1+liangyuan*2<5:
                 print('E003:Change is not enough,pay fail')
             else:
                 print('S002:Pay success,balance=1')
                 print('S003:Buy success,balance=1')
                 numA1-=1
                 wuyuan+=1
                 liangyuan-=2
                 print('Te encuentro 4 yuanes')
         elif m=='10':
             if yiyuan*1+liangyuan*2<10:
                 print('E003:Change is not enough,pay fail')
             else:
                 print('S002:Pay success,balance=1')
                 print('S003:Buy success,balance=1')
                 shiyuan+=1
                 wuyuan-=1
                 liangyuan-=2
                 print('Te encuentro 9 yuanes')
         else:
             print('E002:Denomination error')

  elif counname == '2':
     if numA2 <= 0:
         print('E007:The goods sold out')
     else:
         m=input('Ingrese efectivo:')
         if m == '1':
             print('E008:Lack of balance')
         elif m == '2':
             print('S003:Buy success,balance=1')
             print('E009:Work failure')
             numA2 -= 1
             liangyuan += 1
         elif m == '5':
             if yiyuan * 1 + liangyuan * 2 < 5:
                 print('E003:Change is not enough,pay fail')
             else:
                 print('S002:Pay success,balance=2')
                 print('S003:Buy success,balance=1')
                 wuyuan+=1
                 yiyuan-=1
                 liangyuan-=1
                 print('Te encuentro tres yuanes')
         elif m == '10':
             if yiyuan * 1 + liangyuan * 2  < 10:
                 print('E003:Change is not enough,pay fail')
             else:
                 print('S002:Pay success,balance=2')
                 print('S003:Buy success,balance=1')
                 numA2-=1
                 shiyuan+=1
                 wuyuan-=1
                 yiyuan-=1
                 liangyuan-=2
                 print('Te encuentro 8 yuanes')
         else:
             print('E002:Denomination error')
  elif counname == '3':
     if numA3 <= 0:
         print('E007:The goods sold out')
     else:
         m=input('Ingrese efectivo:')
         if m == '1':
             print('E008:Lack of balance')
         elif m == '2':
             print('E008:Lack of balance')
         elif m == '5':
             if yiyuan * 1 + liangyuan * 2 < 5:
                 print('E003:Change is not enough,pay fail')
             else:
                 print('S002:Pay success,balance=3')
                 print('S003:Buy success,balance=1')
                 numA3-=1
                 wuyuan += 1
                 liangyuan -= 1
                 print('Te encuentro tres yuanes')
         elif m == '10':
             if yiyuan * 1 + liangyuan * 2  < 10:
                 print('E003:Change is not enough,pay fail')
             else:
                 print('S002:Pay success,balance=3')
                 print('S003:Buy success,balance=1')
                 numA3 -= 1
                 shiyuan += 1
                 wuyuan -= 1
                 liangyuan -= 1
                 print('Te encuentro 7 yuanes')
         else:
             print('E002:Denomination error')
  elif counname == '4':
     if numA4 <= 0:
         print('E007:The goods sold out')
     else:
         m=input('Ingrese efectivo:')
         if m == '1':
             print('E008:Lack of balance')
         elif m == '2':
             print('E008:Lack of balance')
         elif m == '5':
             if yiyuan * 1 + liangyuan * 2 < 5:
                 print('E003:Change is not enough,pay fail')
             else:
                 print('S002:Pay success,balance=4')
                 print('S003:Buy success,balance=1')
                 numA4 -= 1
                 wuyuan += 1
                 yiyuan -= 1
                 print('Te encuentro 1 yuan')
         elif m == '10':
             if yiyuan * 1 + liangyuan * 2  < 10:
                 print('E003:Change is not enough,pay fail')
             else:
                 print('S002:Pay success,balance=4')
                 print('S003:Buy success,balance=1')
                 numA4 -= 1
                 shiyuan += 1
                 wuyuan -= 1
                 yiyuan -= 1
                 print('Te encuentro 6 yuanes')
         else:
             print('E002:Denomination error')
  elif counname == '5':
     if numA5 <= 0:
         print('E007:The goods sold out')
     else:
         m=input('Ingrese efectivo:')
         if m == '1':
             print('E008:Lack of balance')
         elif m == '2':
             print('E008:Lack of balance')
         elif m == '5':
             print('E008:Lack of balance')
         elif m == '10':
             if yiyuan * 1 + liangyuan * 2 < 10:
                 print('E003:Change is not enough,pay fail')
             else:
                 print('S002:Pay success,balance=6')
                 print('S003:Buy success,balance=1')
                 numA5 -= 1
                 shiyuan += 1
                 liangyuan-=2
                 print('Te encuentro 4 yuanes')
         else:
             print('E002:Denomination error')
  elif counname == '6':
     if numA6 <= 0:
         print('E007:The goods sold out')
     else:
         m=input('Ingrese efectivo:')
         if m == '1':
             print('E008:Lack of balance')
         elif m == '2':
             print('E008:Lack of balance')
         elif m == '5':
                 print('S003:Buy success,balance=1')
                 print('E009:Work failure')
                 numA6 -= 1
                 wuyuan+=1
         elif m == '10':
             if yiyuan * 1 + liangyuan * 2 < 10:
                 print('E003:Change is not enough,pay fail')
             else:
                 print('S002:Pay success,balance=5')
                 print('S003:Buy success,balance=1')
                 numA6 -= 1
                 shiyuan += 1
                 wuyuan -= 1
                 print('Te encuentro 5 yuanes')
  else:
    print('E006:Goods does not exist')
 else:
      print('Operación inválida')