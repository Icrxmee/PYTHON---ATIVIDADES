print("--" * 15)
print ("BANCO".center(30))
print("--" * 15)

v = int ( input("Digite quanto você deseja sacar:"))
t = v 

ced = 50
tced = 0

while True:

    if t >= ced:
        t -= ced
        tced += 1
    
    else:

        if tced > 0:

            print (f"Total de {tced} cédulas de R${ced}")
        
        if ced == 50:
            ced = 20
        
        elif ced == 20:
            ced = 10

        elif ced == 10:
            ced = 1
        tced = 0
        
        if t == 0:
            break

print("--" * 15)
print("VOLTE SEMPRE".center(30))