from time import sleep

def contador(a , b, c):

    print("-=-" * 20)
    print ("contagem de 1 em 1 até 10")
    sleep(2.5)

    for i in range (1, 11, 1):

        print (f"{i}", end=" ", flush=True)
        sleep(0.5)
    print()
    
    print ("Contagem de 2 em 2 de 10 até 0")
    sleep(2.5)

    for i in range (10, 0, -2):

        print(f"{i}", end=" ", flush=True )
        sleep(0.5)
    
    print("FIM!!!")
    print("-=-" * 20)

    print("CONTAGEM PERSONALIZADA")
    sleep(2)

    if c == 0:
        c = 1

    if a < b:
        for i in range (a, b + 1, c):
            print(i,end=" ", flush=True)
            sleep(0.3)
    
    else:
        for i in range (a, b - 1, -abs(c)):
            print(i, end=" ", flush=True)
            sleep(0.3)
    
    print("FIM!!!")
    print("-=-" * 20)


print("Agora sua vez de personalizar.")
inicio = int(input("Início:"))
fim = int (input("Fim:"))
passo = int (input("Passo:"))
contador(inicio, fim, passo)
