s="AABBEFAATT"
p=0
while(p>-1):
    p=s.find("BE",p)
    if p>=0:
        print("Posição: %d" %p)
        p+=1
