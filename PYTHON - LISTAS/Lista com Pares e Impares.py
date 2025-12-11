List = [[], []] # Lista principal com dois índices para os valores pares e impares.

for i in range(0, 7):

    number = int ( input("Digite um número:"))

    if number % 2 == 0:
        List[0].append(number) # Salva o valor par no primeiro índice da lista principal.
    
    elif number % 2 == 1:
        List[1].append(number) # Salva o valor impar no segundo índice da lista principal.
    
print ("-=-" * 15) # Retorna de maneira crescente e separadamente os valores pares e impares.
print (f"Os valores pares digitados foram: {sorted(List[0])}") 
print (f"Os valres ímpares digitados foram: {sorted(List[1])}")