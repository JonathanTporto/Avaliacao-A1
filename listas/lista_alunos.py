alunos = []
quant = int(input("Quantos alunos deseja cadastrar? "))

for i in range(quant):
    nome = input(f"Digite o nome do aluno {i+1}: ")
    alunos.append(nome)

print("Lista de alunos cadastrados:")
for nome in alunos:
    print("-", nome)
