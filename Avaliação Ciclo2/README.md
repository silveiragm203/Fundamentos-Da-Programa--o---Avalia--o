# Sistema de Gerenciamento de Pacientes

##Este projeto foi feito em Python com o objetivo de aplicar os conceitos da Programação Orientada a Objetos (POO). O sistema é composto por uma classe principal, denominada Paciente, e duas subclasses :Paciente_convenio e Paciente_particular.
A utilização da herança permite que as classes derivadas reutilizem os atributos e métodos da classe principal, adicionando apenas as funcionalidades específicas de cada tipo de paciente.

# Estrutura do Projeto
``O projeto está dividido em três arquivos principais:``
1. paciente.py
2. pacienteconvenio.py
3. pacienteparticular.py

##Cada arquivo possui uma função específica.
# paciente.py
``Classe Paciente, que representa as informações básicas de qualquer paciente.``
``A classe possui os seguintes atributos:``
(Nome;
Data de nascimento;
CPF;
Telefone;
Tipo sanguíneo;
Número do prontuário.)

##Também possui dois métodos principais:
1. registra_atendimento()
##Este método registra um atendimento realizado e exibe o tipo do atendimento e o seu custo.
2. exibir_informacoes()
``Este método exibe as informações do paciente.``
``Quando o parâmetro detalhado é igual a False, são exibidas apenas as informações principais.``
``Quando detalhado=True, todas as informações cadastradas do paciente são apresentadas.``

# pacienteconvenio.py
``Este arquivo contém a subclasse Paciente_convenio, que herda da classe Paciente.``
``Além dos atributos herdados, ela adiciona:``
(Nome do convênio;
Número da carteira do convênio.)
##A classe possui o método:
1. registrar_autorizacao()
``Responsável por registrar a autorização de um procedimento realizado pelo convênio, informando também o valor da glosa.``
``Além disso, o método exibir_informacoes() foi sobrescrito para exibir, além dos dados do paciente, as informações referentes ao convênio.``

# pacienteparticular.py
``Este arquivo contém a subclasse Paciente_particular, que também herda da classe Paciente.``
``Ela adiciona os atributos:``
A. Forma de pagamento;
B. Desconto de fidelidade.
##Além disso, possui o método:
1. calcular_valor_final()
``Recebe o valor da consulta e uma taxa de urgência, calcula o desconto de fidelidade e retorna o valor final da consulta.``
O método exibir_informacoes() também foi sobrescrito para mostrar as informações referentes ao pagamento antes de exibir os dados herdados da classe Paciente.

## A classe Paciente serve como base para as demais classes.

## Herança
As classes Paciente_convenio e Paciente_particular herdam todos os atributos e métodos da classe Paciente, evitando repetição de código e facilitando a organização do projeto.

## Encapsulamento
O atributo _cpf utiliza o prefixo _, indicando que ele deve ser tratado como um atributo protegido, sendo acessado preferencialmente pelos métodos da própria classe.

## Polimorfismo
O método exibir_informacoes() foi sobrescrito nas classes derivadas.
Dessa forma, cada tipo de paciente consegue exibir suas informações específicas, mantendo o mesmo nome de método.

- Utilização do super()
Nas classes derivadas é utilizado o método super() para chamar o construtor e os métodos da classe Paciente.
Isso permite reutilizar a implementação da classe base sem necessidade de repetir código.

## Funcionamento do Sistema
O funcionamento do projeto ocorre da seguinte maneira:
Um paciente é criado utilizando uma das classes disponíveis.
Os dados são armazenados nos atributos do objeto.
As informações do paciente podem ser exibidas de forma resumida ou detalhada.
Pacientes de convênio podem registrar autorizações de procedimentos.
Pacientes particulares podem calcular o valor final da consulta considerando taxa de urgência e desconto de fidelidade.
