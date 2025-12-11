from random import randint 

n = (randint(1, 10), randint(1,10), randint(1,10),randint(1,10),randint(1,10)) #Randomiza vários valores dentro da tupla


print (f"Os números sorteados foram: {n}") 
print (f"O maior número foi:{max(n)}") #Puxa o maior valor randomizado
print (f"O menor número foi:{min(n)}") #Puxa o menor valor randomizado