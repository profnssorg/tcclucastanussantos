import sys

if(len(sys.argv)!=4): 
    print("\nUso: e09-04.py primeiro segundo saída\n\n")
else:
    primeiro = open(sys.argv[1],"r")
    segundo = open(sys.argv[2],"r")
    saída = open(sys.argv[3],"w")

    for l1 in primeiro:
        saída.write(l1)
    for l2 in segundo:
        saída.write(l2)

    primeiro.close()
    segundo.close()
    saída.close()
