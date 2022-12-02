p=float(input("Digite quantos quilos de peixo João pescou: "))

if p > 50:
    e = p
    m = 4
    print(f"munta {m}")
    print(f"exesso {e}")
    print(f"O valor que João devera pagar {e*m}")
else:
    m = 0
    e = 0
    print(f"munta {m}")
    print(f"exesso {e}")

