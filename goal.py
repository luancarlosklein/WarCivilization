import random
#from player import Player

class Goal():
    def __init__(self, np):
    	#1-> Personagem com mais moedas por 10 turnos
    	#2-> Possuir 50 territorios
    	#3-> Personagem as 4 quinas do mapa por 5 turnos conseq
    	#4-> Possuir todos os territorios do bioma dado por type
    	#5-> Possuir uma linha ou duas colunas completas
    	#6-> obter 100 vitorias
    	#7-> Aniquilar o personagem dado por opponent

        self.mission = random.randint (1,7)  
        self.type = random.randint (0,3)
        self.opponent = 0
        if (np>1):
        	self.opponent = random.randint (1,100)%(np-1) +1
        #contador do progresso da missao
        self.count = 0



    def show (self):
        return 0

