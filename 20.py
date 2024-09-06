valores = []
primeiro = int(input("Digite um valor:"))
valores.append(primeiro)
segundo = int(input("mais um:"))
valores.append(segundo)
terceiro = int(input("último:"))
valores.append(terceiro)
valores.sort()
print("Os número digitados em ordem crescente ficam:{}".format(valores))
