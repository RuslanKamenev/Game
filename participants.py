class Participants ():
    def __init__(self, name, maxHealth):
        self.name = name
        self.health = maxHealth
    
    def getHealth(self):
        return self.health

    def getName(self):
        return self.name
    #Получение урона или исцеление участников
    def setlDamage(self, damage):
        self.health = self.health - damage

    def setHeal(self, heal, maxHealth):
        self.health = self.health + heal
        if self.health > maxHealth:
            self.health = maxHealth
