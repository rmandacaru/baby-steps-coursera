#esta função ecebe uma frase como parâmetro e devolve uma string com as letras maiúsculas que existem na frase em ordem que aparecem. 

def maiusculas(frases):
    x=''
    for i in frases:
        if ord(i)>= 65 and ord(i)<= 90: #conforme a tabela ASCII, que define os valores dos caracteres
            x= x+i
    return x 

        
    
