# Contar de 1 até 5 - 
#for número in range(1,6):
#    print(f'Eu sou o número {número}')

# Exemplo de Tabuada -> 5
i = 5 # Variável no escopo global
for número in range(1,11):
    total = i * número # Variável no escopo local
    print(f'5 x {número} = {total}')

## Quando o Python encontra continue:
## Ele ignora o restante do código dentro do loop naquela volta ,Volta para o início do loop para a próxima repetição.

for i in range(5):
    if i == 2:
        continue
    print(i)

##O número 2 é pulado, porque o continue foi executado.

##Exemplo Avaliação grade de Notas. 

#Lista de Gerenciamento de Notas
Quantidade = int(input("Digite Quantos alunos: "))

Nomes = []
média_Final = 7.00
média_Reprovação = 4.00

for i in range(Quantidade):
    nome = input(f"Digite o nome{i + 1}: ")

    Notas = []

    Av1 = float(input("Digite sua nota 1: "))
    Av2 = float(input("Digite sua nota 2: "))
    Av3 = float(input("Digite sua nota 3: "))

    média =(Av1+Av2+Av3) / 3

    situacao = "";

    if média > média_Reprovação < média_Final:
        situacao = "Recuperação";
        print("Você está de Recuperação. ")
    elif média <= média_Reprovação:
        situacao = "Reprovação";
        print("Você está Reprovado. ")
    elif média >= média_Final:
        situacao = "Aprovado";
        print("Você está Aprovado. ")
    
    print(f"Média do Aluno {nome} é: {média:.2f}")

    print("Lista de Alunos: ")
    for Aluno in Nomes:
        print(Aluno)

    Aluno = {
        "nome": nome,
        "nota1": Av1,
        "nota2": Av2,
        "nota3": Av3,
        "media": média,
        "situacao": situacao
    }
    Nomes.append(Aluno)

print('''---Resumo da turma---''')   

for Aluno in Nomes:
    # if Aluno["situacao"] != "aprovado": #Para pular alunos não aprovados
    #     continue;
    
    # if Aluno["situacao"] == "aprovado": #Quando ele encontrar o primeiro aprovado, quebra o laço
    #     break;
    print(f"Nome: {Aluno["nome"]}")
    print(f"Nota 1: {Aluno["nota1"]:.2f}")
    print(f"Nota 2: {Aluno["nota2"]:.2f}")
    print(f"Nota 3: {Aluno["nota3"]:.2f}")
    print(f"Média: {Aluno["media"]:.2f}")
    print(f"situacao: {Aluno["situacao"]}")