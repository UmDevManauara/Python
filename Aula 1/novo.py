# Primeiro programa
print ("Ola Mundo")

nome = input("Qual seu nome?")

print(f"ola, {nome}, seja bem-vindo")

idade = int(input("Qual a sua idade?"))
if idade <13:
    print ("Criança")
elif idade < 18:
    print('Adolescente')
elif idade < 60:
    print("adulto")
else: 
    print("idoso")

print (int(4/2))

print (round(2/3,3))
x = 1/7

print(f"{x:.50f}")
