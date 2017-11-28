s=0
x=0
while True:
    v=int(input("Digite um número para somar ou 0 para sair:"))
    if v==0:
        break
    s=s+v
    x=x+1
print("foram digitados %f números" %x)
print("A soma deles é %f" %s)
print("média: %f" %(s/x))
