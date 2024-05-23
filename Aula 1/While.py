
# 1 + 2 + 3 + 4 + 5 + 6...

n = int(input("N: "))
i = n
somaWhile = 0
while i > 0:
    somaWhile = somaWhile + i
    i = i - 1
print(f"A soma é {somaWhile}")
