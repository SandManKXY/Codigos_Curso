import unittest
from Funçoesdogabinha import sobrenomeNaOrdem

class NomeTest(unittest.TestCase):
    
    def teste_sobrenomeNaOrdem(self):

        NomeCompleto = sobrenomeNaOrdem("Joao","Silva","Jonhs")
        self.assertEqual(NomeCompleto, "Joao Jonhs Silva")

    
unittest.main(argv=[''], exit=False)
