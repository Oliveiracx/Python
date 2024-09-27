conta = input("Insira o número da sua conta:")
print("Número de conta:{}".format(conta))
saldo = float(input("Insira o seu salado atual:"))
debito = float(input("Insira o seu débito:"))
credito = float(input("Insira o seu crédito:"))
saldo_final = saldo-(debito+credito)
if saldo_final < 0:
    print("Seu saldo é negativo!!")
if saldo_final > 0:
    print("Seu saldo é positivo!!")
if saldo_final == 0:
    print("Seu saldo está zerado!!")
