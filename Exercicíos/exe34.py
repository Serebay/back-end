n1 = int(input("Qual é o número?: "))
print("Digite 1 para binario")
print("Digite 2 para exadecimal")
print("Digite 3 para octal")
escolha = int(input("Sua opção: "))
if escolha == 1:
    print("{} convertido para binario é igual a {}".format(n1,bin(n1)))
elif escolha == 2:
    print("{} convertido para hexadecimal é igual a {}".format(n1,hex(n1)))
elif escolha == 3:
    print("{} convertido para octal é igual a {}".format(n1,oct(n1)))
else: 
    print("Opçao invalida, escreva os numeros certo.")
