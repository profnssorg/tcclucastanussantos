import sys


if(len(sys.argv)!=4):     print("\nUso: e09-02.py nome_do_arquivo inicio fim\n\n")
else:
    nome = sys.argv[1]
    inicio = int(sys.argv[2])
    fim = int(sys.argv[3])
    arquivo = open(nome,"r")
    for linha in arquivo.readlines()[inicio-1:fim]:
        print(linha[:-1]) 
    arquivo.close()
