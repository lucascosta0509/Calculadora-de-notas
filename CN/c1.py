import math
func = True
print("INFORME")
def calculadora(Unidade):
    while func == True:
     try:
            dados = []
            teste =(float(input(f"\nNota do {Unidade}º teste: ")))
            dados.append(teste)
            prova =(float(input(f"Nota da {Unidade}º prova: ")))
            dados.append(prova)
            naa =(float(input(f"Nota da {Unidade}º naa: ")))
            dados.append(naa)
            if (teste or prova or naa) >10 or (teste or prova or naa) <0:
                print("insira uma nota válida")
                continue
            else:
                mediaU = sum(dados)/len(dados)
                if mediaU % 1 >0.5:
                    mediaU=math.ceil(mediaU)
                elif mediaU % 1<0.5:
                    mediaU=math.ceil(mediaU*2) / 2
                else:
                    mediaU = mediaU
                return mediaU
     except ValueError:
         print ("Insira apenas números")
        
medias = []

for i in range(1,5):
    mediaU= calculadora(i)
    medias.append(mediaU)
    restante = 28 - sum(medias)
    if restante > 0:
        print(f"Sua média foi de {mediaU} pontos, ainda lhe faltam {restante} pontos")
    elif restante < 0:
        print(f"Você está passado com {-restante} pontos de folga")
    else:
        print("você está passado")
mediaF = sum(medias)/len(medias)
if mediaF >= 7:
    print(f"\nSua nota final foi de {mediaF} pontos, você está passado")
elif mediaF<7:
    print(f"\nSua nota final foi de {mediaF} pontos, você está de recuperação, necessitando de {restante} pontos")
        
        