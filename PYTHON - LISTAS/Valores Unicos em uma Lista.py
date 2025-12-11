l = []

while True: 

    v = int ( input("Digite um valor:")) 
    print ("Valor adicionado com sucesso...")
    
    if v in l: #Se um número já tiver sido escrito, ele não adiciona.

     print("Numero duplicado. Não irei adicionar...")

    else:    

     l.append(v) 

    c = str ( input("Deseja continuar? [S/N]:")).strip().upper() #Formata para a escolha sair em maiúsculo.

    if c == "N":
        break

print(f"Você digitou os números: {sorted(l)}")