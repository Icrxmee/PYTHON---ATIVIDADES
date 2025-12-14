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


def escolha():

    while True:
    
      n = input("Deseja continuar [S/N]: ").strip().upper()

      if n in ('S', 'N'):
            return n
                
      else:
            print("ERRO!!! TENTE NOVAMENTE")
         
         
