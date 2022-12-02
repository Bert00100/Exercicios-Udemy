vet=[]
soma=0
for n in range(0,20):
    num=int(input(f"Digite o numero da posição {n}: "))
    vet.append(num)
    soma= soma+num
print(f"O numeros são: ")
for n in vet:
    print(n)
print(f"E a soma é {soma}")