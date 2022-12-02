numero=int(input("Digite um numero: "))

if numero%2==0 and numero>0:
    print(f"{numero} é par e pisitivo")
elif numero%2==0 and numero<0:
    print(f"{numero} é par e negativo")
elif numero%2==1 and numero<0:
    print(f"{numero} é impar e negativo")
elif numero%2==1 and numero>0:
    print(f"{numero} é impar e positivo")