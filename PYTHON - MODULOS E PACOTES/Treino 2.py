import moeda
from time import sleep

while True:

    valor = float (input("Digite um preço:"))
    sleep(1)

    moeda.resumo(valor, 20, 50)
    sleep(1)
 
    if moeda.escolha() == 'N':
        break

    print()
print("OBRIGADO!!! ATÉ A PRÓXIMA")