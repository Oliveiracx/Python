print("                          Calculadora de Salário")
print()
s_fixo = int(input("Digite seu salário fixo:R$"))
vendas = int(input("Quantos carros você vendeu esse mês:"))
valores_v = int(input("Qual o valor total das suas vendas nesse mês:"))
ganho_v = valores_v*0.05
print("-"*75)
print("Você vendeu {:.2f} carros suas vendas somam R${:.2f} e seu salário fixo antes da comissão é R${:.2f}".format(vendas, valores_v, s_fixo))
comissão_pv = vendas*700
comissão = comissão_pv+ganho_v
valor_pv = ganho_v/vendas
print("Você recebe R${:.2f} por cada venda".format(valor_pv))
salário_final = comissão+s_fixo
print("-"*75)
print("Seu salário final é de R${:.2f}".format(salário_final))
