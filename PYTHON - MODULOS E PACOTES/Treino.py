import moeda

valor = float (input("Digite um preço:"))

print(f"A metade de {valor} é: {moeda.metade(valor)}")
print(f"O dobro de {valor} é: {moeda.dobro(valor)}")
print(f"Aumentando o preço em 10% ficará: {moeda.aumentar10(valor, 10)}")
print(f"Diminuindo o preço em 10% ficará: {moeda.diminuir10(valor, 10)}")

