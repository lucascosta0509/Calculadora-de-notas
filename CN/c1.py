print("INFORME")
#primeira unidade
teste1 = (floating(input("nota do primeiro teste: ")))
prova1 = (float(input("nota da primeira prova: ")))
nna1 = (float(input("nota da primeira nna: ")))
media1 = (teste1+prova1+nna1)/3
restante = 28 - media1
print("Sua primeira média foi de",media1,"ainda faltam",restante,"pontos" )

#segunda unidade
teste2 = (float(input("nota do segundo teste: ")))
prova2 = (float(input("nota da segunda prova: ")))
nna2 = (float(input("nota da segunda nna: ")))
media2 = (teste2+prova2+nna2)/3
restante = 28 - (media1+media2)
print("Sua segunda média foi de",media2,"ainda faltam",restante,"pontos" )

#terceira unidade
teste3 = (float(input("nota do terceiro teste: ")))
prova3 = (float(input("nota da terceira prova: ")))
nna3 = (float(input("nota da terceira nna: ")))
media3 = (teste3+prova3+nna3)/3
restante = 28 - (media1+media2+media3)
if restante > 0:
    print("Sua terceira média foi de",media1,"ainda faltam",restante,"pontos" )
elif restante < 0:
    print("Você está passado com",-restante,"pontos de folga")
else:
    print ("você está passado")

#quarta unidade
teste4 = (float(input("nota do quarto teste: ")))
prova4 = (float(input("nota da quarta prova: ")))
nna4 = (float(input("nota da quarta nna: ")))
media4 = (teste4+prova4+nna4)/3
restante = 28 - (media1+media2+media3+media4)
if restante > 0:
    print("Sua quarta média foi de",media4,"ainda faltam",restante,"pontos" )
elif restante < 0:
    print("Você está passado com",-restante,"pontos de folga")
else:
    print ("você está passado")

#final
mediafinal = (media1+media2+media3+media4)/4
if mediafinal >= 7:
    print ("Você passou com uma média final de",mediafinal)
elif mediafinal < 7:
    print ("sua nota final foi de",mediafinal,"você está de recupéração")
else:
    print ("sua nota final não pode ser calculada")