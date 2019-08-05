#função menor_nome(nomes) recebe uma lista de strings com nomes como parâmetro e devolve o nome mais curto presente na lista.
#Ignora os espaços em branco e retorna o nome com a primeira letra maiúscula. 

#Quando houver mais de um nome com o menor comprimento dentre os nomes na lista, a função devolve o primeiro nome com o menor comprimento.


def menor_nome(nomes):
    m=[]
    for i in nomes:
        i=i.strip() #retira os espaços em branco
        i=i.capitalize()# retorna a primeira letra maiúscula
        m.append(i)
    return min(m,key=len) #retorna o menor nome, com critério de número de caracteries 


