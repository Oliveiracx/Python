print("Promoção de maças uma dúzia R$1,00 cada e caso compre menos q uma dúzia o valor é R$1,30 cada ")
quantidade = float(input("Quantas maças você deseja comprar? "))
if quantidade >= 12:
    valor_duzia = quantidade*1.00
    print("O preço que você deve para é R${:.2f}".format(valor_duzia))
if quantidade < 11:
    valor_ind = quantidade*1.30
    print("O preço que você deve para é R${:.2f}".format(valor_ind))
