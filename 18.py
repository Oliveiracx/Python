ano_atual = int(input("Digite o ano em que estamos:"))
ano_nascimento = int(input("Agore digite o ano em que você nasceu:"))
idade = ano_atual - ano_nascimento
print(idade)
if idade >= 16:
    print("Parabéns você pode votar")
if idade < 16:
    print("Você não pode votar ainda")
