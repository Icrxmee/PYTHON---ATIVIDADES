def fatorial(n, show=False): # A função vai receber um valor e mostrar ou não o cálculo do fatorial desse número.

    f = 1 

    for c in range (n, 0, -1): # Cálculo do fatorial
        
        if show: # Se for declarado o show como True, vai mostrar o cálculo
            
            print(f"{c}", end=" ") 
            
            if c > 1:
                print("x", end=" ")
            
            else:
                print("=", end=" ") # Quando o c chegar a 0, não vai printar mais "x", e sim "=" (Apenas estética).

        f *= c

    return f # Retorna o resultado do cálculo.


n = int (input("Digite um valor:")) # Aqui digo qual número quero saber o fatorial.

c = str (input("Deseja mostrar o cálculo [S/N]:")).upper()[0] # Aqui decido se quero ou não ver o cálculo.

if c == "S":
    print(fatorial(n, show=True))
else:
    print(fatorial(n, show=False))