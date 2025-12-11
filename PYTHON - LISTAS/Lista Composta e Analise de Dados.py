List = [] # Lista principal.
l = [] # Lista secundária que vai ficar atualizando a principal com novos dados.
maior = menor = 0 # Variáveis de controle 

while True:

    l.append(str(input("Nome: ")))
    l.append(float(input("Peso: ")))
    
    if len(List) == 0: # If para rodar a condicional se aproveitando que ainda não existe nada salvo na lista principal.
        maior = menor = l[1]
    
    else:

        if l[1] > maior:
            maior = l[1]

        if l[1] < menor:
            menor = l[1] 

    List.append(l[:]) # Append para ir atualizando a lista principal sem criar conexão.
    l.clear() # Limpa a lista secundária apos inserir novos dados.
    
    c = str ( input("Deseja continuar [S/N]:")).strip().upper()

    if c == "N" or c == "Não":
        break

print("-=-" * 30)
print(f"Os dados foram ; {List}")
print(f"Ao todo você cadastrou {len(List)} pessoas.")
print(f"O maior peso foi: {maior} Kg. Peso de ")

for i in List: # Vai percorrer a lista principal, e após achar o índice com maior peso, retorna o nome correspondente.
    if i[1] == maior:
        print(f"{i[0]}")


print(f"O menor peso foi de: {menor} Kg.")

for i in List: # Vai percorrer a lista principal, e após achar o índice com menor peso, retorna o nome correspondente.
    if i[1] == menor:
        print(f"{i[0]}")