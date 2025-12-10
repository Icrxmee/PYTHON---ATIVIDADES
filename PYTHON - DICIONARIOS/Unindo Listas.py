List = []
Dict = {}
soma = media = 0


while True: # Whilw principal.

    Dict.clear() # Toda vez que os dados principais rodarem mais uma vez, o dicionário é limpado.

    Dict['Nome'] = str (input("Digite o nome da pessoa: "))

    while True: # Tratamento de erro para caso o usuário escreva algo além de "F" ou "M"
        
        Dict['Sexo'] = str (input("Digite o sexo da pessoa: ")).upper()[0] 

        if Dict['Sexo'] in 'MF':

            break
        
        else:
            
            print("ERRO!!! DIGITE APENAS M OU F.")

    Dict['Idade'] = int (input("Digite a idade da pessoa: ")) 
    
    soma += Dict["Idade"] # Somador de todas as idades inputadas
    
    List.append(Dict.copy()) # Adicona tudo inputado até agora á uma Lista sem criar vínculo com o Dicionário.

    while True: # Tratamento de erro para caso o usuário escreva algo além de "S" ou "N"

        c = str (input("Deseja conitnua [S/N]: ")).strip().upper()

        if c in "SN":

            break

        else:
            
            print("ERRO!!! RESPONDA S OU N.")

    if c == "N":

        break # Finaliza do While principal.

media = soma / len(List) # Calcula a media de idades.

print(f"Ao todo temos {len(List)} pessoas cadastradas.") # Retorna a quantiade de pessoas cadastradas.
print(f"A media de idade é de {media:5.2f} anos.") # Retorna a media de idades.

print(f"As mulheres cadastradas foram", end=': ') # Retorna todas as mulheres cadastradas.
for i in List: # Vai averiguar todos os dicionários na lista. Aquele que a key "Sexo" tiver valor "F", vai retornar no terminal.
    
    if i['Sexo'] in 'F':

        print(f'{i["Nome"]}', end=', ')
print()


print('Lista de pessoas que estão acima da média: ', end=" ") # Retorna todas as pessoas acima da média de idade.
for i in List: # Mesma coisa da situação anterior. Vai percorrer cada dicionário, e vai retornar os dados das pessoas acima da média de idade.

    if i['Idade'] >= media:
        print('     ')

        for k, v in i.items():

            print(f"{k} = {v}:", end=" ") 
        print()

print("ENCERRADO!!!")   