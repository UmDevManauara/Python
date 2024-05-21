num = int(input("entre com sua  idade "))
if num <= 13: 
    print ("Você é criança")
if num <18 and not num <=13:
    print("Você é adolescente")
    print ("Sua idade é menor que 18 anos")
    if num >=16 and num < 18:
        print ("Voto opcional")
if  num >= 18 and not num >= 60:
    print("Você é Adulto")
    print ("Pode Dirigir")
    print ("Voto obrigatorio Votar")
if num >=60:
    print ("Você é Idoso")
    print ("Não pode dirigir")
    print ("Voto opcional")