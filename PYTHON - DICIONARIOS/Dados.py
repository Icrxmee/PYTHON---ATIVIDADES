from random import randint
from time import sleep
from operator import itemgetter

Dict = {'jogador1': randint(1,6), # Para cada jogador (keys) vai ser atribuido um número de 1 a 6 (value)
        'jogador2': randint(1,6), 
        'jogador3': randint(1,6),
        'jogador4': randint(1,6),}

ranking = list() 

for k, v in Dict.items(): # Vai printar as keys e os values do dicionarios

    print(f"{k} tirou {v} no dado")
    sleep(1)

ranking = sorted(Dict.items(), key= itemgetter(1), reverse= True) # Tornamos o dicionario numa TUPLA. Com o itemgetter(1) 
                                                                  # declaramos que queremos usar para comparar o valor na posição "1" ou seja, quanto o jogador tirou.
                                                                  # Valor "1" pois como tornamos em uma tupla e eles estão em pares, então o valor do dado fica na posiçaõ 1.
                                                                  # Reverse= True para organizar do maior para o menor.

for k, v in enumerate(ranking): # Vai printar organizado agora de maior para o menor.
    
    print(f"{k+1}° lugar: {v[0]} com {v[1]}.")
    sleep(1)