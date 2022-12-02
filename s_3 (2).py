#infaltil -a: 5 a 7
#infaltil -b: 8 a 11
#juvenil -a: 12 a 13
#juvenil -b: 14 a 17
#adulto 18

idade=int(input("Digite a sua idade: "))

if idade<=7 and idade<=5:
    print("infaltil a")
elif idade<=11:
    print("infantil b")
elif idade<=13:
    print("juvenil a")
elif idade<=17:
    print("juvenil b")
elif idade<=18:
    print("aldulto")
else:
    print("Voce ainda não pode praticar")