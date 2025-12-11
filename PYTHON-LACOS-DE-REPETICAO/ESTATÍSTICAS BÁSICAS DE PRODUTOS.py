print("--" * 10)
print("SUPERMERCADO")
print("--" * 10)

T1 = T2 = M = 0
p = " "
cont = 0

while True:
    
    produto = str ( input("Qual o nome do produto:")) #User declara um nome.
    valor = float ( input("Qual o valor do produto:")) #User declara um valor.
    T1 += valor #A soma de todos os valores 
    cont += 1 #Contador "starta"

    if cont == 1: #Condicional para analisar o menor valor e o produto respectivo a esse valor.
        M = valor
        p = produto
    
    else:
        if valor < M: #Se o novo valor do novo produto for menor que o anterior guardado, o sistema atualiza.
            M = valor
            p = produto

    if valor > 1000: #Verifica se o valor do produto do laço em questão custa mais que "1000" reais. Se for o caso, ele soma + 1
        T2 += 1
    
    r = " " #Faz o While interno rodar.
    
    while r not in "SN": #Usuário deve escrever "Sim(S)" ou "Nao(N)" para continuar.

        r = str ( input("Deseja continuar [S/N]:")).strip().upper()[0]

    if r == "N":
        break
   
print(f"O TOTAL DA COMPRA É DE: {T1}")
print(F"O TOTAL DE PRODUTOS COM VALOR A CIMA DE 1000 REAIS É DE:{T2}")
print(f"O produto mais barato é {p} e ele custa {M}")

