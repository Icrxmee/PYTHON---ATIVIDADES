l1 = []

for i in range (0,6): 
    v = int ( input(f"Digite um valor na posição {i}:"))
    l1.append(v) #Adiciona todos os valores à lista criada.



print("-=-" * 15)
print(f"Você digitou os números: {l1}") #Printa os valores adicionados.

mx = max(l1) #Analisa qual valor é o maior.
l2 = [] #Uma segunda lista para as posições desse maior valor.

for i, v in enumerate(l1): #FOR que analisa a posição e o valor dos elementos da lista.
    if v == mx: #Quando o FOR percorrer o maior valor, ele adiciona a posição dele na lista.
        l2.append(i) 

print(f"O maior valor digitado foi {mx} na ou nas posições {l2}...") #Printa o maior valor e suas posições

mn = min(l1) #Analisa qual valor é o menor.
l3 = [] #Uma terceira lista para as posições desse menor valor.

for i, v in enumerate(l1): #FOR que analisa a posição e o valor dos elementos da lista.
    if v == mn: #Quando o FOR percorrer o menor valor, ele adiciona a posição dele na lista 
        l3.append(i)

print(f"O menor valor digitado foi {mn} na ou nas posições {l3}...") #Printa o maior valor e suas posições.