def metade (n = 0, formato = False):
   res = n / 2
  
   return res if not formato else moeda(res)


def dobro(n = 0, formato = False):
   res = n * 2
    
   return res if not formato else moeda(res)


def aumentar10(n = 0 , f = 0, formato = False):
   res = n + (n * f / 100)
   
   return res if not formato else moeda(res)


def diminuir10(n = 0, f = 0, formato = False):
   res = n - (n * f / 100)
   
   return res if not formato else moeda(res)


def moeda(p=0, m='R$'):
   return f'{m}{p:.2f}'.replace('.',',') 

def resumo(p=0, a= 10, d= 10):
    
    print("-" * 30)
    print("RESUMO DO VALOR".center(30))
    print("-" * 30)
    print(f"Preço analisado: \t{moeda(p)}")
    print(f"O dobro do preço: \t{dobro(p, True)}")
    print(f"A metade do preço: \t{metade(p, True)}")
    print(f"Com {a}% de aumento: \t{aumentar10(p,a,True)}")
    print(f"Como {d}% de reduçaõ: \t{diminuir10(p,d,True)}")
    print("-" * 30)


def escolha():

    while True:
    
      n = input("Deseja continuar [S/N]: ").strip().upper()

      if n in ('S', 'N'):
            return n
                
      else:
            print("ERRO!!! TENTE NOVAMENTE")
         
         
