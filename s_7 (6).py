maior=0
n=int(input("Digite um numero e quando quiser digite 0 para parar "))
while n > 0:
    if n>maior:
        maior=n
        n=int(input("Digite um numero e quando quiser digite 0 para parar "))
print(f"O maior numero é {maior}")