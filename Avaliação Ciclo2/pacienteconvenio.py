from paciente import Paciente

class Paciente_convenio(Paciente):
    def __init__(self, nome: str, data_nascimento: str, cpf: str, telefone: str, tipo_sanguineo: str, numero_prontuario: str, nome_convenio: str, numero_carteira: str):
        super().__init__(
            nome,
            data_nascimento, 
            cpf, 
            telefone, 
            tipo_sanguineo, 
            numero_prontuario)
        
        self.nome_convenio = nome_convenio
        self.numero_carteira = numero_carteira

    def registrar_autorizacao(self, procedimento, valor_glosa = 0):
        print(f"Procedimento autorizado pelo convênio: {procedimento}")
        print(f"Valor da glosa: R$ {valor_glosa:.2f}")
        
    def exibir_informacoes(self, detalhado = False):
        super().exibir_informacoes(detalhado)
        print(f"Convênio: {self.nome_convenio}")
        print(f"Número da carteirinha: {self.numero_carteirinha}")
        

paciente = Paciente_convenio(
    "Maria Silva",
    35,
    "123.456.789-00",
    "(11) 99999-9999",
    "Rua das Flores, 123",
    "maria@email.com",
    "Unimed",
    "987654321"
)

paciente.exibir_informacoes(detalhado=True)
paciente.registrar_autorizacao("Consulta cardiológica", 0)