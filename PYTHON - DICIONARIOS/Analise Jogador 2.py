Dict = {}
List = []
time = []


while True:

    Dict.clear() # Limpa o dicionário a cada volta.
    List.clear() # Limpa a lista a cada volta.

    Dict['Nome'] = str  (input("Digite o nome do jogador: ")) 
    partidas = int (input("Digite quantas partidas ele jogou:")) 

    for i in range (partidas): # Vai rodar de acordo com o número de partidas.

        List.append(int (input(f"Quantos gols ele fez na {i+1}° partida: ")))  # Salva na lista os gols de cada partida.
        
    Dict['Gols'] = List.copy() # Cria uma key para armazenar todos os gols.
    Dict['Total_de_Gols'] = sum(List) # Soma todos

    time.append(Dict.copy()) #Salva tudo na segunda lista (time) sem criar vínculo com o dicionário.

    while True: # Tratamento de erro para decidir se quer adicionar mais um jogador.
    
        c = str (input("Deseja continuar [S/N]:")).upper()[0]

        if c in "SN":

            break

        else:

            print("ERRO!!! ESCREVA SIM OU NÃO")
        
    if c == "N":

        break

    print("-=-" * 30)

for k, v in enumerate(time): # Retorna cada jogador e seus gols.

    print (f"{k:>3}", end=" ")

    for d in v.values():

        print(f"{str(d):<15}", end=" ")

    print()

print("-=-" * 30)

while True: 

    s = int(input("Mostrar dados de qual jogador [999 para parar]:"))

    if s == 999:

        break

    if s >= len(time): # Se for escolhido para analisar um jogador numa psoição que não existe, retorna um erro.

        print(f"ERRO!!! NÃO EXISTE UM JOGADOR COM ESSE CÓDIGO DE BUSCAR: {s}")

    else:

        print(f"Levantamento do jogador {time[s]['Nome']}:") # Se for escolhido um que existe, puxa o nome, e quantos gols em cada partida.

        for i, g in enumerate(time[s]['Gols']):

            print(f"No jogo {i+1} fez {g}.")
        
    print("-=-" * 30)

print("ENCERRADO!!!")