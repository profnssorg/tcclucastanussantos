def lê_número(arquivo):
    while True:
        número = arquivo.readline()
        if número == "":
            return None
        if número.strip()!="":
            return int(número)

def escreve_número(arquivo,n):
    arquivo.write("%d\n" % n);


pares = open("pares.txt","r")
ímpares = open("ímpares.txt","r")
pares_ímpares = open("pareseimpares.txt","w")
npar = lê_número(pares)
nímpar = lê_número(ímpares)
while True:
    if npar == None and nímpar == None: 
        break
    if npar != None and (nímpar==None or npar<=nímpar):
        escreve_número(pares_ímpares, npar)
        npar = lê_número(pares)
    if nímpar != None and (npar==None or nímpar<=npar):
        escreve_número(pares_ímpares, nímpar)
        nímpar = lê_número(ímpares)

pares_ímpares.close()
pares.close()
ímpares.close()
