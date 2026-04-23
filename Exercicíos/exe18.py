catetoop = float(input('Comprimento do cateto oposto: '))
catetoad = float(input('Comprimento do cateto adjacente: '))
hipotenusa = (catetoop ** 2 + catetoad ** 2) ** (1/2)
print(f'A hipotenusa vai medir {hipotenusa:.2f}')
