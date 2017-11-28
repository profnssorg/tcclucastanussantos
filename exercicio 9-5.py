pares = open("pares.txt","r")
saída = open("pares_invertido.txt","w")

L = pares.readlines()
L.reverse()
for l in L:
    saída.write(l)

pares.close()
saída.close()
