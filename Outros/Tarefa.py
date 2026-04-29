idade = int(input("Digite sua idade: "))
salario = float(input("Digite seu salário: "))
tempo_trabalho = int(input("Digite seu tempo de trabalho (em anos): "))

if idade < 18:
    print("Empréstimo NEGADO: menor de idade.")
elif salario >= 5000:
    print("Empréstimo APROVADO automaticamente (alto salário).")
elif idade >= 18 and salario >= 2000 and tempo_trabalho >= 2:
    print("Empréstimo APROVADO.")
else:
    print("Empréstimo NEGADO: não atende aos requisitos.")
