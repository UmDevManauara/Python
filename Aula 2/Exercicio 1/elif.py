num = int(input("entre com sua  idade "))
if num <= 13: 
    print ("Você é criança")
elif num <18:
    print("Você é adolescente")
    if num >=16 and num < 18:
        print ("Voto opcional")
elif num <60:
    print("Você é Adulto")
    print ("Pode Dirigir")
    print ("Voto obrigatorio Votar")
else:
    print ("Você é Idoso")
    print ("Não pode dirigir")
    print ("Voto opcional")