Saldo = 1000.00
historico = [""] # Lista Vazia

print(f' 🏧--- Bem-Vindo ao Caixa Eletrônico ---')

while True: # Imprime pelo menos o while uma vez
    print(f''' --- Menu Principal ---
          [1] - Depositar
          [2] - sacar
          [3] - Ver Saldo
          [4] - Histórico
          [5] - Sair     
          ''')
    Opção = input('➡️ Escolha uma opção: ')

    # Lógica para a opção de Depósito
    if Opção == '1':
        Valor_deposito = float(input(' ➡️ Digite o Valor para Depósito: R$'))
        if Valor_deposito > 0:
            #Saldo = Saldo + Valor_deposito
            Saldo += Valor_deposito
            registro = f'Depósito: +R$ {Valor_deposito:.2f}'
            historico.append(registro)  # append() adicionar algo a lista
            print(' 🆗 Depósito realizado com sucesso. ')
        else:
            print(' ❌ Valor inválido. O Depósito deve ser um número positivo. ')
    elif Opção == '2':
        Valor_Saque = float(input(' ➡️ Digite o Valor para Saque: R$'))
        if Valor_Saque <= 0:
            print('❌ Valor inválido! O saque deve ser um número positivo. ')
        elif Valor_Saque > Saldo:
            print('❌ Saldo insuficiente para realizar este saque. ')
        else:
            # Saldo = Saldo - Valor_Saque
            Saldo -= Valor_Saque
            registro = f'Saque: -R$ {Valor_Saque:.2f}'
            historico.append(registro)
            print(' 🆗 Saque realizado com sucesso! Retire o seu dinheiro. ')
    elif Opção == "3":
        print(f' 💵 Seu saldo atual é: R$ {Saldo:.2f}')
    elif Opção == "4":
        print(' 📃 --- Histórico de Transações ---')
        if not historico: # Verifica se histórico está vazia , pois toda variável/estrutura vazia é true por padrão.
            print('❌ Nenhuma transação foi realizada ainda.')
        else:
            for transação in historico:
                print(transação)
    elif Opção == '5':
        print('🌞 Obrigado por utilizar nossa Caixa eletrônica. Finalizando . . .')
        break # Encerra o laço while
    else:
        print('❌ Opção inválida. Por favor, escolha uma das opções do menu.')