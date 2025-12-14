def metade (n = 0):
  res = n / 2
  return res 

def dobro(n = 0):
    res = n * 2
    return res 

def aumentar10(n = 0 , f = 0):
   res = n + (n * f / 100)
   return res

def diminuir10(n = 0, f = 0):
   res = n - (n * f / 100)
   return res

def moeda(p=0, m='R$'):
   return f'{m}{p:.2f}'.replace('.',',') 

def escolha():

    while True:
    
      n = input("Deseja continuar [S/N]: ").strip().upper()

      if n in ('S', 'N'):
            return n
                
      else:
            print("ERRO!!! TENTE NOVAMENTE")
         
         
