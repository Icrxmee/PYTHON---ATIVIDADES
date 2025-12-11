l1 = []

while True: 

    l1.append(str(input("Digite um NOME:"))) #Adiciona direto o nome digitado.
    l1.append(int(input("Digite uma IDADE:")))#Adiciona direto a idade digitada.

    c = str ( input("Deseja continuar? [S/N]:")).strip().upper()

    if c == "N" or c == "NÃO":

        break

print(l1) #Retorna a lista com as listas digitadas.