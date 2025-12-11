somaidade = 0  #Somadores e um acumulador
mediaidade = 0 
maioridadehome = 0
nomevelho = ""
mulher20 = 0

for c in range (1, 5): #Laço de repetição
    
    print (f'---------- {c}° PESSOA ----------') # Dados a serem "Inputados"
    
    nome = str ( input ("Digite o nome: ")).strip()
    idade = int ( input("Digite a idade:"))
    sexo = str ( input("Sexo [F/M]: ")).strip()

    somaidade += idade # Soma para o cálculo da média das idades posterior mente.¹

    if c == 1 and sexo in 'Mm': # Defiinindo o primeiro homem do laço como o mais velho para ser comparado com o resto.
        maioridadehome = idade
        nomevelho = nome

    if sexo in 'Mm' and idade > maioridadehome: # Compara cada homem do laço e definine o com a maior idade "inputada" como mais velho
        maioridadehome = idade
        nomevelho = nome 

    if sexo in 'Ff' and idade < 20: # Soma ao somador (mulher20) sempre que uma mulher tiver menos de 20 anos
        mulher20 += 1

mediaidade = somaidade / 4 # Divisão para a média das idades ²

print (f"A media de idade do grupo é de: {mediaidade}") 
print (f'O homem mais velho tem {maioridadehome} anos e se chama {nomevelho}')
print (f'Temos {mulher20} mulheres menores que 20 anos.')