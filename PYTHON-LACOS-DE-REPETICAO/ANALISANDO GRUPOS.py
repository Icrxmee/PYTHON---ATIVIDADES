

c1, c2, c3 = 0, 0, 0 #Starta as variáveis com 0 previamente.

while True: 
    
    i = int ( input ("Digite a idade:"))
    s = " " #Faz o While interno rodar.

    while s not in "MF": #Roda de imediato porquê "s" começa sem nada atribuído.
        
        s = str ( input ("Digite o sexo [M/F]:")).strip().upper()[0] #Padroniza o input para maiusculo e só considerar a primeira letra.
    
    if i >= 18: #Se a pessoa em questão da volta do laço tiver 18 anos ou mais, soma mais 1.
       c1 += 1
    
    if s == "M": #Se a pessoa em questão da volta do laço for "Masculino", soma mais 1.
       c2 += 1
       
    if s == "F" and i >= 20: #Se a pessoa em questão da volta do laõ for uma mulher com mais de 20 anos, soma mais 1
          c3 += 1

    r = " " #Faz esse outro While rodar de imediato por não ter nada atribuído à variável previamente.
    
    while r not in "SN": #Roda até o usuário escrever corretamente o que deseja.

     r = str ( input ( "Deseja continua?: ")).strip().upper()[0]

    if r == "N": #Encerra se a escolha for "Não"
       break


print(f"Total de pessoas com mais de 18 anos {c1}.") 
print(f"Ao todo temos {c2} homens cadastrados")
print(f"Possuímos {c3} de mulheres com mais de 20 anos")

