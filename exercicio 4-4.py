x = float(input("Qual o seu salário?:"))
if x > 1250:
    aumento = x*0.1
    print("O seu aumento será %5.2f" %aumento)
if x <= 1250:
    aumento = x*0.15
    print("O seu aumento será %5.2f" %aumento)
