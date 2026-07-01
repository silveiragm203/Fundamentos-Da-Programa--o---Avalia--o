from paciente import Paciente
from pacienteparticular import Paciente_particular
from pacienteconvenio import Paciente_convenio

def main():
    
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
    

    pacienteparticular1 = Paciente_particular(
        "Felipe",
        "20/06/1999"
        ,"19282977730"
        ,"341251243"
        ,"A+"
        ,"219422"
        ,"Pix"
        ,0.10
        )

    print("\n=== Informações detalhadas ===")
    pacienteparticular1.exibir_informacoes(True)

    pacienteconvenio1 = Paciente_convenio(
    "Maria Silva",
    "30/02/1976",
    "123.456.789-00",
    "(11) 99999-9999",
    "Rua das Flores, 123",
    "maria@email.com",
    "Unimed",
    "987654321"
)

    print("\n=== Informações detalhadas ===")
    pacienteconvenio1.exibir_informacoes(detalhado=True)
    print("\n=== Registro de atendimento ===")
    pacienteconvenio1.registrar_autorizacao("Consulta cardiológica", 0)
      
if __name__ == '__main__':
    main()
