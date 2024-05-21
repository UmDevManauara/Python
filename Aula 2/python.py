#numero é positivo ou negativo
num  = int(input("entre com um numero "))
if num < 0:
    print(f"{num} é negativo")
else: 
    print (f"{num} é positivo")

#numero é par ou impar?
if num % 2 == 0:
    print (f"{num} é par")
else: 
    print(f"{num} é impar")

if num % 2 == 0 and num % 3 == 0:
    print(f"{num} é divisivel por 2 e por 3")
