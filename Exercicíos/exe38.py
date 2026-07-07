primeiro = int(input("Primeiro termo: "))
razao = int(input("Razao: "))
decimo = primeiro + 10 * razao 
for c in range (primeiro, decimo, razao):
    print(f"{c}", end=" -> ")
print("acabou")
