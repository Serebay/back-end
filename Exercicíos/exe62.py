resp = "s"
soma = quant = media = maior = menor = 0
while resp in "ss":
    num=int(input("digite um numero:"))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
                maior = num
        if num < menor:
             menor = num
    resp = str(input("quer continuar? [s/n] ")).lower().strip()[0]
media = soma / quant
print(f"voce digitou {quant} numeros e a media foi {media}")
print(f"o maior foi {maior} e o menor foi {menor}")
