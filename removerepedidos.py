lista = []

def remove_repetidos(lista):
    if lista:
        lista.sort()
        ultimo = lista[-1]
        for i in range(len(lista)-2, -1, -1):
            if ultimo == lista[i]:
                del lista[i]
            else:
                ultimo = lista[i]
    return(lista)

                
remove_repetidos(lista)
