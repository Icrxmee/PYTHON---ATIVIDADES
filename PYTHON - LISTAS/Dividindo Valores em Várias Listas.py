l1 = [] #Lista principal.

while True: #While para definir quantos valores a lista principal possuirá.

    v = int ( input ("Digite um valor: "))
    l1.append(v)

    c = str ( input ("Deseja continuar [S/N]:")).strip().upper()

    if c == "N" :

        break

l2 = [] #Lista dos números PARES
l3 = [] #Lista dos npumeros IMPARES

for i in l1: #For para alocar cada valor da lista principal em sua devida lista.

    if i % 2 == 0:
        l2.append(i)
    
    elif i % 2 != 0:
        l3.append(i)


print (f"A lista completa é: {sorted(l1)}")
print (f"Os números ÍMPARES são: {sorted(l3)}")
print (f"Os números PARES são: {sorted(l2)}")