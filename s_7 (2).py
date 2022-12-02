maior=0
menor=0
media=0

for n in range(0,3):
    n = int(input("Digite um numero: "))
    if n > 0:
        if n > maior:
            maior = n
        elif n > menor and menor < maior:
            menor = n
    media = media + n
media=media/3
print(f"O maior numero: {maior}")
print(f"O menor numero é: {menor}")
print(f"A media é: {media}")