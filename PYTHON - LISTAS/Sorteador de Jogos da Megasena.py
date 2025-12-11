import random 
import time
Jogos = []


c = int(input("Diga quantos jogos você quer que eu sorteie: "))

print(f"Sorteando {c} jogos")

for i in range (c):

    number = sorted(random.sample(range(1,61),6))
    Jogos.append(number)
    print(f"Jogo {i+1}: {number}")
    time.sleep(1)