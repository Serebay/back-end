altura = float(input("Digite a altura da parede:"))
largura = float(input("Digite a largura da parede:"))
area = altura*largura
tinta = area/2
print("A parede com {:.0f}x{:.0f} tem uma area de {:.0f}, e seram utilizado {:.0f} litros de tinta.".format(altura,largura,area,tinta))
