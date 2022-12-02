horas= 10
horas_exedente= 20
e= 0

c=int(input("Informe o codigo: "))
n=int(input("Informe a quantidade de horas trabalhadas: "))

if n > 50:
    e = (n-50)*horas_exedente
    salario=(50*horas)+e
else:
    salario=(n*horas)

print(f"Seu salario {salario}")
print(f"Sua horas exedidas {e}")


