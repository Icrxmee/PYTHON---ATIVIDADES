Dicionario = {} # Dicionario 

Dicionario['Nome'] = str (input("Digite o nome do aluno:")) # Salva 'Nome' como a key e o nome de fato como o valor.
Dicionario['Media'] = float (input("Digite qual foi a média final: ")) # Salva 'Media' como a key e a media de fato como o valor.

if Dicionario['Media'] >= 7: # Se for maior que 7 é APROVADO. Se for maior que 4 e menor que 7 é RECUPERAÇÃO. Se for menor que 4 é REPROVADO.

    Dicionario['Situação'] = ("Aprovado")

if Dicionario['Media'] < 7 and Dicionario['Media'] >= 4:

    Dicionario['Situação'] = ("De recuperação")

if Dicionario['Media'] < 4:

    Dicionario['Situação'] = ("Reprovado!!!")


print(f"O nome é {Dicionario['Nome']}")
print(f"A média foi {Dicionario['Media']}")
print(f"A situação final do aluno é {Dicionario['Situação']}")