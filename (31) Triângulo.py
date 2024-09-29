A = int(input("Escreva o primeiro valor:"))
B = int(input("Escreva o segundo valor:"))
C = int(input("Escreva o terceiro valor:"))
if A < (B+C) and B < (A+C) and C < (B+A):
    print("Esses valores podem formar um triângulo!")
else:
    print("Esses valores não podem formar um triângulo!")