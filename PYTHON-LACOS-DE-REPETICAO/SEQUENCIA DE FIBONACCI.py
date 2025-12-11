n = int ( input ("Digite o 1° valor:"))

a, b = 0, 1

for i in range (n):
    print(a, end=" ")
    a, b = b, a + b

