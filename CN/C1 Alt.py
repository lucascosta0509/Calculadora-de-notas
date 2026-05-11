dados = []
func = True
def pegar_dados(nA):
    while func == True:
        nome = input("digite seu nome ")
        dados.append(nome)
        m1 = float(input("digite sua primeira média: "))
        m2 = float(input("digite sua segunda média: "))
        m3 = float(input("digite sua terceira média: "))
        m4 = float(input("digite sua quarta média: "))
        mR = (m1 + m2 + m3 + m4 )/4
        print (mR)

        
        
        
        
        return dados
nA = int(input("digite o número de alunos: "))
for i in range(1, nA+1):
    pegar_dados(i)
print (dados)