from Functions import whoHere

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

    def DEAD(self, players):
        witnesses = whoHere(self, players)
        for w in range(len(witnesses)):
            witnesses[w].message += str(self.name + "'s body lies montionless on the floor. ")

    def DEFEND(self, players):
        if self.alive is False:
            self.DEAD(players)
            return

        self.message += str("For the duration of the hour, you stay alert to any potencial threat. ")
        witnesses = whoHere(self, players)
        for w in range(len(witnesses)):
            witnesses[w].message += str(self.name + " was alert and on their guard. ")

    def REST(self, locations, players):
        if self.alive is False:
            self.DEAD(players)
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
            self.DEAD(players)
            return
        if self.location is not room:
            self.message += str("Instead of working at " + room.name + ", ")
            self.LOITER(self.location, locations, players)
            return

        if self.location is locations[0]:   #Barraks
            locations[0].workload = locations[0].workload - 1
            self.message += str("You spend the hour collecting dirty sheets and restocking sleeping supplies. ")
            witnesses = whoHere(self, players)
            for w in range(len(witnesses)):
                witnesses[w].message += str(self.name + " spent the hour collecting dirty sheet and restocking sleeping supplies. ")
        if self.location is locations[1]:   #Sanitation
            locations[1].workload = locations[1].workload - 1
            self.message += str("You spend the hour throwing piled up garbage into the incinerator. ")
            witnesses = whoHere(self, players)
            for w in range(len(witnesses)):
                witnesses[w].message += str(self.name + " spent the hour throwing piled up garbage into the incinerator. ")
        if self.location is locations[2]:   #Gymnasium
            locations[2].workload = locations[2].workload - 1
            self.message += str("You spend the hour organzing weights and cleaning debris off the track. ")
            witnesses = whoHere(self, players)
            for w in range(len(witnesses)):
                witnesses[w].message += str(self.name + " spent the hour organzing weights and cleaning debris off the track. ")
        if self.location is locations[3]:   #Medical
            locations[3].workload = locations[3].workload - 1
            self.message += str("You spend the hour restocking medical supplies and preping the equipment for procedures. ")
            witnesses = whoHere(self, players)
            for w in range(len(witnesses)):
                witnesses[w].message += str(self.name + " spent the hour retsocking medical supplies and preping the equipment for procedures. ")
        if self.location is locations[4]:   #Library
            locations[4].workload = locations[4].workload - 1
            self.message += str("You spend the hour organzing and logging books. ")
            witnesses = whoHere(self, players)
            for w in range(len(witnesses)):
                witnesses[w].message += str(self.name + " spent the hour organzing and logging books. ")
        if self.location is locations[5]:   #Information
            locations[5].workload = locations[5].workload - 1
            self.message += str("You spend the hour filing records and debuging the computers. ")
            witnesses = whoHere(self, players)
            for w in range(len(witnesses)):
                witnesses[w].message += str(self.name + " spent the hour filing records and debuging the computers. ")
        if self.location is locations[6]:   #Bathhouse
            locations[6].workload = locations[6].workload - 1
            self.message += str("You spend the hour cleaning the sauna and preping the heating systems. ")
            witnesses = whoHere(self, players)
            for w in range(len(witnesses)):
                witnesses[w].message += str(self.name + " spent the hour cleaning the sauna and preping the heating systems. ")
        if self.location is locations[7]:   #Communications
            locations[7].workload = locations[7].workload - 1
            self.message += str("You spend the hour debuging the communications systems and trying to fix the connection to the capital, to no avail. ")
            witnesses = whoHere(self, players)
            for w in range(len(witnesses)):
                witnesses[w].message += str(self.name + " spent the hour debuging the communications systems and trying to fix the connection to the capital, to no avail. ")
        if self.location is locations[8]:   #Power
            locations[8].workload = locations[8].workload - 1
            self.message += str("You spend the hour working on the generator and wiring the base's electrical systems. ")
            witnesses = whoHere(self, players)
            for w in range(len(witnesses)):
                witnesses[w].message += str(self.name + " spent the hour working on the generator and wiring the base's electrical systems. ")
        if self.location is locations[9]:   #Armaments
            locations[9].workload = locations[9].workload - 1
            self.message += str("You spend the hour logging and properly locking up the base's supply of weapons. ")
            witnesses = whoHere(self, players)
            for w in range(len(witnesses)):
                witnesses[w].message += str(self.name + " spent the hour logging and properly locking up the base's supply of weapons. ")
        if self.location is locations[10]:  #Security
            locations[10].workload = locations[10].workload - 1
            self.message += str("You spend the hour working on the base's security systems. ")
            witnesses = whoHere(self, players)
            for w in range(len(witnesses)):
                witnesses[w].message += str(self.name + " spent the hour working on the base's security systems. ")
        if self.location is locations[11]:  #Command
            locations[11].workload = locations[11].workload - 1
            self.message += str("You spend the hour allocating shifts and assigning future work. ")
            witnesses = whoHere(self, players)
            for w in range(len(witnesses)):
                witnesses[w].message += str(self.name + " spent the hour allocating shifts and assigning future work. ")

    def SABOTAGE(self, room, locations, players):
        if self.alive is False:
            self.DEAD(players)
            return
        if self.location is not room:
            self.message += str("Instead of sabotaging " + room.name + ", ")
            self.LOITER(self.location, locations, players)
            return

        if self.location is locations[0]:   #Barraks
            locations[0].sabotages = locations[0].sabotages + 1
            self.message += str("You spend the hour tossing perfectly clean sheets and stocking the supplies incorrectly. ")
            witnesses = whoHere(self, players)
            for w in range(len(witnesses)):
                witnesses[w].message += str(self.name + " spent the hour collecting dirty sheet and restocking sleeping supplies. ")
        if self.location is locations[1]:   #Sanitation
            locations[1].sabotages = locations[1].sabotages + 1
            self.message += str("You spend the hour improperly using the incinerator in an attempt to break it. ")
            witnesses = whoHere(self, players)
            for w in range(len(witnesses)):
                witnesses[w].message += str(self.name + " spent the hour throwing piled up garbage into the incinerator. ")
        if self.location is locations[2]:   #Gymnasium
            locations[2].sabotages = locations[2].sabotages + 1
            self.message += str("You spend the hour hiding the weights and making a mess of the track. ")
            witnesses = whoHere(self, players)
            for w in range(len(witnesses)):
                witnesses[w].message += str(self.name + " spent the hour organzing weights and cleaning debris off the track. ")
        if self.location is locations[3]:   #Medical
            locations[3].sabotages = locations[3].sabotages + 1
            self.message += str("You spend the hour replacing the labels on various medical supplies and messing with the procedure equipment. ")
            witnesses = whoHere(self, players)
            for w in range(len(witnesses)):
                witnesses[w].message += str(self.name + " spent the hour restocking medical supplies and preping the equipment for procedures. ")
        if self.location is locations[4]:   #Library
            locations[4].sabotages = locations[4].sabotages + 1
            self.message += str("You spend the hour misplacing books and ripping random pages out. ")
            witnesses = whoHere(self, players)
            for w in range(len(witnesses)):
                witnesses[w].message += str(self.name + " spent the hour organzing and logging books. ")
        if self.location is locations[5]:   #Information
            locations[5].sabotages = locations[5].sabotages + 1
            self.message += str("You spend the hour messing with the computers and misplacing files. ")
            witnesses = whoHere(self, players)
            for w in range(len(witnesses)):
                witnesses[w].message += str(self.name + " spent the hour filing records and debuging the computers. ")
        if self.location is locations[6]:   #Bathhouse
            locations[6].sabotages = locations[6].sabotages + 1
            self.message += str("You spend the hour messing with the heating systems. ")
            witnesses = whoHere(self, players)
            for w in range(len(witnesses)):
                witnesses[w].message += str(self.name + " spent the hour cleaning the sauna and preping the heating systems. ")
        if self.location is locations[7]:   #Communications
            locations[7].sabotages = locations[7].sabotages + 1
            self.message += str("You spend the hour messing with the communications systems. ")
            witnesses = whoHere(self, players)
            for w in range(len(witnesses)):
                witnesses[w].message += str(self.name + " spent the hour debuging the communications systems and trying to fix the connection to the capital, to no avail. ")
        if self.location is locations[8]:   #Power
            locations[8].sabotages = locations[8].sabotages + 1
            self.message += str("You spend the hour messing with the generator and trying to screw up the base's electrical systems. ")
            witnesses = whoHere(self, players)
            for w in range(len(witnesses)):
                witnesses[w].message += str(self.name + " spent the hour working on the generator and wiring the base's electrical systems. ")
        if self.location is locations[9]:   #Armaments
            locations[9].sabotages = locations[9].sabotages + 1
            self.message += str("You spend the hour improperly locking up weapons. ")
            witnesses = whoHere(self, players)
            for w in range(len(witnesses)):
                witnesses[w].message += str(self.name + " spent the hour logging and properly locking up the base's supply of weapons. ")
        if self.location is locations[10]:  #Security
            locations[10].sabotages = locations[10].sabotages + 1
            self.message += str("You spend the hour messing with the base's security systems. ")
            witnesses = whoHere(self, players)
            for w in range(len(witnesses)):
                witnesses[w].message += str(self.name + " spent the hour working on the base's security systems. ")
        if self.location is locations[11]:  #Command
            locations[11].sabotages = locations[11].sabotages + 1
            self.message += str("You spend the hour misallocating shifts and misplacing important work documents. ")
            witnesses = whoHere(self, players)
            for w in range(len(witnesses)):
                witnesses[w].message += str(self.name + " spent the hour allocating shifts and assigning future work. ")

    def LOITER(self, room, locations, players):
        if self.alive is False:
            self.DEAD(players)
            return
        if self.location is not room:
            self.message += str("Instead of loitering in " + room.name + ", ")
            self.LOITER(self.location, locations, players)
            return

        if self.location is locations[0]:   #Barraks
            self.message += str("You spend the hour lying in bed, watching to see if you can spot anything intresting. ")
            witnesses = whoHere(self, players)
            for w in range(len(witnesses)):
                witnesses[w].message += str(self.name + " spent the hour lying in bed, relaxing. ")
        if self.location is locations[1]:   #Sanitation
            self.message += str("You spend the hour leaning against the incinerator, watching to see if you can spot anything intresting. ")
            witnesses = whoHere(self, players)
            for w in range(len(witnesses)):
                witnesses[w].message += str(self.name + " spent the hour leaning against the incinerator, relaxing. ")
        if self.location is locations[2]:   #Gymnasium
            self.message += str("You spend the hour relaxing on weight bench, watching to see if you can spot anything intresting. ")
            witnesses = whoHere(self, players)
            for w in range(len(witnesses)):
                witnesses[w].message += str(self.name + " spent the hour relaxing on weight bench. ")
        if self.location is locations[3]:   #Medical
            self.message += str("You spend the hour relaxing on a gurney, watching to see if you can spot anything intresting. ")
            witnesses = whoHere(self, players)
            for w in range(len(witnesses)):
                witnesses[w].message += str(self.name + " spent the hour relaxing on a gurney. ")
        if self.location is locations[4]:   #Library
            self.message += str("You spend the hour casually perusing bookshelves, watching to see if you can spot anything intresting. ")
            witnesses = whoHere(self, players)
            for w in range(len(witnesses)):
                witnesses[w].message += str(self.name + " spent the hour casually perusing bookshelves. ")
        if self.location is locations[5]:   #Information
            self.message += str("You spend the hour perched ontop of a filing cabinet, watching to see if you can spot anything intresting. ")
            witnesses = whoHere(self, players)
            for w in range(len(witnesses)):
                witnesses[w].message += str(self.name + " spent the hour perched ontop of a filing cabinet, relaxing. ")
        if self.location is locations[6]:   #Bathhouse
            self.message += str("You spend the hour floating relaxingly in the pool, watching to see if you can spot anything intresting. ")
            witnesses = whoHere(self, players)
            for w in range(len(witnesses)):
                witnesses[w].message += str(self.name + " spent the hour floating in the pool, relaxing. ")
        if self.location is locations[7]:   #Communications
            self.message += str("You spend the hour admiring the complicated display of communcation data and watching to see if you can spot anything intresting. ")
            witnesses = whoHere(self, players)
            for w in range(len(witnesses)):
                witnesses[w].message += str(self.name + " spent the hour admiring the complicated display of communcation data, relaxing. ")
        if self.location is locations[8]:   #Power
            self.message += str("You spend the hour listening to the relaxing hum of the generator, watching to see if you can spot anything intresting. ")
            witnesses = whoHere(self, players)
            for w in range(len(witnesses)):
                witnesses[w].message += str(self.name + " spent the hour listening to the relaxing hum of the generator. ")
        if self.location is locations[9]:   #Armaments
            self.message += str("You spend the hour admiring the base's large collection of deadly weapons, watching to see if you can spot anything intresting. ")
            witnesses = whoHere(self, players)
            for w in range(len(witnesses)):
                witnesses[w].message += str(self.name + " spent the hour admiring the base's large collection of deadly weapons. ")
        if self.location is locations[10]:  #Security
            self.message += str("You spend the hour fiddling aimlessly with camera equipment and watching to see if you can spot anything intresting. ")
            witnesses = whoHere(self, players)
            for w in range(len(witnesses)):
                witnesses[w].message += str(self.name + " spent the hour fiddling aimlessly with camera equipment, relaxing. ")
        if self.location is locations[11]:  #Command
            self.message += str("You spend the hour relaxing in a desk chair and watching to see if you can spot anything intresting. ")
            witnesses = whoHere(self, players)
            for w in range(len(witnesses)):
                witnesses[w].message += str(self.name + " spent the hour relaxing in a desk chair. ")

    def WATCH(self, locations, players):
        if self.alive is False:
            self.DEAD(players)
            return
        self.LOITER(self.location, locations, players)
        
    def STEAL(self, target, locations, players):

    def KILL(self, target, report, time):
        if self.location is not target.location:
            self.LOITER(self.location, locations, players)
            return
        if target.alive is False:
            self.message += str("While looking to kill them, you find " + target.name + "'s body on the floor. ")
            self.LOITER(self.location, locations, players)
            return

        #Deal with defending
        if target.commands[h][0] is "DEFEND":
            self.message += str("Unfortunatly, " + target.name + " is totally alert when you had intended on killing them, ")
            return

        #FIGHT!

        #Blunt
        if self.currentWeapon.type is "blunt":
            self.marks.append("bruises")
            target.marks.append("bruises")

            #Wins
            if self.strength > target.strength:
                target.alive = False
                report += str(target.name + " has been killed by " + self.name + " in " + target.location + " at " + time + " with " + self.weapon + ". His rank was " + target.rank + ", his strength was " + target.strength + ", his intellect was " + target.intellect + ", his nerves was " + target.nerves + ", his weapon was " + target.weapon + ", and his shift was " + target.shift + ". ")
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
        elif self.currentWeapon.type is "medical":

            #Wins
            if self.intellect > target.intellect:
                target.alive = False
                report += str(target.name + " has been killed by " + self.name + " in " + target.location + " at " + time + " with " + self.weapon + ". His rank was " + target.rank + ", his strength was " + target.strength + ", his intellect was " + target.intellect + ", his nerves was " + target.nerves + ", his weapon was " + target.weapon + ", and his shift was " + target.shift + ". ")
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
            self.marks.append("cuts")
            target.marks.append("cuts")

            #Wins
            if self.nerves > target.nerves:
                target.alive = False
                report += str(target.name + " has been killed by " + self.name + " in " + target.location + " at " + time + " with " + self.weapon + ". His rank was " + target.rank + ", his strength was " + target.strength + ", his intellect was " + target.intellect + ", his nerves was " + target.nerves + ", his weapon was " + target.weapon + ", and his shift was " + target.shift + ". ")
                self.honor = self.honor - target.honor
                if self.honor is 0:
                    self.honor = -1
                target.message += str(self.name + " catches you off guard and stabs you with " + self.currentWeapon + ". Unless contradicted by future information, you are dead. You may no longer discuss the game with other players or communicate any game relevant details.")
                witnesses = []
                return

            #Loses
            else:
                target.message += str(self.name + " tries to stab you with " + self.weapon + ", but your reaction time is quicker than theirs and you survive.")
                self.message += str("You try to stab " + target.name + " with your " + self.currentWeapon + ", but he's too quick, survives the attempt. ")
                return
