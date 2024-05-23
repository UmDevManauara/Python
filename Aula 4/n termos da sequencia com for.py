n = int(input("Digite um valor "))

if n < 0:
    print("Valor nao pode ser negativo")
else:
   prim_termo = 0
   seg_termo = 1
   termos = 2
for i in range (1, n +1,1):
    print(prim_termo, end = " ")
    prox_termo = prim_termo + seg_termo
    prim_termo = seg_termo 
    seg_termo = prox_termo
    termos += 1