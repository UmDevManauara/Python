n = int(input("Digite o numero a ser fatorado "))
fat = 1
if n < 0:
    print("Não existe fatorial de numero negativo")
else:
    for i in range(1,n + 1,+1):
        fat *= i
        print(fat)
print(f"o fatorial de {n} é {fat}")