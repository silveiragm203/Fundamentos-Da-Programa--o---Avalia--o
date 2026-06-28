from paciente import Paciente
# Atributos adicionais
# forma_pagamento — string · ex: "Cartão", "Pix", "Dinheiro"
# desconto_fidelidade — float · desconto aplicado por fidelidade (ex: 0.10 = 10%)

# Classe Filha, Subclasse
class Paciente_particular(Paciente):
    def __init__(self, nome: str, data_nascimento: str, cpf: str, telefone: str, tipo_sanguineo: str, numero_prontuario: str, forma_pagamento: str, desconto_fidelidade: float):
        super().__init__(
        nome,
        data_nascimento,
        cpf, telefone,
        tipo_sanguineo,
        numero_prontuario
        )

        self.forma_pagamento = forma_pagamento
        self.desconto_fidelidade = desconto_fidelidade
    
    def calcular_valor_final(self, valor_consulta, taxa_urgencia):
        valor = valor_consulta + taxa_urgencia
        desconto = valor_consulta * self.desconto_fidelidade
        valor -= desconto
        return valor
    
    def exibir_informacoes(self, detalhado=False):
        print(f"Forma de pagamento: {self.forma_pagamento}")
        print(f"Desconto fidelidade: {self.desconto_fidelidade * 100:.0f}%")
        return super().exibir_informacoes(detalhado)
    
pessoa1 = Paciente_particular("Felipe","20/06/1999","19282977730","341251243","A+","219422","Pix",0.10)

pessoa1.exibir_informacoes(True)