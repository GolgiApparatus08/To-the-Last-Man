from Functions import doTheyDeduce, doTheyDefend, whoHere

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
        self.weaponDestroyed = False
        self.endMessage = ""

    def DEAD(self, locations, players):
        whoHere(self, "none", str(self.name + "'s body lies montionless on the floor. "), True, locations, players)

    def REST(self, locations, players):
        if self.alive is False:
            self.DEAD(locations, players)
            return

        if self.location is locations[0]:   #Barraks
            self.location.visit(self)
        if self.location is locations[1]:   #Sanitation
            self.message += str("You nod off as far from the incinerator as you can get and manage to get a decent hour of rest in. ")
            whoHere(self, "none", str(self.name + " was sleeping as far from the incinerator as they could get. "), False, locations, players)
        if self.location is locations[2]:   #Gymnasium
            self.message += str("You nod off on one of the weight benches and manage to get a decent hour of rest in. ")
            whoHere(self, "none", str(self.name + " was sleeping on one of the weight benches. "), False, locations, players)
        if self.location is locations[3]:   #Medical
            self.message += str("You nod off on a gurney and manage to get a decent hour of rest in. ")
            whoHere(self, "none", str(self.name + " was sleeping on a gurney. "), False, locations, players)
        if self.location is locations[4]:   #Library
            self.message += str("You nod off behind one of the bookshelves and manage to get a decent hour of rest in. ")
            whoHere(self, "none", str(self.name + " was sleeping behind one of the bookshelves. "), False, locations, players)
        if self.location is locations[5]:   #Information
            self.message += str("You nod off between two fileing cabinets and manage to get a decent hour of rest in. ")
            whoHere(self, "none", str(self.name + " was sleeping between two fileing cabinets. "), False, locations, players)
        if self.location is locations[6]:   #Bathhouse
            self.message += str("You nod off in one of the pool chairs and manage to get a decent hour of rest in. ")
            whoHere(self, "none", str(self.name + " was sleeping in one of the pool chairs. "), False, locations, players)
        if self.location is locations[7]:   #Communications
            self.message += str("You nod off leaning forward against a communications monitor and manage to get a decent hour of rest in. ")
            whoHere(self, "none", str(self.name + " was leaning foward, asleep, against one of the communications monitors. "), False, locations, players)
        if self.location is locations[8]:   #Power
            self.message += str("You nod off against the wall as far from the generator as you can get and manage to get a decent hour of rest in. ")
            whoHere(self, "none", str(self.name + " was sleeping against the wall as far from the generator as they could get. "), False, locations, players)
        if self.location is locations[9]:   #Armaments
            self.message += str("You nod off against the glass case that stores the weapons and manage to get a decent hour of rest in. ")
            whoHere(self, "none", str(self.name + " was sleeping against the glass case that stores the weapons. "), False, locations, players)
        if self.location is locations[10]:  #Security
            self.message += str("You nod off in one of the security guard's swiveling chairs and manage to get a decent hour of rest in. ")
            whoHere(self, "none", str(self.name + " was sleeping in one of the security guard's swiveling chairs. "), False, locations, players)
        if self.location is locations[11]:  #Command
            self.message += str("You nod off in a desk chair and manage to get a decent hour of rest in. ")
            whoHere(self, "none", str(self.name + " was sleeping in a desk chair. "), False, locations, players)

    def WORK(self, room, locations, players):
        if self.alive is False:
            self.DEAD(locations, players)
            return
        if self.location is not room:
            self.message += str("Instead of working at " + room.name + ", ")
            self.LOITER(self.location, locations, players)
            return

        if self.location is locations[0]:   #Barraks
            locations[0].workload = locations[0].workload - 1
            self.message += str("You spend the hour collecting dirty sheets and restocking sleeping supplies. ")
            whoHere(self, "none", str(self.name + " spent the hour collecting dirty sheet and restocking sleeping supplies. "), False, locations, players)
        if self.location is locations[1]:   #Sanitation
            locations[1].workload = locations[1].workload - 1
            self.message += str("You spend the hour throwing piled up garbage into the incinerator. ")
            whoHere(self, "none", str(self.name + " spent the hour throwing piled up garbage into the incinerator. "), False, locations, players)
        if self.location is locations[2]:   #Gymnasium
            locations[2].workload = locations[2].workload - 1
            self.message += str("You spend the hour organzing weights and cleaning debris off the track. ")
            whoHere(self, "none", str(self.name + " spent the hour organzing weights and cleaning debris off the track. "), False, locations, players)
        if self.location is locations[3]:   #Medical
            locations[3].workload = locations[3].workload - 1
            self.message += str("You spend the hour restocking medical supplies and preping the equipment for procedures. ")
            whoHere(self, "none", str(self.name + " spent the hour retsocking medical supplies and preping the equipment for procedures. "), False, locations, players)
        if self.location is locations[4]:   #Library
            locations[4].workload = locations[4].workload - 1
            self.message += str("You spend the hour organzing and logging books. ")
            whoHere(self, "none", str(self.name + " spent the hour organzing and logging books. "), False, locations, players)
        if self.location is locations[5]:   #Information
            locations[5].workload = locations[5].workload - 1
            self.message += str("You spend the hour filing records and debuging the computers. ")
            whoHere(self, "none", str(self.name + " spent the hour filing records and debuging the computers. "), False, locations, players)
        if self.location is locations[6]:   #Bathhouse
            locations[6].workload = locations[6].workload - 1
            self.message += str("You spend the hour cleaning the sauna and preping the heating systems. ")
            whoHere(self, "none", str(self.name + " spent the hour cleaning the sauna and preping the heating systems. "), False, locations, players)
        if self.location is locations[7]:   #Communications
            locations[7].workload = locations[7].workload - 1
            self.message += str("You spend the hour debuging the communications systems and trying to fix the connection to the capital, to no avail. ")
            whoHere(self, "none", str(self.name + " spent the hour debuging the communications systems and trying to fix the connection to the capital, to no avail. "), False, locations, players)
        if self.location is locations[8]:   #Power
            locations[8].workload = locations[8].workload - 1
            self.message += str("You spend the hour working on the generator and wiring the base's electrical systems. ")
            whoHere(self, "none", str(self.name + " spent the hour working on the generator and wiring the base's electrical systems. "), False, locations, players)
        if self.location is locations[9]:   #Armaments
            locations[9].workload = locations[9].workload - 1
            self.message += str("You spend the hour logging and properly locking up the base's supply of weapons. ")
            whoHere(self, "none", str(self.name + " spent the hour logging and properly locking up the base's supply of weapons. "), False, locations, players)
        if self.location is locations[10]:  #Security
            locations[10].workload = locations[10].workload - 1
            self.message += str("You spend the hour working on the base's security systems. ")
            whoHere(self, "none", str(self.name + " spent the hour working on the base's security systems. "), False, locations, players)
        if self.location is locations[11]:  #Command
            locations[11].workload = locations[11].workload - 1
            self.message += str("You spend the hour allocating shifts and assigning future work. ")
            whoHere(self, "none", str(self.name + " spent the hour allocating shifts and assigning future work. "), False, locations, players)

    def SABOTAGE(self, room, locations, players):
        if self.alive is False:
            self.DEAD(locations, players)
            return
        if self.location is not room:
            self.message += str("Instead of sabotaging " + room.name + ", ")
            self.LOITER(self.location, locations, players)
            return

        if self.location is locations[0]:   #Barraks
            locations[0].sabotages = locations[0].sabotages + 1
            self.message += str("You spend the hour tossing perfectly clean sheets and stocking the supplies incorrectly. ")
            whoHere(self, "none", str(self.name + " spent the hour collecting dirty sheet and restocking sleeping supplies. "), False, locations, players)
        if self.location is locations[1]:   #Sanitation
            locations[1].sabotages = locations[1].sabotages + 1
            self.message += str("You spend the hour improperly using the incinerator in an attempt to break it. ")
            whoHere(self, "none", str(self.name + " spent the hour throwing piled up garbage into the incinerator. "), False, locations, players)
        if self.location is locations[2]:   #Gymnasium
            locations[2].sabotages = locations[2].sabotages + 1
            self.message += str("You spend the hour hiding the weights and making a mess of the track. ")
            whoHere(self, "none", str(self.name + " spent the hour organzing weights and cleaning debris off the track. "), False, locations, players)
        if self.location is locations[3]:   #Medical
            locations[3].sabotages = locations[3].sabotages + 1
            self.message += str("You spend the hour replacing the labels on various medical supplies and messing with the procedure equipment. ")
            whoHere(self, "none", str(self.name + " spent the hour restocking medical supplies and preping the equipment for procedures. "), False, locations, players)
        if self.location is locations[4]:   #Library
            locations[4].sabotages = locations[4].sabotages + 1
            self.message += str("You spend the hour misplacing books and ripping random pages out. ")
            whoHere(self, "none", str(self.name + " spent the hour organzing and logging books. "), False, locations, players)
        if self.location is locations[5]:   #Information
            locations[5].sabotages = locations[5].sabotages + 1
            self.message += str("You spend the hour messing with the computers and misplacing files. ")
            whoHere(self, "none", str(self.name + " spent the hour filing records and debuging the computers. "), False, locations, players)
        if self.location is locations[6]:   #Bathhouse
            locations[6].sabotages = locations[6].sabotages + 1
            self.message += str("You spend the hour messing with the heating systems. ")
            whoHere(self, "none", str(self.name + " spent the hour cleaning the sauna and preping the heating systems. "), False, locations, players)
        if self.location is locations[7]:   #Communications
            locations[7].sabotages = locations[7].sabotages + 1
            self.message += str("You spend the hour messing with the communications systems. ")
            whoHere(self, "none", str(self.name + " spent the hour debuging the communications systems and trying to fix the connection to the capital, to no avail. "), False, locations, players)
        if self.location is locations[8]:   #Power
            locations[8].sabotages = locations[8].sabotages + 1
            self.message += str("You spend the hour messing with the generator and trying to screw up the base's electrical systems. ")
            whoHere(self, "none", str(self.name + " spent the hour working on the generator and wiring the base's electrical systems. "), False, locations, players)
        if self.location is locations[9]:   #Armaments
            locations[9].sabotages = locations[9].sabotages + 1
            self.message += str("You spend the hour improperly locking up weapons. ")
            whoHere(self, "none", str(self.name + " spent the hour logging and properly locking up the base's supply of weapons. "), False, locations, players)
        if self.location is locations[10]:  #Security
            locations[10].sabotages = locations[10].sabotages + 1
            self.message += str("You spend the hour messing with the base's security systems. ")
            whoHere(self, "none", str(self.name + " spent the hour working on the base's security systems. "), False, locations, players)
        if self.location is locations[11]:  #Command
            locations[11].sabotages = locations[11].sabotages + 1
            self.message += str("You spend the hour misallocating shifts and misplacing important work documents. ")
            whoHere(self, "none", str(self.name + " spent the hour allocating shifts and assigning future work. "), False, locations, players)

    def LOITER(self, room, locations, players):
        if self.alive is False:
            self.DEAD(locations, players)
            return
        if self.location is not room:
            self.message += str("Instead of loitering in " + room.name + ", ")
            self.LOITER(self.location, locations, players)
            return

        if self.location is locations[0]:   #Barraks
            self.message += str("You spend the hour lying in bed, watching to see if you can spot anything intresting. ")
            whoHere(self, "none", str(self.name + " spent the hour lying in bed, relaxing. "), False, locations, players)
        if self.location is locations[1]:   #Sanitation
            self.message += str("You spend the hour leaning against the incinerator, watching to see if you can spot anything intresting. ")
            whoHere(self, "none", str(self.name + " spent the hour leaning against the incinerator, relaxing. "), False, locations, players)
        if self.location is locations[2]:   #Gymnasium
            self.message += str("You spend the hour relaxing on weight bench, watching to see if you can spot anything intresting. ")
            whoHere(self, "none", str(self.name + " spent the hour relaxing on weight bench. "), False, locations, players)
        if self.location is locations[3]:   #Medical
            self.message += str("You spend the hour relaxing on a gurney, watching to see if you can spot anything intresting. ")
            whoHere(self, "none", str(self.name + " spent the hour relaxing on a gurney. "), False, locations, players)
        if self.location is locations[4]:   #Library
            self.message += str("You spend the hour casually perusing bookshelves, watching to see if you can spot anything intresting. ")
            whoHere(self, "none", str(self.name + " spent the hour casually perusing bookshelves. "), False, locations, players)
        if self.location is locations[5]:   #Information
            self.message += str("You spend the hour perched ontop of a filing cabinet, watching to see if you can spot anything intresting. ")
            whoHere(self, "none", str(self.name + " spent the hour perched ontop of a filing cabinet, relaxing. "), False, locations, players)
        if self.location is locations[6]:   #Bathhouse
            self.message += str("You spend the hour floating relaxingly in the pool, watching to see if you can spot anything intresting. ")
            whoHere(self, "none", str(self.name + " spent the hour floating in the pool, relaxing. "), False, locations, players)
        if self.location is locations[7]:   #Communications
            self.message += str("You spend the hour admiring the complicated display of communcation data and watching to see if you can spot anything intresting. ")
            whoHere(self, "none", str(self.name + " spent the hour admiring the complicated display of communcation data, relaxing. "), False, locations, players)
        if self.location is locations[8]:   #Power
            self.message += str("You spend the hour listening to the relaxing hum of the generator, watching to see if you can spot anything intresting. ")
            whoHere(self, "none", str(self.name + " spent the hour listening to the relaxing hum of the generator. "), False, locations, players)
        if self.location is locations[9]:   #Armaments
            self.message += str("You spend the hour admiring the base's large collection of deadly weapons, watching to see if you can spot anything intresting. ")
            whoHere(self, "none", str(self.name + " spent the hour admiring the base's large collection of deadly weapons. "), False, locations, players)
        if self.location is locations[10]:  #Security
            self.message += str("You spend the hour fiddling aimlessly with camera equipment and watching to see if you can spot anything intresting. ")
            whoHere(self, "none", str(self.name + " spent the hour fiddling aimlessly with camera equipment, relaxing. "), False, locations, players)
        if self.location is locations[11]:  #Command
            self.message += str("You spend the hour relaxing in a desk chair and watching to see if you can spot anything intresting. ")
            whoHere(self, "none", str(self.name + " spent the hour relaxing in a desk chair. "), False, locations, players)

    def AMBUSH(self, room, target, locations, players, time, report):
        if self.alive is False:
            self.DEAD(locations, players)
            return
        if self.location is not room:
            self.message += str("Instead of ambushing " + target.name + " in " + room.name + ", ")
            self.LOITER(self.location, locations, players)
            return
        if self.location is not target.location:
            self.message += str("You prepare to ambush " + target.name + ", but they never shows. ")
            self.LOITER(self.location, locations, players)
            return

        self.message += str("Predicting that " + target.name + " would be in " + target.location.name + " at precisely " + time + ", you use your surrondings to set a trap ahead of their arrival, killing them without any struggle or chance of defense. ")
        target.message += str("Seemingly predicting that you would be in " + target.location.name + " at percisely " + time + ", " + self.name + " set a trap ahead of your arrival, killing you without any struggle or chance of defence. You are now dead, and may no longer talk to other players about the game or communicate any game relavent information. ")
        report += str(target.name + " has been ambushed by " + self.name + " in " + target.location.name + " at " + time + ". Their rank was " + target.rank + ", their strength was " + target.strength + ", their intellect was " + target.intellect + ", their nerves was " + target.nerves + ", their weapon was " + target.weapon.name + ", and their shift was " + target.shift.name + ". ")
        self.honor = self.honor - target.honor
        if self.honor is 0 and target.honor < 0:
            self.honor = 1
        if self.honor is 0 and target.honor > 0:
            self.honor = -1
        whoHere(self, target, str("You witness " + self.name + " spring a trap on " + target.name + ", killing them without any struggle or chance of defense, seemingly having predicted they would be in " + target.location.name + " at precisely " + time + ". "), False, locations, players)
        return

    def WATCH(self, locations, players):
        if self.alive is False:
            self.DEAD(locations, players)
            return
        self.LOITER(self.location, locations, players)
        
    def STEAL(self, target, locations, players):
        if self.alive is False:
            self.DEAD(locations, players)
            return
        if self.location is not target.location:
            self.message += str("Instead of stealing from " + target.name + ", ")
            self.LOITER(self.location, locations, players)
            return
        if target.alive is False and target.currentWeapon is not "none":
            self.message += str("You find " + target.name + " dead, and slip " + target.currentWeapon + " off of them. They won't be needing it now. ")
            self.LOITER(self.location, locations, players)
            return
        if target.alive is False:
            self.message += str("You find " + target.name + " dead, which makes the job of stealing from them easier--except when you search them for a weapon you find none. Someone must have beat you to it. ")
            self.LOITER(self.location, locations, players)
            return
        if target.currentWeapon is "none":
            self.message += str("You approach " + target.name + "carefully, hoping to slip away with their weapon when their not looking. Unfortunatly, you find nothing on them and slip away just in time not to be caught in the attempt. ")
            self.LOITER(self.location, locations, players)
            return

        if self.nerves > target.nerves:
            self.message += str("Due to your greater finess, you manage to slip " + target.currentWeapon + " away from " + target.name + " You'll have to return it by morning to avoid trouble, but its yours in the meantime. ")
            self.currentWeapon = target.currentWeapon
            target.currentWeapon = "none"
            self.LOITER(self.location, locations, players)
        else:
            self.message += str("Unfortunatly, " + target.name + " has greater finess than you and catches you in the act of trying to slip a potencial weapon away from them. They make a scene, hoping someone will take notice, and you shuffle away embarrased. ")
            target.message += str("At some point, you catch " + self.name + " trying to steal your weapon, as your nerves are better than theres. You scold them loudly, hoping someone will take notice of their betrayal. ")
            whoHere(self, target, str("At some point there's a loud altercation. Apparently, " + self.name + " tried to steal something from " + target.name + " but was caught in the act. "), False, locations, players)

    def KILL(self, target, report, time, locations, players):
        if self.location is not target.location:    #In the right place?
            self.LOITER(self.location, locations, players)
            return
        if target.alive is False:                   #Target alive?
            self.message += str("While looking to kill them, you find " + target.name + "'s body on the floor. ")
            self.LOITER(self.location, locations, players)
            return
        defend = doTheyDefend(self, target)         #Target defends?
        if defend is "pass":
            self.message += str("You approach " + target.name + " carefully with intent to kill, but suddenly notice how strong they are compared to you. Intimidated, you back off and decide to wait for a better moment. ")
            self.LOITER(self.location, locations, players)
            return

        if self.currentWeapon.type is "blunt":      #Blunt weapon fight
            self.marks.append("bruises")
            target.marks.append("bruises")
            if self.strength > target.strength:
                target.alive = False
                report += str(target.name + " has been killed by " + self.name + " in " + target.location.name + " at " + time + " with " + self.currentWeapon.name + ". Their rank was " + target.rank + ", their strength was " + target.strength + ", their intellect was " + target.intellect + ", their nerves was " + target.nerves + ", their weapon was " + target.weapon.name + ", and their shift was " + target.shift.name + ". ")
                self.honor = self.honor - target.honor
                if self.honor is 0 and target.honor < 0:
                    self.honor = 1
                if self.honor is 0 and target.honor > 0:
                    self.honor = -1
                self.message += str("You catch " + target.name + " off guard and bash their skull in with " + self.currentWeapon.name + ". ")
                target.message += str(self.name + " catches you off guard and bashes your skull in with " + self.currentWeapon.name + ". Unless contradicted by future information, you are dead. You may no longer discuss the game with other players or communicate any game relevant details.")
                whoHere(self, target, str(self.name + " bashes " + target.name + "'s skull in with " + self.currentWeapon.name + ", killing them. "), False, locations, players)
                return
            else:
                target.message += str(self.name + " comes at you with " + self.currentWeapon.name + " in an attempt to bash your head in. Stronger than them, you survive the scuffle that follows, albeit with a few bruises.")
                self.message += str("You attempt to bash " + target.name + "'s head in with your " + self.currentWeapon.name + ", but their too strong and survive the scuffle that follows with only a few bruises.")
                whoHere(self, target, str(self.name + " attempts to bash " + target.name + "'s skull in with " + self.currentWeapon.name + ", but their strong enough to resist and make it out with only a few bruises. "), False, locations, players)
                return

        elif self.currentWeapon.type is "medical":  #Medical weapon fight
            self.marks.append("tired")
            target.marks.append("tired")
            if self.intellect > target.intellect:
                target.alive = False
                report += str(target.name + " has been killed by " + self.name + " in " + target.location.name + " at " + time + " with " + self.currentWeapon.name + ". Their rank was " + target.rank + ", their strength was " + target.strength + ", their intellect was " + target.intellect + ", their nerves was " + target.nerves + ", their weapon was " + target.weapon + ", and their shift was " + target.shift + ". ")
                self.honor = self.honor - target.honor
                if self.honor is 0 and target.honor < 0:
                    self.honor = 1
                if self.honor is 0 and target.honor > 0:
                    self.honor = -1
                self.message += str("You outsmart " + target.name + " in a game of wits involving " + self.currentWeapon.name + ", ending in their death. ")
                target.message += str(self.name + " outsmarts you in a game of wits involving " + self.currentWeapon.name + ". Unless contradicted by future information, you are dead. You may no longer discuss the game with other players or communicate any game relevant details.")
                whoHere(self, target, str(self.name + " outsmarts " + target.name + " in a game of wits involving " + self.currentWeapon.name + ", killing them. "), False, locations, players)
                return
            else:
                target.message += str(self.name + " attempts to outsmart you in a game of wits involving " + self.currentWeapon.name + ", but your smarter than them and manage to survive the challenge, though visibly exhausted.")
                self.message += str("You attempt outsmart " + target.name + " in a game of wits involving " + self.currentWeapon.name + ", but their too smart and survive the challenge, though visibly exhausted.")
                whoHere(self, target, str(self.name + " attempts to outsmart " + target.name + " in a game of wits involving " + self.currentWeapon.name + ", but their smart enough to win and make it out alive. "), False, locations, players)
                return

        elif self.currentWeapon.type is "sharp":    #Sharp weapon fight
            self.marks.append("cuts")
            target.marks.append("cuts")
            if self.nerves > target.nerves:
                target.alive = False
                report += str(target.name + " has been killed by " + self.name + " in " + target.location.name + " at " + time + " with " + self.currentWeapon.name + ". Their rank was " + target.rank + ", their strength was " + target.strength + ", their intellect was " + target.intellect + ", their nerves was " + target.nerves + ", their weapon was " + target.weapon + ", and their shift was " + target.shift + ". ")
                self.honor = self.honor - target.honor
                if self.honor is 0 and target.honor < 0:
                    self.honor = 1
                if self.honor is 0 and target.honor > 0:
                    self.honor = -1
                self.message += str("You slice " + target.name + " open with " + self.currentWeapon.name + ", and they bleed to death. ")
                target.message += str(self.name + " slices you open with " + self.currentWeapon.name + ", and you bleed to death. Unless contradicted by future information, you are dead. You may no longer discuss the game with other players or communicate any game relevant details.")
                whoHere(self, target, str(self.name + " slices " + target.name + " open with " + self.currentWeapon.name + ", and they bleed to death. "), False, locations, players)
                return
            else:
                target.message += str(self.name + " attempts to slice you open with " + self.currentWeapon.name + ", but your reflexes are faster than theirs and you manage to survive the ordeal with only some cuts.")
                self.message += str("You attempt to slice " + target.name + " open with " + self.currentWeapon.name + ", but their reflexes are faster than yours and they manage to survive the ordeal with only some cuts.")
                whoHere(self, target, str(self.name + " attempts to slice " + target.name + " open with " + self.currentWeapon.name + ", but their reflexes are faster than theirs and they manage to survive the ordeal with only some cuts."), False, locations, players)
                return
            
        else:
            self.message += str("Just as you're approaching " + target.name + " to attempt to kill them, you reach into your pocket and realize you have no weapon! ")
            self.LOITER(self.location, locations, players)
