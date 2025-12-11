
n1 = int ( input ("Primeiro Valor:")) # Defino dois valores.
n2 = int ( input ("Segundo Valor:"))

chosen = 0 # Crio uma variável controladora para usá-la posteriormente.

while chosen != 5: # Enquanto não for escolhido 5, o código não para.
    print ('''      [OPÇÕES]
    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] TROCAR VALORES
    [5] SAIR''')
    
    chosen = int ( input ( "Qual sua escolha:")) # Escolher opção.

    if chosen == 1: # Somar ambas variáveis.
        print (f"A soma dos valores {n1} e {n2} será: {n1 + n2}\n")
    
    if chosen == 2: # Multiplica ambas variáveis.
        print (f"A multiplicação dos valores {n1} e {n2} será: {n1 * n2}\n")

    if chosen == 3: # Compara ambas vaiáveis.
        if n1 > n2:
            print(f"O maior valor entre ambos é: {n1}\n")
        
        elif n2 > n1: 
            print(f"O maior valor entra ambos é: {n2}\n")

    if chosen == 4: # Atualizar ambas variáveis.
        n1 = int ( input ("Digite o primeiro valor: ")) 
        n2 = int ( input ("Digite o segundo valor: "))

    if chosen == 5: # Encerrar.
        print("Obrigado, volte sempre.")

    if chosen >= 6: # Verificação de erro
        print("Opção inválida, por favor escreva novamente o que você deseja.\n")

