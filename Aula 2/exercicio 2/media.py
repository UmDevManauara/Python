nota1 = float(input("Digite a sua primeira nota "))
nota2 = float(input("Digite a sua segunda nota "))
nota3 = float(input("Digite a sua terceira nota "))
media = (nota1 + nota2 + nota3)/3
if media <6:
    print(f"sua media é {media}")
    print ("Reprovado")
elif media >=6 and not media >=8:
    print(media)
    print("Exame final")
else:
    print(media)
    print("aprovado")
