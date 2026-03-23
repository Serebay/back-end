preço = float(input("Digite o preço do produto:"))
preçodescontado = preço - (preço*5/100)
print("O produto custava:{:.0f}, mas com o desconto de 5% ficará: {:.0f}".format(preço, preçodescontado))
