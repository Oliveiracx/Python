salario_fixo = int(input("Digite seu salário sem o adicional das comissões:"))
vendas = int(input("e agora dgite o valor total de suas vendas:"))
if vendas < 1500:
    comissão_3 = salario_fixo+vendas*0.03
    print("Seu salário com a adição das comissões é de R${:.2f}".format(comissão_3))
if vendas >= 1500:
    passou = vendas-1500
    comissão_5 = salario_fixo+vendas*0.03 + passou*0.05
    print("Seu salário com a adição das comissões é de R${:.2f}".format(comissão_5))
