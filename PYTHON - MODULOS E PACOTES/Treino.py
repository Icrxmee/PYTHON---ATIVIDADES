import moeda

valor = float (input("Digite um preço:"))

print(f"A metade de {moeda.moeda(valor)} é: {moeda.moeda(moeda.metade(valor))}")
print(f"O dobro de {moeda.moeda(valor)} é: {moeda.moeda(moeda.dobro(valor))}")
print(f"Aumentando o preço em 10% ficará: {moeda.moeda(moeda.aumentar10(valor, 10))}")
print(f"Diminuindo o preço em 10% ficará: {moeda.moeda(moeda.diminuir10(valor, 10))}")

