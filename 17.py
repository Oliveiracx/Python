nota_1 = float(input("Digite sua primeira nota:"))
nota_2 = float(input("Digite sua segunda nota:"))
media = (nota_1+nota_2)/2
print("Sua média é {}".format(media))
if media >= 6:
    print("Parabéns você está aprovado!")
if media < 6:
    print("Sinto muito você está reprovado!")
