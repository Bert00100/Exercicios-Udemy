contador_total=0
indent_1=0
indent_2=0
indent_3=0
indent_4=0

ind_cod=int(input("Digite o codigo do mouse: "))

while ind_cod != 0:
#tipo de defeito
    print("1 - Necessidade de esfera.")
    print("2 - Necessidade de limpeza.")
    print("3 - Necessidade troca de cabo ou conector.")
    print("4 - Quebrado ou inutilizado.")

    defeito=int(input("Informe o defeito: "))
#quantidade
    if defeito == 1:
        indent_1 = indent_1+1
    elif defeito == 2:
        indent_2 = indent_2+1
    elif defeito == 3:
        indent_3 = indent_3+1
    elif defeito == 4:
        indent_4 = indent_4+1
    contador_total = contador_total + 1 

    ind_cod=int(input("Digite o codigo do mouse: "))

p1= indent_1 / contador_total * 100
p2= indent_2 / contador_total * 100
p3= indent_3 / contador_total * 100
p4= indent_4 / contador_total * 100

print("Defeitos                Quantidade     Persentual")
print(f"1 -                        {indent_1}           {p1}%")
print(f"2 -                        {indent_2}           {p2}%")
print(f"3 -                        {indent_3}           {p3}%")
print(f"4 -                        {indent_4}           {p4}%")