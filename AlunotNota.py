###Moude######

class Aluno():
    def __init__(self, Numero_da_matricula, Nome_do_aluno, Nota):
        self.Numero_da_matricula = Numero_da_matricula
        self.Nome_do_aluno = "Josias"
        self.Nota = Nota

    def TodosOsDados(self):
        return "TodosOsDados: "+str(self.Numero_da_matricula)+ ", "+self.Nome_do_aluno+ " - Nota: " + self.Nota.CalcularResultadotodaNota(self)


#######Sistema de Nota#############

class Nota():   

    def _init_(self, Nota):
        self.Nota = Nota
        
    def CalcularResultadotodaNota(self):

        if (self.Nota > 7):
            return "Aprovado"
    
        elif (self.Nota < 5):
            return "repovado"
    
        

####Objeto do moude##########]

Aluno1 = Aluno(Numero_da_matricula=50000000, Nome_do_aluno="Josias", Nota=8 )

print(Aluno1.TodosOsDados())
print(Nota.CalcularResultadotodaNota())



