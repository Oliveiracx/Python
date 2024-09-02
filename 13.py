print("Obs:sua nota de Matemática tem peso 2, a de Português tem peso 3 e a de Geografia tem peso 5.")
nota_mat = int(input("Digite sua nota de Matemática:"))
nota_port = int(input("Digite sua nota de Português:"))
nota_geo = int(input("Digite sua nota de Geografia:"))
media = (nota_mat*2)+(nota_port*3)+(nota_geo*5)
media_final = media/10
print("Sua média final é de {}".format(media_final))
