import math
print("INFORME")
Func = True
#primeira unidade
while Func == True:
    teste1 = (float(input("nota do primeiro teste: ")))
    prova1 = (float(input("nota da primeiro prova: ")))
    nna1 = (float(input("nota da primeiro nna: ")))
    media1 = (teste1+prova1+nna1)/3
    if (teste1 or prova1 or nna1) >10 or (teste1 or prova1 or nna1) <0:
        print("insira nota válida, reinicie o programa")
        break
    else:
        if media1 % 1 > 0.5:
            media1=math.ceil(media1)
        elif media1 % 1 < 0.5:
            media1=math.ceil(media1*2) / 2
        restante = 28 - media1
        print(f"sua primeira média foi de {media1:.1f}, ainda faltam {restante:.1f} pontos")
        

#segunda unidade
    teste2 = (float(input("nota do segundo teste: ")))
    prova2 = (float(input("nota da segundo prova: ")))
    nna2 = (float(input("nota da segundo nna: ")))
    media2 = (teste2+prova2+nna2)/3
    if (teste2 or prova2 or nna2) >10 or (teste2 or prova2 or nna2) <0:
        print("insira nota válida, reinicie o programa")
        break
    else:
        if media2 % 1 > 0.5:
            media2=math.ceil(media2)
        elif media2 % 1 < 0.5:
            media2=math.ceil(media2*2) / 2
        restante = 28 - (media1+media2)
        print(f"sua segunda média foi de {media2:.1f}, ainda faltam {restante:.1f} pontos")
       
    #terceira unidade
    teste3 = (float(input("nota do terceiro teste: ")))
    prova3 = (float(input("nota da terceira prova: ")))
    nna3 = (float(input("nota da terceira nna: ")))
    media3 = (teste3+prova3+nna3)/3
    if (teste3 or prova3 or nna3) >10 or (teste3 or prova3 or nna3) <0:
        print("insira nota válida, reinicie o programa")
        break
    else:
        if media3 % 1 > 0.5:
            media3=math.ceil(media3)
        elif media3 % 1 < 0.5:
            media3 = math.ceil(media3*2) / 2
        restante = 28 - (media1+media2+media3)
        if restante > 0:
            print(f"sua terceira média foi de {media3:.1f}, ainda faltam {restante:.1f} pontos")
        elif restante <= 0:
          print(f"Sua terceira média foi de {media3:.1f},você está passado com {-restante:.1f} pontos de folga")
        
          
 
#quarta unidade
    teste4 = (float(input("nota do quarto teste: ")))
    prova4 = (float(input("nota da quarta prova: ")))
    nna4 = (float(input("nota da quarta nna: ")))
    media4 = (teste4+prova4+nna4)/3
    if (teste4 or prova4 or nna4) >10 or (teste4 or prova4 or nna4) <0:
        print("insira nota válida, reinicie o programa")
        break
    else:
        if media4 % 1 > 0.5:
            media4=math.ceil(media4)
        elif media4 % 1 < 0.5:
            media4 = math.ceil(media4*2) / 2
        restante = 28 - (media1+media2+media3+media4)
        if restante > 0:
            print(f"sua quarta média foi de {media4:.1f}, ainda faltam {restante:.1f} pontos")
        elif restante <= 0:
          print(f"Sua quarta média foi de {media4:.1f},você está passado com {-restante:.1f} pontos de folga")
 
#final
    mediafinal = (media1+media2+media3+media4)/4
    if mediafinal >= 7:
        print (f"você passou com uma média final de {mediafinal:.1f} pontos")
        break
    elif mediafinal < 7:
        print (f"sua nota final foi de {mediafinal:.1f}, você está de recuperação")
        break
    else:
        print ("sua nota final não pode ser calculada")
        break