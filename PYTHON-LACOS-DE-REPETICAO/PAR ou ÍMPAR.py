from random import randint

v = 0 #Variável de controle

while True: #Começa o laço infinito 

    p = int ( input("Digite um número:")) #Número pelo user
    c = randint(0, 10) #Sistema randomiza um número de até 10
    t = p + c 
   

    e = ' ' #Faz o While interno rodar.

    while e not in 'PpIi': #Uma espécime de tratamento de erro. Enquanto não for inputado o valor correto, ele não finaliza ou continua.

        e = str( input ("ímpar ou Par: ")).strip().upper()[0] #Formata a escolha do usuário para um padrão de somente a primeira letra e maiúscula.

    print (f"Você jogou {p} e o computador jogou {c}, total de: {t}") #Retorna o resultado das escolha tanto do usuário quanto do sistema.

    if e == 'P': #Todo o cálculo para retornar quantas vitórias o usuário teve até o sistema parar.
        if t % 2 == 0:
            print ("Você ganhou")
            v += 1
        else:
            print("Você perdeu")
            break

    elif e == 'I':
        if t % 2 == 1:
            print ("Você ganhou")
            v += 1
        
        else:
            print("Você perdeu")
            break
    
    print("Vamos jogar novamente...")


print(f"Você ganhou {v}") #Retorna o número de vitórias.