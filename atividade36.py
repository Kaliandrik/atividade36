# Ler uma lista com 4 notas, em seguida
# o programa deve exibir as notas e a
# média.

notas = []

for i in range(1,5):
    nota = float(input("Digite sua nota: "))
    notas.append(nota)

media = sum(notas)/len(notas)

print(f"As notas são: {notas}")
print(f"A média das notas são: {media}")