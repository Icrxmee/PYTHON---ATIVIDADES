n1 = int ( input("Digite o 1° número:"))
n2 = int ( input("Digite o 2° número:"))

t = n1
cont = 1
chosen = 10

while chosen != 0:

    fim = cont + chosen

    while cont < fim:
        
        print (f"-> {t}" )
        t += n2
        cont += 1
    print()
    
    chosen = int ( input("Deseja mostrar mais qunatos termos:"))

print(f"O codigo finalizado teve {cont-1} termos")
    