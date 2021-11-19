def funciones(p1,p2,p3,*args,**kwargs):
    print(p1,p2,p3)
    print(args)
    print(kwargs)

funciones(1,2,5,nombre='victor',dia='viernes')