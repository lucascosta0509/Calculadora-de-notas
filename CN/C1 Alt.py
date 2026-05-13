dados = {'nomes': [], 'notas': [],"status" : []}
func = True
def pegar_dados(nA):
    while func == True:
        try:
            nome = str(input("digite o nome do aluno: "))
            dados["nomes"].append(nome)
            m1 = float(input("digite a primeira média: "))
            m2 = float(input("digite a segunda média: "))
            m3 = float(input("digite a terceira média: "))
            m4 = float(input("digite a quarta média: "))
            ##adicionar sistema para bloquear números invalidos
            mR = (m1 + m2 + m3 + m4 )/4
            dados["notas"].append(mR)
            if mR >= 7:
                 estado = ("aprovado")
            else:
                 estado = ("reprovado")
            dados["status"].append(estado)
            return dados        
        except ValueError:
            print("Digite valores válidos")
try:
        nA = int(input("digite o número de alunos: "))
except ValueError:
     print("digite apenas números inteiros")        
for i in range(1,nA+1):
    pegar_dados(i)


