#Lista de Gerenciamento de Notas
Quantidade = int(input("Digite Quantos alunos: "))

Nomes = []
média_Final = 7.00
média_Reprovação = 4.00   #Sempre seguir aquilo que for pedido sem nenhum tipo de alteração , média de reprovação = 5.00. Muito importante se quiser ter sucesso na area de programador.

for i in range(Quantidade):
    nome = input(f"Digite o nome{i + 1}: ")

    Notas = []

    Av1 = float(input("Digite sua nota 1: "))
    Av2 = float(input("Digite sua nota 2: "))
    Av3 = float(input("Digite sua nota 3: "))

    média =(Av1+Av2+Av3) / 3

    situacao = "";

    if média > média_Reprovação < média_Final:   #elif média > média_Reprovação and média < média_Final: - Esse ajuste garante que a classificação de Recuperação seja feita corretamente.
        situacao = "Recuperação";
        print("Você está de Recuperação. ")
    elif média <= média_Reprovação:
        situacao = "Reprovação";
        print("Você está Reprovado. ")
    elif média >= média_Final:
        situacao = "Aprovado";
        print("Você está Aprovado. ")
    
    print(f"Média do Aluno {nome} é: {média:.2f}")


    Aluno = {
        "nome": nome,
        "nota1": Av1,
        "nota2": Av2,
        "nota3": Av3,
        "media": média,
        "situacao": situacao
    }
    Nomes.append(Aluno)

    #print("Lista de Alunos: ")#
    #for Aluno in Nomes:#
        #print(Aluno)#

print('''---Resumo da turma---''')   

for Aluno in Nomes:
 
    print(f"Nome: {Aluno["nome"]}")
    print(f"Nota 1: {Aluno["nota1"]:.2f}")
    print(f"Nota 2: {Aluno["nota2"]:.2f}")
    print(f"Nota 3: {Aluno["nota3"]:.2f}")
    print(f"Média: {Aluno["media"]:.2f}")
    print(f"situacao: {Aluno["situacao"]}")
