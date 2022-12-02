vet=[]

for n in range(0,3):
    num = int(input(f"Digite o numero {n} : "))
    vet.append(num)

vet.reverse()

for p in vet:
    print(p)