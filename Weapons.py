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
        self.index = "00"
        self.withoutArticle = "lifting weight"

class majorAward(Weapon):
    def __init__(self):
        self.name = "a major award"
        self.type = "blunt"
        self.used = False
        self.index = "01"
        self.withoutArticle = "major award"

class encryptedLaptop(Weapon):
    def __init__(self):
        self.name = "an encrypted laptop"
        self.type = "blunt"
        self.used = False
        self.index = "02"
        self.withoutArticle = "encrypted laptop"

class heavyBriefcase(Weapon):
    def __init__(self):
        self.name = "a heavy briefcase"
        self.type = "blunt"
        self.used = False
        self.index = "03"
        self.withoutArticle = "heavy briefcase"

class thePrince(Weapon):
    def __init__(self):
        self.name = "a copy of 'The Prince'"
        self.type = "blunt"
        self.used = False
        self.index = "04"
        self.withoutArticle = "copy of 'The Prince'"

class humanSkull(Weapon):
    def __init__(self):
        self.name = "a human skull"
        self.type = "blunt"
        self.used = False
        self.index = "05"
        self.withoutArticle = "human skull"

class strongBourbon(Weapon):
    def __init__(self):
        self.name = "strong bourbon"
        self.type = "medical"
        self.used = False
        self.index = "06"
        self.withoutArticle = "strong bourbon"

class aggressiveStimulants(Weapon):
    def __init__(self):
        self.name = "aggressive stimulants"
        self.type = "medical"
        self.used = False
        self.index = "07"
        self.withoutArticle = "aggressive stimulants"

class petSnake(Weapon):
    def __init__(self):
        self.name = "a pet snake"
        self.type = "medical"
        self.used = False
        self.index = "08"
        self.withoutArticle = "pet snake"

class exoticPoison(Weapon):
    def __init__(self):
        self.name = "exotic poison"
        self.type = "medical"
        self.used = False
        self.index = "09"
        self.withoutArticle = "exotic poison"

class sleepingPills(Weapon):
    def __init__(self):
        self.name = "sleeping pills"
        self.type = "medical"
        self.used = False
        self.index = "10"
        self.withoutArticle = "sleeping pills"

class neurotoxicGas(Weapon):
    def __init__(self):
        self.name = "neurotoxic gas"
        self.type = "medical"
        self.used = False
        self.index = "11"
        self.withoutArticle = "neurotoxic gas"

class captainsKnife(Weapon):
    def __init__(self):
        self.name = "the captain's knife"
        self.type = "sharp"
        self.used = False
        self.index = "12"
        self.withoutArticle = "captain's knife"

class antiqueSword(Weapon):
    def __init__(self):
        self.name = "an antique sword"
        self.type = "sharp"
        self.used = False
        self.index = "13"
        self.withoutArticle = "antique sword"

class forgedKeycard(Weapon):
    def __init__(self):
        self.name = "a forged keycard"
        self.type = "sharp"
        self.used = False
        self.index = "14"
        self.withoutArticle = "forged keycard"

class sacredDagger(Weapon):
    def __init__(self):
        self.name = "a sacred dagger"
        self.type = "sharp"
        self.used = False
        self.index = "15"
        self.withoutArticle = "sacred dagger"

class throwingShurikens(Weapon):
    def __init__(self):
        self.name = "throwing shurikens"
        self.type = "sharp"
        self.used = False
        self.index = "16"
        self.withoutArticle = "throwing shurikens"

class improvisedShiv(Weapon):
    def __init__(self):
        self.name = "an improvised shiv"
        self.type = "sharp"
        self.used = False
        self.index = "17"
        self.withoutArticle = "improvised shiv"