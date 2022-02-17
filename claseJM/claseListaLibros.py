''' Jose Manuel Perez Puig
clase para modelar el objeto lista. En este caso una lista de libros que hay que mantener siempre ordenados'''

OVER = 'ERROR: En esa posición no hay ningún libro. Número de libros actual = '

class ListaLibros():
    def __init__(self, lista=[]) -> None:
        self.__lista_libros = lista
        self.__lista_libros.sort()
        self.__numero_de_libros = len(self.__lista_libros)


    @property
    def numero_de_libros(self):
        '''devuelve el número de libros que hay actualmente en la lista'''
        return self.__numero_de_libros


    def inserta_libro(self, nuevo_libro):
        '''recibe un nuevo libro y lo inserta en la lista en la posicion dada por el orden alfabético'''
        posicion = self.__busca_indice(nuevo_libro)
        self.__lista_libros.insert(posicion, nuevo_libro)
        self.__numero_de_libros += 1


    def elimina_libro(self, pos):
        '''elimina de la lista de libros el libro que haya en la posición pasada'''
        if self.__valida_posicion(pos):    
            self.__lista_libros.pop(pos-1)
            self.__numero_de_libros -= 1
        else:
            print(OVER + str(self.__numero_de_libros))


    def obtener_libro(self, pos):
        '''dada una posición nos devuelve el libro que se encuentra en esa posición dentro de la lista'''
        if self.__valida_posicion(pos):
            return self.__lista_libros[pos-1]
        else:
            print(OVER + str(self.__numero_de_libros))


    def busca_libro(self, cadena):
        '''recibe una cadena y busca el libro que la contenga en su título.
        Si lo encuentra devuelve la posición que ocupa en al lista. Si no, devuelve -1'''
        indice = -1
        for i in range(self.__numero_de_libros):
            libro = self.__lista_libros[i].upper()
            cad = cadena.upper()
            if cad in libro:
                indice = i+1
                break
        return indice


    def __str__(self) -> str:
        salida = f'\n*** {self.__numero_de_libros} Libros actualmente en la Lista:\n    --------------------------------\n'
        for i in range(1, self.__numero_de_libros+1):
            salida += f'    n.{i} - {self.__lista_libros[i-1]}\n'
        return salida


    
    def __busca_indice(self, nuevo_libro):
        for i in range(self.__numero_de_libros):
            if self.__lista_libros[i] >= nuevo_libro:
                indice = i
                break
        return indice

    def __valida_posicion(self, pos):
        return pos <= self.__numero_de_libros

# ============================================================

biblio = ListaLibros()
print(biblio)
l1 = 'La isla del tesoro'
l2 = 'El asesinato de Pitágoras'
l3 = 'Amanecer rojo'
l4 = 'El topo'
biblioteca = ListaLibros([l1, l2, l3, l4])
biblioteca.elimina_libro(5)
print(biblioteca)
print(biblioteca.numero_de_libros)
biblioteca.inserta_libro('Cosmos')
print(biblioteca)
print(biblioteca.obtener_libro(2))
biblioteca.elimina_libro(5)
print(biblioteca)
pos = biblioteca.busca_libro('pi')
print(f'Si existe el libro cuyo titulo contine "pi" está en la posición: {pos}')
