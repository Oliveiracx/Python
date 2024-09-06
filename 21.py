começo = int(input("A que horas começou a partida? "))
termino = int(input("Qual a hora do termino da partida? "))
if começo > termino:
    tempo = (24-começo+termino)
    print("Sua partida durou {}Hrs".format(tempo))
if começo < termino:
    tempo = (termino-começo)
    print("Sua partida durou {}Hrs".format(tempo))
if começo == termino:
    print("Sua partida durou 24hrs")
