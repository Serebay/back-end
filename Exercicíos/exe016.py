aluguel = int (input("A quantos dias está com o carro?"))
km = float(input("Quantos kilometros foram rodados?"))
kmp = km*0.15
aluguelp = aluguel*60
total = kmp + aluguelp
print(f"O aluguel de {aluguel} dias é equivalente a: {aluguelp}R$, Ao rodar {km}km devera ser pago: {kmp}R$. O total a pagar será {total}.")
