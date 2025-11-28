idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("Entrada permitida. Bem-vindo ao evento!")
elif idade >= 16:
    print("Entrada permitida apenas com responsável.")
else:
    print("Entrada não permitida. Evento exclusivo para maiores de 16 anos.")
    