Dia = int(input("Digite o dia do seu aniversario:"))
Mês = int(input("Digite o mês do seu aniversario:"))
Ano = int(input("Digite o Ano do seu aniversario:"))
print ("Agora")
Dia_atual = int(input("Digite o dia em que estamos:"))
Mês_atual = int(input("Digite o mês em que estamos:"))
Ano_atual = int(input("Digite o Ano em que estamos:"))
print()
print ("Nascido em {}/{}/{}?".format(Dia, Mês, Ano))
Resposta = str(input())
if Resposta == "sim":
    print ("Então vamos começar a calcular a quantos dias vc está vivo!")
    print()
    Dias_corridos = Dia-Dia_atual
    Mês_corridos = (Mês-Mês_atual)*30
    Anos_corridos = (Ano-Ano_atual)*365
    Tempo_final = (Dias_corridos+Mês_corridos+Anos_corridos)*-1
    print ("Se não considerarmos os anos bissextos você está vivo a {} dias".format(Tempo_final))
if Resposta == "não":
    print ("Corrija a idade então")
 
