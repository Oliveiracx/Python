horas_trabalhadas = int(input("Quantas horas totais foram trabalhadas esse mês ? "))
horas_semana = horas_trabalhadas/4
print("Você trabalhou por {} Horas por semana".format(horas_semana))
salario = (horas_trabalhadas)*10
if horas_trabalhadas <= 160:
    print("Você recebe R$10.00 por hora trabalhada")
    print("logo você receberá R${:.2f} por mês.".format(salario))
else:
    salario_final = salario+(salario*0.50)
    print("Você recebe R$10.00 por hora trabalhada e recebe R$5.00 por hora extra")
    print("logo você receberá R${:.2f} por mês.".format(salario_final))
    
