# Primeiro programa
print ("Ola Mundo")

nome = input("Qual seu nome?")

print(f"ola, {nome}, seja bem-vindo")

idade = int(input("Qal a sua idade?"))
if idade <13:
    print ("Criança")
elif idade < 18:
    print('Adolescente')
elif idade < 60:
    print("adulto")
else: 
    print("idoso")