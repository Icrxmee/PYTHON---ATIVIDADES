def ficha (j= '<Desconhecido>', g= 0): # Declaro previamente que os parâmetros possuem esses valores.

    print(f"O jogador {j} fez {g} gol(s)") 

n = str(input("Digite um nome:")) 
g = str(input("Digite a quantidade de gols: "))

if g.isnumeric(): # Se na variável "g" o user tiver escrito algo, ele vai analisar se esse algo é numérico e converter.
    g = int(g)
else: # Se não, ele apenas atribui valor 0
     g = 0

if n.strip() == "": # Se nãoa tiver escrito o nome, apenas chama a função dando o valor dos gols.
    ficha(g=g) 
else: # Se tiver nome, chama a função dando ambos valores.
    ficha(n, g)