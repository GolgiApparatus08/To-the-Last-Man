class Weapon:
    def __init__(self):
        self.name = "none"

    def __str__(self):
        return self.name

class liftingWeight(Weapon):
    def __init__(self):
        self.name = "a lifting weight"
        self.type = "blunt"
        self.used = False

class majorAward(Weapon):
    def __init__(self):
        self.name = "a major award"
        self.type = "blunt"
        self.used = False

class encryptedLaptop(Weapon):
    def __init__(self):
        self.name = "an encrypted laptop"
        self.type = "blunt"
        self.used = False

class heavyBriefcase(Weapon):
    def __init__(self):
        self.name = "a heavy briefcase"
        self.type = "blunt"
        self.used = False

class thePrince(Weapon):
    def __init__(self):
        self.name = "a copy of 'The Prince'"
        self.type = "blunt"
        self.used = False

class humanSkull(Weapon):
    def __init__(self):
        self.name = "a human skull"
        self.type = "blunt"
        self.used = False

class strongBourbon(Weapon):
    def __init__(self):
        self.name = "strong bourbon"
        self.type = "medical"
        self.used = False

class aggressiveStimulants(Weapon):
    def __init__(self):
        self.name = "aggressive stimulants"
        self.type = "medical"
        self.used = False

class petSnake(Weapon):
    def __init__(self):
        self.name = "a pet snake"
        self.type = "medical"
        self.used = False

class firstAid(Weapon):
    def __init__(self):
        self.name = "a first aid kit"
        self.type = "medical"
        self.used = False

class sleepingPills(Weapon):
    def __init__(self):
        self.name = "sleeping pills"
        self.type = "medical"
        self.used = False

class neurotoxicGas(Weapon):
    def __init__(self):
        self.name = "neurotoxic gas"
        self.type = "medical"
        self.used = False

class captainsKnife(Weapon):
    def __init__(self):
        self.name = "the captain's knife"
        self.type = "sharp"
        self.used = False

class antiqueSword(Weapon):
    def __init__(self):
        self.name = "an antique sword"
        self.type = "sharp"
        self.used = False

class forgedKeycard(Weapon):
    def __init__(self):
        self.name = "a forged keycard"
        self.type = "sharp"
        self.used = False

class sacredDagger(Weapon):
    def __init__(self):
        self.name = "a sacred dagger"
        self.type = "sharp"
        self.used = False

class throwingShurikens(Weapon):
    def __init__(self):
        self.name = "throwing shurikens"
        self.type = "sharp"
        self.used = False

class improvisedShiv(Weapon):
    def __init__(self):
        self.name = "an improvised shiv"
        self.type = "sharp"
        self.used = False

class aBluntWeapon(Weapon):
    def __init__(self):
        self.name = "a blunt weapon"
        self.type = "blunt"
        self.used = False

class aMedicalWeapon(Weapon):
    def __init__(self):
        self.name = "a medical weapon"
        self.type = "medical"
        self.used = False

class aSharpWeapon(Weapon):
    def __init__(self):
        self.name = "a sharp weapon"
        self.type = "sharp"
        self.used = False