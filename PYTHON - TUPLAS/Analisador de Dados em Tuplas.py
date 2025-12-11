t = () #Tuplas
t1 = ()

for i in range (4): #Laço para rodar 4 vezes

    v = int ( input(f"Digite o {i+1}° número: ")) 
    t += (v,) #Forma para atribuir um valor a uma tupla (uma "gambiarra", pois tuplas são imutáveis)

    if v % 2 == 0: 

        t1 += (v,) 
         

print (f"Você digitou os números: {t}")
print (f"O número 9 apareceu {t.count(9)} vezes") # Retorna quantas vezes o valor "9 aparece"
print (f"O número 3 aparece na posição {t.index(3)}") # Retorna qual index (posição) do valor "3"
print (f"Os números {t1} são pares") 