l = [] 

for i in range (0, 5):
    
    v = int ( input("Digite um valor:"))

    if i == 0 or v > l[-1]: #Se o número digitado for o primeiro ou maior que o último que estiver na lista, ele vai para o final.
        l.append(v)
    
    else: #Se não, vai alocar o número em algum lugar no meio.

        p = 0 

        while p < len(l): #While para rodar enquanto a lista não tiver completa
            if v <= l[p]: #O código vai rodar, e vai averiguar os valores de cada posição e alocar o número inputado antes do número que ele for menor.
                l.insert(p, v)  #Insere o valor na posição.

                break
            
            p += 1 

print ("-=-" * 30)
print (f"Os valores digitados em ordem foram: {l}")