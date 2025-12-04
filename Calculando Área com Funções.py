
def area(a, b): # Crio a função para calcular área. ¹

    terreno = (a * b)

    print(f"A área de um terreno de {a}x{b} será: {terreno}") # Após declarar os valores da função, vai realizar o cálculo e retornar o resultado. ³

while True: 

    a = float(input("Digite o comprimento do terreno: "))
    b = float(input("Digite a largura do terreno:"))

    area(a,b) # Após inputar os valores de a e b, puxo a função criada, e declaro que os valores de a e b dela, sejam os valores inputados. ²

    c = str(input("Deseja continuar[S/N]:")).upper()[0]

    if c == "N":

        break
    print( )

    