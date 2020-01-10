class moves():
    def __init__(self, nom, damage, probab):
        self.nom = nom
        self.damage = damage
        self.probab = probab

        #getters y setters nombre y damage
    def getNom(self):
        return self.nom
    def setNom(self, newNom):
        self.nom = newNom
    def getDamage(self):
        return  self.damage
    def setDamage(self, newDamage):
        self.damage = newDamage
    def getProbab(self):
        return self.probab
    def setProbab(self, newProbab):
        self.probab = newProbab
