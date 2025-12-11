import time
List = []

while True:

    name = str (input("Nome:"))
    n1 = float (input("Nota 1:"))
    n2 = float (input("Nota 2:"))

    media = n1 * n2 / 2

    List.append([name, [n1, n2], media]) # Salva na Lista os dados (as notas em uma lista composta para não aparecer no print do boletim).

    c = str (input("Deseja continuar [S/N]:")).strip().upper() 

    if c == "N" :
        break

print(f"{"N.":<4}{"NOME":<10}{"NOTA":>8}") # Visual para o terminal.
print("-=-" * 10)

for i, a in enumerate (List): # FOR vai mostrar o número de cada, o nome do aluno e sua média.

    print(f"{i:<4}{a[0]:10}{a[2]:>8}") # os "a[]" servem para a cada volta do laço na lista, printar os valores nessas posições.

while True:

    opç = int (input("Deseja ver a nota de qual aluno (999 para parar): "))

    if opç <= len(List) - 1: # Se a opção escrita for menor que a quantidade de alunos cadastrados, subtraindo 1 (para puxar o aluno através de seu número).
        
        print(f"As NOTAS do Aluno {List[opç][0]} foram: {List[opç][1]}") # De acordo com a posição, puxa o NOME e NOTAS 
   
    if opç == 999: # FInaliza.
       
        print("FINALIZADO.")
        time.sleep(1)

        break

    else: # Finaliza.

        break

print("VOLTE SEMPRE.")