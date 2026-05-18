from datetime import date
ano = int(input("Que ano quer analisar? Coloque e para analisar o ano atual"))
if ano == 0:
ano date.today().year
bissexto ano % 4
if bissexto and ano%1000 or ano% 4000:
print("o ano {} é bissexto".format(ano))
else:
print("o ano {} não é bissexto".format(ano))
