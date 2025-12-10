Locadora = [] # Declarando LISTA para agrupar os DICIONARIOS.
Filmes = {} # Declarando o DICIONARIO base para agrupar as keys e valores.

while True:

    Filmes['Nome'] = str(input("Digite um nome de um Filme:")) # Declarando a key 'Nome' e já atribuindo um valor.
    Filmes['Data'] = int(input("Digite sua data de lançamento:")) # Declarando a key 'Data' e já atribuindo um valor.
    Locadora.append(Filmes.copy()) # Salvando na lista sem criar conexão (através do .copu())

    c = str (input("Deseja adicionair mais um [S/N]:")).strip().upper() 

    if c == 'N':

        break

for i in Locadora:
    
    print(f"O nome do filme é {i['Nome']} e sua data de lançamento é {i['Data']}") # Printa na tela os valores das keys 'Nome' e 'Data'