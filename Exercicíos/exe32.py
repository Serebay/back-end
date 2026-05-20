L1 = float(input("Primeiro lado:"))
L2 = float(input("Segundo lado:"))
L3 = float(input("Terceiro lado:"))
if L1<L2+L3 and L2<L1+L3 and L3<L1+L2:
    print("os numeros acima podem formar um triangulo! iei")
else:
    print("os numeros acima nao podem formar um triangulo! oh no")
