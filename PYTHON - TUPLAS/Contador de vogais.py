t = ("Jose","Pedro","Icaro","Mouta","Macedo")
v = 'aeiou'


for i in t: #For para percorrer cada palavra.
 
    print (f"\nA palavra {i} tem as vogais: ", end="")

    for n in i: #For para percorrer cada letra.

        if n.lower() in 'aeiou': #Joga tudo para minpusculo e analisa se tem vogal.

            print (n, end="") #Diz as vogais que existem em cada palavra percorrida anteriormente.