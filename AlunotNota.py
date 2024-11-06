class Aluno:
    def __init__(self, Numero_da_matricula, Nome_do_aluno, Nota):
        self.Numero_da_matricula = Numero_da_matricula
        self.Nome_do_aluno = Nome_do_aluno
        self.Nota = Nota  # Nota já é um objeto da classe Nota

    def TodosOsDados(self):
        return "TodosOsDados: " + str(self.Numero_da_matricula) + ", " + self.Nome_do_aluno + " - Nota: " + self.Nota.CalcularResultadotodaNota()


class Nota:
    def __init__(self, Nota):
        self.Nota = Nota

    def CalcularResultadotodaNota(self):
        if self.Nota >= 7:
            return "Aprovado"
        elif self.Nota < 5:
            return "Reprovado"
        else:
            return "Recuperação"


# Criando os objetos
nota_aluno = Nota(8)  # Criando o objeto Nota
Aluno1 = Aluno(Numero_da_matricula=50000000, Nome_do_aluno="Josias", Nota=nota_aluno)

# Exibindo os resultados
print(Aluno1.TodosOsDados())



