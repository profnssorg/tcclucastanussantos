x = int(input("Quantos km deseja percorrer?"))
if x <= 200:
    preço = x*0.5
    print("a passagem vai custar %5.2f" %preço)
else:
    preço = x*0.45
    print("a passagem vai custar %5.2f" %preço)
