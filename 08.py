print ("Bem vindo ao balanço da eleição")
regiao = input("Digite sua cidade:")
numero_eleitores = int(input("Digite o número de eleitores que tem na sua cidade:"))
print ("Sua cidade tem {} eleitores".format(numero_eleitores))
print ("Calculando os dados referentes as eleições do(a) {} ...".format(regiao))
vt_branco = 20
vt_nulo = 30
vt_valido = (vt_nulo+vt_branco-numero_eleitores)*-1
print ("A quantidade de votos em brancos é {}".format(vt_branco))
print ("A quantidade de votos nulos é {}".format(vt_nulo))
print ("A quantidade de votos validos é {}".format(vt_valido))
porcentagem_bc = (vt_branco*100)/numero_eleitores
porcentagem_nl = (vt_nulo*100)/numero_eleitores
porcentagem_vd = (vt_valido*100)/numero_eleitores
print ("A porcentagem de votos em brancos é {}%".format(porcentagem_bc))
print ("A porcentagem de votos nulos é {}%".format(porcentagem_nl))
print ("A porcentagem de votos validos é {}%".format(porcentagem_vd))
