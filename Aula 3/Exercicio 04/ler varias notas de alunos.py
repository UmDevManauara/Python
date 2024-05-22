qtde_alunos = 0
soma_nota = 0
nota = float(input("Nota: "))
while nota != -1:
    qtde_alunos = qtde_alunos + 1

    soma_nota += nota

    nota = float(input("Nota: "))

media = soma_nota / qtde_alunos
if media >= 8: 
    print ("Media")
    print("Aprovado")
elif media < 4:
    print ("Media")
    print("reprovado ")
else: 
    print (f"media é {media}")
    print("Prova final")