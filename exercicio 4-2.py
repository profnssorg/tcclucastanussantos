x = int(input("Escreva a velocidade do carro:"))
if x > 80:
    print("você foi multado")
    y = (x - 80)*5
    print("o valor da multa é R$ %5.2f" %y)
if x < 80:
    print("dentro da velocidade permitida")
