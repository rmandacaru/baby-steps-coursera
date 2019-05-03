#Escreva a função maiusculas(frase) que recebe uma frase (uma string)
#como parâmetro e devolve uma string com as letras maiúsculas que existem nesta frase,
#na ordem em que elas aparecem.

#Para resolver este exercício, pode ser útil verificar uma tabela ASCII,
#que contém os valores de cada caractere. Ver https://pt.wikipedia.org/wiki/ASCII

#Dica: Os valores apresentados na tabela são os mesmos devolvidos pela função
#ord apresentada nas aulas.

#maiusculas('Programamos em python 2?')
# deve devolver 'P'

#maiusculas('Programamos em Python 3.')
# deve devolver 'PP'

#maiusculas('PrOgRaMaMoS em python!')
# deve devolver 'PORMMS'

def maiusculas(frases):
    x=''
    for i in frases:
        if ord(i)>= 65 and ord(i)<= 90:
            x= x+i
    return x 

        
    
