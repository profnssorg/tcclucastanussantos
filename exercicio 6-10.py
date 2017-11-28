L = [15,7,27,39]
p = int(input("Digite o valor a procurar (p):"))
v = int(input("Digite o outro valor a procurar (v):"))
x = 0
achouP = -1 achouV = -1
primeiro = 0
while x < len(L):
     if L[x] == p:
         achouP = x
     if L[x] == v:
         achouV = x
     x += 1
if achouP!=-1:
     print("p: %d encontrado na posição %d" % (p, achouP))
else:
     print("p: %d não encontrado" % p)
if achouV!=-1:
     print("v: %d encontrado na posição %d" % (v, achouV))
else:
     print("v: %d não encontrado" % v)
if achouP!=-1 and achouV!=-1:
    if achouP <= achouV:
        print("p foi achado antes de v")
    else:
        print("v foi achado antes de p")
