from random import shuffle
aluno1 = str (input("Escreva o nome do primeiro aluno: "))
aluno2 = str (input("Do segundo: "))
aluno3 = str (input("O terceiro "))
aluno4 = str (input("O quarto "))
lista = [aluno1, aluno2, aluno3, aluno4]
shuffle(lista)
print("O aluno escolhido foi {}".format(lista))
