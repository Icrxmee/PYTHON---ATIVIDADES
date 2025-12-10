from datetime import datetime # Importando datetime para puxar o ano atual.

Dict = {}
ano_atual = datetime.now().year # Puxando o ano atual.

Dict['Nome'] = str (input("Digite o nome do indivíduo:"))
Dict['Ano_de_Nascimento'] = int (input("Digite seu ano de nascimento:"))
Dict['Carteira'] = int(input("Digite sua carteira de trabalho (0 não tem):"))

idade = ano_atual - Dict['Ano_de_Nascimento'] # Cria a variável "idade" para armazenar a idade do indivíduo.

if Dict['Carteira'] != 0: # Se ele tiver uma carteira de trabalho, será inputado mais 2 chaves e valores ao dicionário.

    Dict['Ano_de_Contratação'] = int (input("Digite o ano de contratação"))
    Dict['Salario'] = int (input("Digite seu salário: "))
    
    ano_trabalhados = ano_atual - Dict['Ano_de_Contratação'] # Cálculo para averiguar com quantos anos o indivíduo vai se aposentar
    anos_para_aposentar = 35 - ano_trabalhados # Aqui serve também para dizer quantos anos faltam para se aposentar. 
    aposentadoria = idade + anos_para_aposentar # Idade que ele vai se aposentar.


else: # Se o indivíduo não tiver carteira de trabalho, apenas retorna os valores já cadastrados. 

    print(f"O nome do cidadão é: {Dict['Nome']}")
    print(f"A idade dele(a) é: {idade} anos")
    print(f"O número de sua carteira de trabalho é: {Dict['Carteira']}")

print("-=-" * 15)

print (f"O nome do cidadão é: {Dict['Nome']}")
print (f"A idade dele(a) é: {idade}")
print (f"O número de sua carteira de trabalho é: {Dict['Carteira']}")
print (f"Sua contrataçaõ foi em: {Dict['Ano_de_Contratação']}")
print (f"Seu salário é de: {Dict['Salario']}")
print (f"Ele(a) vai se aposentar com: {aposentadoria} anos")