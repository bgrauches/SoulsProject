class Stats():
    def __init__(self, hp, ataque, bloqueo, evasion):
        self.hp = hp
        self.ataque = ataque
        self.bloqueo = bloqueo
        self.evasion = evasion

    def getHp (self):
        return self.hp

    def getAtaque (self):
        return self.ataque

    def getBloqueo (self):
        return self.bloqueo

    def getEvasion (self):
        return self.evasion
