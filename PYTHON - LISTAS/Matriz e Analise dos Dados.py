List = [[0, 0, 0], [0, 0, 0], [0, 0, 0]] # Lista da Matriz com as listas secundárias já estabelecidas.
soma = maior = coluna = 0

for l in range (0,3): # FOR para as linhas

    for c in range (0, 3): # FOR para as colunas

        List[l][c] =  int( input(f"Digite um valor para [{l}, {c}]")) # Armazena os valores nas posições corretas dentro da matriz.

print("-=-" * 30)

for l in range (0, 3): 

    for c in range( 0, 3):
        print(f"[{List[l][c]}]", end="") # Faz com que retorne no terminal os dados posicionados.
        
        if List[l][c] % 2 == 0: # Vai averiguar cada valor das,linhas e colunas. Se for PAR, eles somam.
            soma += List[l][c]

    print()

print("-=-" * 30)
print(f"A soma dos valores PARES é: {soma}")

for c in range(0, 3): # FOR para averiguar os 3 valores da terceira COLUNA e somá-los.
    coluna += List[c][2] 

print(f"A soma da TERCEIRA COLUNA é: {coluna}")

for l in range (0, 3): # FOR para averiguar os 3 valores da segunda LINHA e somá-los.

    if l == 0:
        maior = List[1][l] # Atualiza com o valor da coluna dentro dessa linha.

    elif List[1][l] > maior:
        maior = List[1][l] # Atualiza com o valor da coluna dentro dessa linha.

print(f"O maior VALOR da SEGUNDA LINHA é: {maior}")