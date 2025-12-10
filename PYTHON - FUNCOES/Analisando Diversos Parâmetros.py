from time import sleep

def maior(* num): # A função vai receber diversos parâmetros.

    cont = maior = 0 # Variáveis acumuladoras.

    print("\nAnalisando os valores...")
    sleep(1)

    for i in num:
        
        print(f"{i}", end=" ", flush=True)
        sleep(0.2)

        if cont == 0: # Analisa qual o maior valor de cada bloco de parâmetros.
            maior = i

        else:
             if i > maior:
                 maior = i
        

        

    print(f"Foram informados {len(num)} valores. O maior deles sendo {maior}") # Possível substituir a variável cont (que seria o contador) pelo len da função.

maior(2, 3, 5, 6, 1, 10, 32, 45, 102, 23, 54)
maior(54, 12, 21, 13, 1, 4)
maior(3, 5, 1, 7, 2, 10, 4)