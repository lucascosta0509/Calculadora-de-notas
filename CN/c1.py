import math
func = True
print("INFORME")
def calculadora(Unidade):
    while func == True:
     try:
            dados = []
            teste =(float(input(f"\nNota da {Unidade}º teste: ")))
            dados.append(teste)
            prova =(float(input(f"Nota da {Unidade}º prova: ")))
            dados.append(prova)
            naa =(float(input(f"Nota da {Unidade}º naa: ")))
            dados.append(naa)
            if (teste or prova or naa) >10 or (teste or prova or naa) <0:
                print("insira nota válida, reinicie o programa")
                break
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
         break