f = int(input("Escreva a temperatura em fahrenheit:"))
print("Agora vamos converter para celsius.")
input("Calculando...")
conversão = (f-32)/9
c = 5*conversão
print("Seus {}F convertidos se tornam {:.0f}°C.".format(f, c))
