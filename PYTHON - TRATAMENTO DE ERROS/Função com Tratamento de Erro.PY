import sys

def leiaINt(a):

    while True:
        
        try:
            
            n = int(input(a))

        except (ValueError, TimeoutError):

            print("ERRO: Por favor, digite um número inteiro válido!!!")
            continue

        except (KeyboardInterrupt):

            print("ERRO: Usuário interrompeu.")
            sys.exit()
        
        else:
            return n
        
def leiaFloat(a):

    while True:

        try:

            n = float(input(a))
        
        except (ValueError, TypeError):

            print("ERRO: Por favor digite um número real válido!!!")
            continue

        except (KeyboardInterrupt):
            print("ERRO: Usuário interrompeu. ")
            sys.exit()

        else:

            return n

a = leiaINt("Digite um número inteiro: ")
b = leiaFloat("Digite um número real: ")    

print(f"O valor inteiro informado foi: {a}")
print(f"O valor real informado foi: {b}")


