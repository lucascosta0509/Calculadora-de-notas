dados = {'nomes': [], 'notas': [],"status" : []}
func = True
try:
    def pegar_dados(nA):
        while func == True:
            nome = str(input("digite o nome do aluno: "))
            dados["nomes"].append(nome)
            m1 = float(input("digite a primeira média: "))
            m2 = float(input("digite a segunda média: "))
            m3 = float(input("digite a terceira média: "))
            m4 = float(input("digite a quarta média: "))
            if (m1 or m2 or m3 or m4) >10 or (m1 or m2 or m3 or m4) <0:
                print("insira uma nota válida")
                continue
            else:
                mR = (m1 + m2 + m3 + m4 )/4
                dados["notas"].append(mR)
                if mR >= 7:
                    estado = ("aprovado")
                else:
                    estado = ("reprovado")
                dados["status"].append(estado)
            return dados                  
    nA = int(input("digite o número de alunos: ")) 
    for i in range(1,nA+1):
        pegar_dados(i)
    valores_chave = ['nomes','status']
    for nome, status in zip(dados['nomes'], dados['status']):
        print(f"Aluno: {nome} | Status: {status}")
except (ValueError, NameError):
     print("Digite valores válidos, reinicie o programa")  


