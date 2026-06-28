class Paciente:
    def __init__(self, nome: str, data_nascimento: str, cpf: str, telefone: str, tipo_sanguineo: str, numero_prontuario: str): #Método Contrutor
        self.nome = nome
        self.data_nascimento = data_nascimento
        self._cpf = cpf
        self.telefone = telefone
        self.tipo_sanguineo = tipo_sanguineo
        self.numero_prontuario = numero_prontuario

    def registra_atendimento(self, tipo, custo):
        print(f"O paciente {self.nome} passou por um atendimento do tipo {tipo}, com custo de R$ {custo:.2f}.")

    def exibir_informacoes(self, detalhado = False):
        if detalhado:
            print(f"Nome: {self.nome}")
            print(f"Data de Nascimento: {self.data_nascimento}")
            print(f"CPF: {self._cpf}")
            print(f"Telefone: {self.telefone}")
            print(f"Tipo sanguíneo: {self.tipo_sanguineo}")
            print(f"Prontuário: {self.numero_prontuario}")
        else:
            print(f"Nome: {self.nome}")
            print(f"Tipo sanguíneo: {self.tipo_sanguineo}")
            print(f"Prontuário: {self.numero_prontuario}")

paciente1 = Paciente(
    "Felipe",
    "20/06/1999",
    "19282977730",
    "341251243",
    "A+",
    "219422"
)

print("=== Informações resumidas ===")
paciente1.exibir_informacoes()

print("\n=== Informações detalhadas ===")
paciente1.exibir_informacoes(True)

print("\n=== Registro de atendimento ===")
paciente1.registra_atendimento("Consulta Clínica", 180.00)