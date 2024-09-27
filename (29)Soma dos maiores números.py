valores = []
primeiro = int(input("Primeiro valor:"))
valores.append(primeiro)
segundo = int(input("Segundo valor:"))
valores.append(segundo)
terceiro = int(input("Terceiro valor:"))
valores.append(terceiro)
maior = max((valores))
menor = min((valores))
valores.sort(reverse=True)
maiores_soma = valores[0] + valores[1]
print("A soma dos maiores números digitados é {}".format(maiores_soma))
