n = int(input ("Digite um numero "))
if n < 0:
    print ("Fatorial nao pode numeros negativos")
elif  n == 0:
    print("Fatorial de 0 é igual a 1")
else:
    num = n
    cont = n
    fatorial = n

    while n > 1:
        n = n -1
        fatorial *= n
    
print (fatorial)
    
 
