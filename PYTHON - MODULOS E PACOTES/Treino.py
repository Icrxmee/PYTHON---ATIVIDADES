import moeda

while True:

    valor = float (input("Digite um preço:"))

    print(f"A metade de {moeda.moeda(valor)} é: {moeda.metade(valor, True)}")
    print(f"O dobro de {moeda.moeda(valor)} é: {moeda.dobro(valor, True)}")
    print(f"Aumentando o preço em 10% ficará: {moeda.aumentar10(valor, 10, True)}")
    print(f"Diminuindo o preço em 10% ficará: {moeda.diminuir10(valor, 10, True)}")

    
    if moeda.escolha() == 'N':
        break

    print()
print("OBRIGADO!!! ATÉ A PRÓXIMA")