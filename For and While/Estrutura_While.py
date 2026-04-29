# Cire um sistema aonde o valor inicial é de R$1000 e o usuário consiga realizar um saque e ao final seja exibido o valor restante do saldo.
Saldo = 1000
while Saldo > 0:
    saque = float(input("Digite o valor do saque: "))
    Saldo -= saque  #Saldo = Saldo - saque
    print(f'Saldo restante: {Saldo}')

##Se a condição nunca ficar falsa, o loop nunca para:

while True:
    print("Isso nunca para!")

##Isso é um loop infinito Só para com (break) ou fechando o programa ,Usando break no while.

while True:
    numero = int(input("Digite um número (0 para sair): "))
    
    if numero == 0:
        break

## continue Exemplo com while 

contador = 0

while contador < 5:
    contador += 1
    
    if contador == 3:
        continue
    
    print(contador)

## O valor 3 não aparece, pois foi pulado.

## Cuidado com while se usar continue sem atualizar a variável, pode gerar loop infinito: