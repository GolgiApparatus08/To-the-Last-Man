from Functions import whoHere

moderatorMessage = ""

class Player:
    def __init__(self, name, rank, strength, intellect, nerves, weapon, enteredShift, location):
        self.name = name
        self.rank = rank
        self.strength = strength
        self.intellect = intellect
        self.nerves = nerves
        self.weapon = weapon
        self.enteredShift = enteredShift
        self.location = location
        self.shift = "shift"
        self.honor = 1
        self.alive = True
        self.defending = False
        self.message = ""
        self.gymnasiumVisits = 0
        self.libraryVisits = 0
        self.bathhouseVisits = 0
        self.power = 0
        self.sleep = 0
        self.currentWeapon = weapon
        self.marks = []
        self.commands = []
        self.located = False
        self.visited = False

    def REST(self, locations, players):
        if self.alive is False:
            self.DEAD()
            return

        if self.location is locations[0]:   #Barraks
            self.location.visit(self)
        if self.location is locations[1]:   #Sanitation
            self.message += str("You nod off as far from the incinerator as you can get and manage to get a decent hour of rest in. ")
            witnesses = whoHere(self, players)
            for w in range(len(witnesses)):
                witnesses[w].message += str(self.name + " was sleeping as far from the incinerator as they can get. ")
        if self.location is locations[2]:   #Gymnasium
            self.message += str("You nod off on one of the weight benches and manage to get a decent hour of rest in. ")
            witnesses = whoHere(self, players)
            for w in range(len(witnesses)):
                witnesses[w].message += str(self.name + " was sleeping on one of the weight benches. ")
        if self.location is locations[3]:   #Medical
            self.message += str("You nod off on a gurney and manage to get a decent hour of rest in. ")
            witnesses = whoHere(self, players)
            for w in range(len(witnesses)):
                witnesses[w].message += str(self.name + " was sleeping on a gurney. ")
        if self.location is locations[4]:   #Library
            self.message += str("You nod off behind one of the bookshelves and manage to get a decent hour of rest in. ")
            witnesses = whoHere(self, players)
            for w in range(len(witnesses)):
                witnesses[w].message += str(self.name + " was sleeping behind one of the bookshelves. ")
        if self.location is locations[5]:   #Information
            self.message += str("You nod off between two fileing cabinets and manage to get a decent hour of rest in. ")
            witnesses = whoHere(self, players)
            for w in range(len(witnesses)):
                witnesses[w].message += str(self.name + " was sleeping between two fileing cabinets. ")
        if self.location is locations[6]:   #Bathhouse
            self.message += str("You nod off in one of the pool chairs and manage to get a decent hour of rest in. ")
            witnesses = whoHere(self, players)
            for w in range(len(witnesses)):
                witnesses[w].message += str(self.name + " was sleeping in one of the pool chairs. ")
        if self.location is locations[7]:   #Communications
            self.message += str("You nod off leaning forward against a communications monitor and manage to get a decent hour of rest in. ")
            witnesses = whoHere(self, players)
            for w in range(len(witnesses)):
                witnesses[w].message += str(self.name + " was leaning foward, asleep, against one of the communications monitors. ")
        if self.location is locations[8]:   #Power
            self.message += str("You nod off against the wall as far from the generator as you can get and manage to get a decent hour of rest in. ")
            witnesses = whoHere(self, players)
            for w in range(len(witnesses)):
                witnesses[w].message += str(self.name + " was sleeping against the wall as far from the generator as they could get. ")
        if self.location is locations[9]:   #Armaments
            self.message += str("You nod off against the glass case that stores the weapons and manage to get a decent hour of rest in. ")
            witnesses = whoHere(self, players)
            for w in range(len(witnesses)):
                witnesses[w].message += str(self.name + " was sleeping against the glass case that stores the weapons. ")
        if self.location is locations[10]:  #Security
            self.message += str("You nod off in one of the security guard's swiveling chairs and manage to get a decent hour of rest in. ")
            witnesses = whoHere(self, players)
            for w in range(len(witnesses)):
                witnesses[w].message += str(self.name + " was sleeping in one of the security guard's swiveling chairs. ")
        if self.location is locations[11]:  #Command
            self.message += str("You nod off in a desk chair and manage to get a decent hour of rest in. ")
            witnesses = whoHere(self, players)
            for w in range(len(witnesses)):
                witnesses[w].message += str(self.name + " was sleeping in a desk chair. ")

    def WORK(self, room, locations, players):
        if self.alive is False:
            self.DEAD()
            return
        if self.location is not room:
            self.message += str("Instead of working at " + room.name + ", ")
            self.LOITER(self.location)
            return

        if self.location is locations[0]:   #Barraks
            
        if self.location is locations[1]:   #Sanitation
        if self.location is locations[2]:   #Gymnasium
        if self.location is locations[3]:   #Medical
        if self.location is locations[4]:   #Library
        if self.location is locations[5]:   #Information
        if self.location is locations[6]:   #Bathhouse
        if self.location is locations[7]:   #Communications
        if self.location is locations[8]:   #Power
        if self.location is locations[9]:   #Armaments
        if self.location is locations[10]:  #Security
        if self.location is locations[11]:  #Command

    def SABOTAGE():
        if self.location is locations[0]:   #Barraks
        if self.location is locations[1]:   #Sanitation
        if self.location is locations[2]:   #Gymnasium
        if self.location is locations[3]:   #Medical
        if self.location is locations[4]:   #Library
        if self.location is locations[5]:   #Information
        if self.location is locations[6]:   #Bathhouse
        if self.location is locations[7]:   #Communications
        if self.location is locations[8]:   #Power
        if self.location is locations[9]:   #Armaments
        if self.location is locations[10]:  #Security
        if self.location is locations[11]:  #Command

    def LOITER():
        if self.location is locations[0]:   #Barraks
        if self.location is locations[1]:   #Sanitation
        if self.location is locations[2]:   #Gymnasium
        if self.location is locations[3]:   #Medical
        if self.location is locations[4]:   #Library
        if self.location is locations[5]:   #Information
        if self.location is locations[6]:   #Bathhouse
        if self.location is locations[7]:   #Communications
        if self.location is locations[8]:   #Power
        if self.location is locations[9]:   #Armaments
        if self.location is locations[10]:  #Security
        if self.location is locations[11]:  #Command

    def KILL(self, target):

        global moderatorMessage

        #Make sure the target is actually alive :P
        if target.alive is False:
            self.message += str("While looking to kill them, you find " + target.name + "'s body on the floor in " + self.location + ". ")
            return

        self.message += str("You find " + target.name + " in " + target.location + ". ")

        #Deal with defending
        if target.defending is true:
            self.message += str("Unfortunatly, they're alert at the moment, and you're too intimidated to attack head on. ")
            return

        #FIGHT!

        #Blunt
        if self.currentWeapon.type is "blunt":
            self.marks.append("bruises")
            target.marks.append("bruises")

            #Wins
            if self.strength > fightStrength:
                target.alive = false
                moderatorMessage += str(target.name + " has been killed by " + self.name + " in " + target.location + " at " + time + " with " + self.weapon + ". His rank was " + target.rank + ", his strength was " + target.strength + ", his intellect was " + target.intellect + ", his nerves was " + target.nerves + ", his weapon was " + target.weapon + ", and his shift was " + target.shift + ". ")
                self.honor = self.honor - target.honor
                if self.honor is 0:
                    self.honor = -1
                target.message += str(self.name + " catches you off guard and bashes your skull in with " + self.currentWeapon + ". Unless contradicted by future information, you are dead. You may no longer discuss the game with other players or communicate any game relevant details.")
                return

            #Loses
            else:
                target.message += str(self.name + " comes at you with " + self.weapon + " in an attempt to bash your head in. Stronger than him, you survive the scuffle that follows, albeit with a few bruises.")
                self.message += str("You attempt to bash " + target.name + "'s head in with your " + self.currentWeapon + ", but he's too strong and survives the scuffle that follows with only a few bruises.")
                return

        #Medical
        elif self.currentWeapon.weaponType is medical:

            #Wins
            if self.intellect > fightIntellect:
                target.alive = false
                moderatorMessage += str(target.name + " has been killed by " + self.name + " in " + target.location + " at " + time + " with " + self.weapon + ". His rank was " + target.rank + ", his strength was " + target.strength + ", his intellect was " + target.intellect + ", his nerves was " + target.nerves + ", his weapon was " + target.weapon + ", and his shift was " + target.shift + ". ")
                self.honor = self.honor - target.honor
                if self.honor is 0:
                    self.honor = -1
                target.message += str(self.name + " catches you off guard and manages to outwit you with " + self.currentWeapon + ". Unless contradicted by future information, you are dead. You may no longer discuss the game with other players or communicate any game relevant details.")
                witnesses = []
                return

            #Loses
            else:
                target.message += str(self.name + " tries to kill you with " + self.weapon + ", but you outwit him and survive.")
                self.message += str("You try to kill " + target.name + " with your " + self.currentWeapon ", but he's too smart and catches you, surviving the attempt.")
                return

        #Sharp
        else if self.currentWeapon.weaponType is sharp:
            self.marks.append(cuts)
            target.marks.append(cuts)

            #Wins
            if self.nerves > fightnerves:
                target.alive = false
                moderatorMessage += str(target.name + " has been killed by " + self.name + " in " + target.location + " at " + time + " with " + self.weapon + ". His rank was " + target.rank + ", his strength was " + target.strength + ", his intellect was " + target.intellect + ", his nerves was " + target.nerves + ", his weapon was " + target.weapon + ", and his shift was " + target.shift + ". ")
                self.honor = self.honor - target.honor
                if self.honor is 0:
                    self.honor = -1
                target.message += str(self.name + " catches you off guard and stabs you with " + self.currentWeapon + ". Unless contradicted by future information, you are dead. You may no longer discuss the game with other players or communicate any game relevant details.")
                witnesses = []
                return

            #Loses
            else:
                target.message += str(self.name + " tries to stab you with " + self.weapon + ", but your reaction time is quicker than theirs and you survive.")
                self.message += str("You try to stab " + target.name + " with your " + self.currentWeapon ", but he's too quick, survives the attempt.")
                return