class liquorHandle():
    def __init__(self):
        self.name = "a liquor handle"
        self.type = "blunt"
        self.used = False

class combatAward():
    def __init__(self):
        self.name = "a combat award"
        self.type = "blunt"
        self.used = False

class encryptedLaptop():
    def __init__(self):
        self.name = "an encrypted laptop"
        self.type = "blunt"
        self.used = False

class heavyBriefcase():
    def __init__(self):
        self.name = "a heavy briefcase"
        self.type = "blunt"
        self.used = False

class thePrince():
    def __init__(self):
        self.name = "a copy of 'The Prince'"
        self.type = "blunt"
        self.used = False

class alarmClock():
    def __init__(self):
        self.name = "an alarm clock"
        self.type = "blunt"
        self.used = False

class exoticPoison():
    def __init__(self):
        self.name = "exotic poison"
        self.type = "medical"
        self.used = False

class aggressiveStimulants():
    def __init__(self):
        self.name = "aggressive stimulants"
        self.type = "medical"
        self.used = False

class petSnake():
    def __init__(self):
        self.name = "a pet snake"
        self.type = "medical"
        self.used = False

class firstAid():
    def __init__(self):
        self.name = "a first aid kit"
        self.type = "medical"
        self.used = False

class sleepingPills():
    def __init__(self):
        self.name = "sleeping pills"
        self.type = "medical"
        self.used = False

class neurotoxicGas():
    def __init__(self):
        self.name = "neurotoxic gas"
        self.type = "medical"
        self.used = False

class kitchenKnife():
    def __init__(self):
        self.name = "a kitchen knife"
        self.type = "sharp"
        self.used = False

class decorativeSword():
    def __init__(self):
        self.name = "a decorative sword"
        self.type = "sharp"
        self.used = False

class forgedKeycard():
    def __init__(self):
        self.name = "a forged keycard"
        self.type = "sharp"
        self.used = False

class sacredDagger():
    def __init__(self):
        self.name = "a sacred dagger"
        self.type = "sharp"
        self.used = False

class throwingShurikens():
    def __init__(self):
        self.name = "throwing shurikens"
        self.type = "sharp"
        self.used = False

class improvisedShiv():
    def __init__(self):
        self.name = "an improvised shiv"
        self.type = "sharp"
        self.used = False








def findWeapons(players, weapons):
    for p in range(len(players)):
        for i in range(len(weapons)):
            if weapons[i].name is players[p].weapons:
                players[p].weapons = weapons[i]
