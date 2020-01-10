from moves import  moves
class enemigos():
    def __init__(self,name, hP, ataque, bloqueo, evasion, moves):
        self.name = name
        self.hP = hP
        self.ataque = ataque
        self.bloqueo = bloqueo
        self.evasion = evasion
        self.moves = []

    #Getters i setters hp
    def getName(self):
        return self.name
    def setName(self, newName):
        self.name = newName
    def getHP(self):
        return self.hP
    def setHP(self, newHP):
        self.HP = newHP
    def getAtaque(self):
        return self.ataque
    def setAtaque(self, newAtaque):
        self.ataque = newAtaque
    def getBloqueo(self):
        return self.bloqueo
    def setBloqueo(self, newBloqueo):
        self.bloqueo = newBloqueo
    def getEvasion(self):
        return self.evasion
    def setEvasion(self, newEvasion):
        self.evasion = newEvasion
    def addMove(self, newMove):
        self.moves.append(newMove)