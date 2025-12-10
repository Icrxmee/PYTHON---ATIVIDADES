from random import randint
from time import sleep

def sorteio(lista): # Uma função que vai randomizar 5 valores de 1 a 10 em uma lista (num)

    print("Sorteando 5 Valores da Lista:", end=" ")
    
    for cont in range (0, 5):
        n = randint(1, 10)
        lista.append(n)

        print(f"{n}", end=" ", flush=True)
        sleep(0.5)
    
    print("PRONTO!!!")


def somaPar(lista): # Uma função que vai averiguar cada valor ímpar e par da lista, e somá-los separadamente.

    par = 0
    impar = 0

    for i in lista:

        if i % 2 == 0:
            par += i

        if i % 2 == 1:
            impar += i
            
    
    print("Calculando...")
    sleep(2)
    print(f"A soma de todos os valore PARES da lista é: {par}")
    print(f"A soma de todos os valores ÍMPARES da lista é: {impar}")




num = [] # Declarando a lista para receber os valores.
sorteio(num) # Chamando a função sorteio().
somaPar(num) # Chamando a função somaPar().