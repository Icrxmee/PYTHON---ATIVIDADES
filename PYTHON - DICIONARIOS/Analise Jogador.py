Dict = {}
List = []

Dict['Nome'] = str  (input("Digite o nome do jogador: ")) # Armazena o nome no dicionário.
partidas = int (input("Digite quantas partidas ele jogou:")) # Uma variável para declarar a quantidade de partidas

for i in range (partidas): # O laço vai rodar a quantidade de partidas. 

    List.append(int (input(f"Quantos gols ele fez na {i+1}° partida: "))) # A cada volta é armazenado quantos gols foram feitos em cada partida na Lista. 
    
    Dict['Gols'] = List # Salva a Lista toda no dicionário
    Dict['Total_de_Gols'] = sum(List) # Salva a soma total dos valores da Lista no dicionário

print("-=-" * 40)
print(Dict)
print("-=-" * 40)

print (f"O nome do jogador é: {Dict['Nome']}")
print (f"Ele jogou: {partidas} partidas")
print (f"Ele teve um total de: {Dict['Total_de_Gols']} gols")

print("-=-" * 40)

print (f"O jogador {Dict['Nome']} jogou {partidas} partidas.")

for i, v in enumerate(List): # Enumerate vai olhar cada valor de cada índice da lista (posição da lista) e vai retornar ambos (posição e valor)
    print(f"Na {i+1}° partida ele marcou: {v} gols")