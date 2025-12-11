t = ("Lápis",1.75,"Borracha",2.00,"Cderno",15.90,"Estojo",25.00,"Transferidor",4.20,
     "Compasso",9.99,"Mochila",120.32,"Canetas",22.30,"Livro",34.00) #Tupla com produto e valor respectivamente.

print("--"*25)
print("Listagem de Preços".center(50))
print("--"*25)

for i in range (0, len(t)): #For par percorrer a quantidade de elementos da Tupla.
    
    if i % 2 == 0: #Se for Par, vai alocar a esquerda do terminal.
        print(f"{t[i]:.<30}", end="")
    else: #Se for Impar, vai alocar a direita.
        print(f"R$`{t[i]:>7.2f}")