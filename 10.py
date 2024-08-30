i_distribuidor = float
impostos = float
valor_final = float
print("Bem vindo a calculadora de preço de mercado!!")
fabricação = float(input("Digite o valor da fabricação do veiculo:R$"))
print("_"*50)
print("O valor de fabricação so seu carro é R${}".format(fabricação))
i_distribuidor = (fabricação)*0.28
impostos = (fabricação)*0.45
valor_final = (fabricação+i_distribuidor+impostos)
print("O valor cobrado ao consumidor é R${}".format(valor_final))
print("_"*50)
