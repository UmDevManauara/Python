N = int
p = 0
par = 0
impar = 0
while N != 0:
    N = int(input("Digite um numero: "))
    if N != 0:
        if N % 2 == 0:
                print(f"{N} é par")
                par = par + 1
        else: 
                print(f"{N} é impar")
                impar = impar + 1

print("Numero 0 encontrado, fim do programa")
print(f"a quantidade de pares foi {par} e a quantidade de impares foi {impar}")