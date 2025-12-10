def Notas(*n, sit=False): #Vai receber uma lista com notas e inicialmente não mostrar a situação do aluno.

    Dict = {} # Vai armazenar num dicionário dados com base nas notas.

    Dict['Total'] = len(n)
    Dict['Maior Nota'] = max(n)
    Dict['Menor Nota'] = min(n)
    Dict['Media'] = sum(n) / len(n)

    if sit: # Vai averiguar a situação do aluno e guardar no dicionário

        if Dict["Media"] >= 7:
            Dict["Situação"] = 'Aprovado'

        if Dict['Media'] >= 5:
            Dict['Situação'] = 'Recuperação'
        
        if Dict['Media'] < 5:
            Dict['Situação'] = 'Reprovado'
    
    return Dict # Returna o dicionário pronto.


List = [] # Declarando a lista.

while True:

    n = float(input("Digite um valor"))
    List.append(n) # Guarda os valores na lista.

    c = str(input("Deseja continuar[S/N]:")).upper()[0] # Decide se deseja continuar.

    if c == "N":

        break

c = str(input("Deseja mostrar a situação[S/N]: ")).upper()[0] # Decide se deseja mostar a situação.

if c == "S":

    List=Notas(*List, sit=True)

else:

    List=Notas(*List)

print(List) # Inves de printar a lista, vai printar o dicionário.