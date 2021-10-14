from os import name
import random
import sys
from Functions import doTheyDefend, freeRest, whoHere, workload, bloodFeud

class Player:
    def __init__(self, name, rank, strength, intellect, nerves, weapon, enteredShift, location):

        #Game Rules
        self.debug = True
        self.ran = True

        self.name = name
        self.rank = rank
        self.infRank = "none"
        self.strength = strength
        self.infStrength = "none"
        self.intellect = intellect
        self.infIntellect = "none"
        self.nerves = nerves
        self.infNerves = "none"
        self.weapon = weapon
        self.infWeapon = "none"
        self.enteredShift = enteredShift
        self.location = location
        self.shift = "shift"
        self.infShift = "none"
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
        self.accusers = []
        self.requiredWork = 2
        self.requiredSleep = 4
        self.sabotage = False
        self.trueName = name

        if self.ran == True:
            self.shift = self.enteredShift

    def DEAD(self, locations, players, weapons):
        if players[0].debug == True:
            print(self.trueName + " is dead in " + self.location.name + ". ")
        whoHere(self, "none", str(self.name + "'s body lies montionless on the floor. "), str(self.trueName + "'s body lies montionless on the floor. "), True, locations, players , weapons)

    def REST(self, locations, players, weapons):
        if self.alive == False:
            self.DEAD(locations, players, weapons)
            return
        if players[0].debug == True and self.location != locations[0]:
            print(self.trueName + " is resting in " + self.location.name + ". ")
        

        if self.location == locations[0]:   #Barraks
            self.location.visit(self, locations, players, weapons)
        if self.location == locations[1]:   #Sanitation
            self.message += str("You nod off as far from the incinerator as you can get and manage to get a decent hour of rest in. ")
            whoHere(self, "none", str(self.name + " was sleeping as far from the incinerator as they could get. "), str(self.trueName + " was sleeping as far from the incinerator as they could get. "), False, locations, players, weapons)
            freeRest(self, weapons)
        if self.location == locations[2]:   #Gymnasium
            self.message += str("You nod off on one of the weight benches and manage to get a decent hour of rest in. ")
            whoHere(self, "none", str(self.name + " was sleeping on one of the weight benches. "), str(self.trueName + " was sleeping on one of the weight benches. "), False, locations, players, weapons)
            freeRest(self, weapons)
        if self.location == locations[3]:   #Medical
            self.message += str("You nod off on a gurney and manage to get a decent hour of rest. ")
            whoHere(self, "none", str(self.name + " was sleeping on a gurney. "), str(self.trueName + " was sleeping on a gurney. "), False, locations, players, weapons)
            freeRest(self, weapons)
        if self.location == locations[4]:   #Library
            self.message += str("You nod off behind one of the bookshelves and manage to get a decent hour of rest in. ")
            whoHere(self, "none", str(self.name + " was sleeping behind one of the bookshelves. "), str(self.trueName + " was sleeping behind one of the bookshelves. "), False, locations, players, weapons)
            freeRest(self, weapons)
        if self.location == locations[5]:   #Information
            self.message += str("You nod off between two fileing cabinets and manage to get a decent hour of rest in. ")
            whoHere(self, "none", str(self.name + " was sleeping between two fileing cabinets. "), str(self.trueName + " was sleeping between two fileing cabinets. "), False, locations, players, weapons)
            freeRest(self, weapons)
        if self.location == locations[6]:   #Bathhouse
            self.message += str("You nod off in one of the pool chairs and manage to get a decent hour of rest in. ")
            whoHere(self, "none", str(self.name + " was sleeping in one of the pool chairs. "), str(self.trueName + " was sleeping in one of the pool chairs. "), False, locations, players, weapons)
            freeRest(self, weapons)
        if self.location == locations[7]:   #Communications
            self.message += str("You nod off leaning forward against a communications monitor and manage to get a decent hour of rest in. ")
            whoHere(self, "none", str(self.name + " was leaning foward, asleep, against one of the communications monitors. "), str(self.trueName + " was leaning foward, asleep, against one of the communications monitors. "), False, locations, players, weapons)
            freeRest(self, weapons)
        if self.location == locations[8]:   #Power
            self.message += str("You nod off against the wall as far from the generator as you can get and manage to get a decent hour of rest in. ")
            whoHere(self, "none", str(self.name + " was sleeping against the wall as far from the generator as they could get. "), str(self.trueName + " was sleeping against the wall as far from the generator as they could get. "), False, locations, players, weapons)
            freeRest(self, weapons)
        if self.location == locations[9]:   #Armaments
            self.message += str("You nod off against the glass case that stores the weapons and manage to get a decent hour of rest in. ")
            whoHere(self, "none", str(self.name + " was sleeping against the glass case that stores the weapons. "), str(self.trueName + " was sleeping against the glass case that stores the weapons. "), False, locations, players, weapons)
            freeRest(self, weapons)
        if self.location == locations[10]:  #Security
            self.message += str("You nod off in one of the security guard's swiveling chairs and manage to get a decent hour of rest in. ")
            whoHere(self, "none", str(self.name + " was sleeping in one of the security guard's swiveling chairs. "), str(self.trueName + " was sleeping in one of the security guard's swiveling chairs. "), False, locations, players, weapons)
            freeRest(self, weapons)
        if self.location == locations[11]:  #Command
            self.message += str("You nod off in a desk chair and manage to get a decent hour of rest in. ")
            whoHere(self, "none", str(self.name + " was sleeping in a desk chair. "), str(self.trueName + " was sleeping in a desk chair. "), False, locations, players, weapons)
            freeRest(self, weapons)

    def WORK(self, room, locations, players, weapons):
        if self.alive == False:
            self.DEAD(locations, players, weapons)
            return
        if self.location != room:
            self.message += str("Instead of working at " + room.name + ", ")
            self.LOITER(self.location, locations, players, weapons)
            return
        if players[0].debug == True:
            print(self.trueName + " is working in " + self.location.name + ". ")

        if self.location == locations[0]:   #Barraks
            workload(self, locations[0], weapons)
            self.message += str("You spend the hour collecting dirty sheets and restocking sleeping supplies. ")
            whoHere(self, "none", str(self.name + " spent the hour collecting dirty sheet and restocking sleeping supplies. "), str(self.trueName + " spent the hour collecting dirty sheet and restocking sleeping supplies. "), False, locations, players, weapons)
        if self.location == locations[1]:   #Sanitation
            workload(self, locations[1], weapons)
            self.message += str("You spend the hour throwing piled up garbage into the incinerator. ")
            whoHere(self, "none", str(self.name + " spent the hour throwing piled up garbage into the incinerator. "), str(self.trueName + " spent the hour throwing piled up garbage into the incinerator. "), False, locations, players, weapons)
        if self.location == locations[2]:   #Gymnasium
            workload(self, locations[2], weapons)
            self.message += str("You spend the hour organzing weights and cleaning debris off the track. ")
            whoHere(self, "none", str(self.name + " spent the hour organzing weights and cleaning debris off the track. "), str(self.trueName + " spent the hour organzing weights and cleaning debris off the track. "), False, locations, players, weapons)
        if self.location == locations[3]:   #Medical
            workload(self, locations[3], weapons)
            self.message += str("You spend the hour restocking medical supplies and preping the equipment for procedures. ")
            whoHere(self, "none", str(self.name + " spent the hour retsocking medical supplies and preping the equipment for procedures. "), str(self.trueName + " spent the hour retsocking medical supplies and preping the equipment for procedures. "), False, locations, players, weapons)
        if self.location == locations[4]:   #Library
            workload(self, locations[4], weapons)
            self.message += str("You spend the hour organzing and logging books. ")
            whoHere(self, "none", str(self.name + " spent the hour organzing and logging books. "), str(self.trueName + " spent the hour organzing and logging books. "), False, locations, players, weapons)
        if self.location == locations[5]:   #Information
            workload(self, locations[5], weapons)
            self.message += str("You spend the hour filing records and debuging the computers. ")
            whoHere(self, "none", str(self.name + " spent the hour filing records and debuging the computers. "), str(self.trueName + " spent the hour filing records and debuging the computers. "), False, locations, players, weapons)
        if self.location == locations[6]:   #Bathhouse
            workload(self, locations[6], weapons)
            self.message += str("You spend the hour cleaning the sauna and preping the heating systems. ")
            whoHere(self, "none", str(self.name + " spent the hour cleaning the sauna and preping the heating systems. "), str(self.trueName + " spent the hour cleaning the sauna and preping the heating systems. "), False, locations, players, weapons)
        if self.location == locations[7]:   #Communications
            workload(self, locations[7], weapons)
            self.message += str("You spend the hour debuging the communications systems and trying to fix the connection to the capital, to no avail. ")
            whoHere(self, "none", str(self.name + " spent the hour debuging the communications systems and trying to fix the connection to the capital, to no avail. "), str(self.trueName + " spent the hour debuging the communications systems and trying to fix the connection to the capital, to no avail. "), False, locations, players, weapons)
        if self.location == locations[8]:   #Power
            workload(self, locations[8], weapons)
            self.message += str("You spend the hour working on the generator and wiring the base's electrical systems. ")
            whoHere(self, "none", str(self.name + " spent the hour working on the generator and wiring the base's electrical systems. "), str(self.trueName + " spent the hour working on the generator and wiring the base's electrical systems. "), False, locations, players, weapons)
        if self.location == locations[9]:   #Armaments
            workload(self, locations[9], weapons)
            self.message += str("You spend the hour logging and properly locking up the base's supply of weapons. ")
            whoHere(self, "none", str(self.name + " spent the hour logging and properly locking up the base's supply of weapons. "), str(self.trueName + " spent the hour logging and properly locking up the base's supply of weapons. "), False, locations, players, weapons)
        if self.location == locations[10]:  #Security
            workload(self, locations[10], weapons)
            self.message += str("You spend the hour working on the base's security systems. ")
            whoHere(self, "none", str(self.name + " spent the hour working on the base's security systems. "), str(self.trueName + " spent the hour working on the base's security systems. "), False, locations, players, weapons)
        if self.location == locations[11]:  #Command
            workload(self, locations[11], weapons)
            self.message += str("You spend the hour allocating shifts and assigning future work. ")
            whoHere(self, "none", str(self.name + " spent the hour allocating shifts and assigning future work. "), str(self.trueName + " spent the hour allocating shifts and assigning future work. "), False, locations, players, weapons)

    def SABOTAGE(self, room, locations, players, weapons):
        if self.alive == False:
            self.DEAD(locations, players, weapons)
            return
        if self.weapon == weapons[2]:
            self.message += str("You hack into " + room.name + "'s hardware and screw around with it. ")
            room.sabotages = room.sabotages + 1
            self.LOITER(self.location, locations, players, weapons)
            return
        if self.location != room:
            self.message += str("Instead of sabotaging " + room.name + ", ")
            self.LOITER(self.location, locations, players, weapons)
            return
        if players[0].debug == True:
            print(self.trueName + " is sabotaging in " + self.location.name + ". ")

        if self.location == locations[0]:   #Barraks
            locations[0].sabotages = locations[0].sabotages + 1
            self.message += str("You spend the hour tossing perfectly clean sheets and stocking the supplies incorrectly. ")
            whoHere(self, "none", str(self.name + " spent the hour collecting dirty sheet and restocking sleeping supplies. "), str(self.trueName + " spent the hour collecting dirty sheet and restocking sleeping supplies. "), False, locations, players, weapons)
        if self.location == locations[1]:   #Sanitation
            locations[1].sabotages = locations[1].sabotages + 1
            self.message += str("You spend the hour improperly using the incinerator in an attempt to break it. ")
            whoHere(self, "none", str(self.name + " spent the hour throwing piled up garbage into the incinerator. "), str(self.trueName + " spent the hour throwing piled up garbage into the incinerator. "), False, locations, players, weapons)
        if self.location == locations[2]:   #Gymnasium
            locations[2].sabotages = locations[2].sabotages + 1
            self.message += str("You spend the hour hiding the weights and making a mess of the track. ")
            whoHere(self, "none", str(self.name + " spent the hour organzing weights and cleaning debris off the track. "), str(self.trueName + " spent the hour organzing weights and cleaning debris off the track. "), False, locations, players, weapons)
        if self.location == locations[3]:   #Medical
            locations[3].sabotages = locations[3].sabotages + 1
            self.message += str("You spend the hour replacing the labels on various medical supplies and messing with the procedure equipment. ")
            whoHere(self, "none", str(self.name + " spent the hour restocking medical supplies and preping the equipment for procedures. "), str(self.trueName + " spent the hour restocking medical supplies and preping the equipment for procedures. "), False, locations, players, weapons)
        if self.location == locations[4]:   #Library
            locations[4].sabotages = locations[4].sabotages + 1
            self.message += str("You spend the hour misplacing books and ripping random pages out. ")
            whoHere(self, "none", str(self.name + " spent the hour organzing and logging books. "), str(self.trueName + " spent the hour organzing and logging books. "), False, locations, players, weapons)
        if self.location == locations[5]:   #Information
            locations[5].sabotages = locations[5].sabotages + 1
            self.message += str("You spend the hour messing with the computers and misplacing files. ")
            whoHere(self, "none", str(self.name + " spent the hour filing records and debuging the computers. "), str(self.trueName + " spent the hour filing records and debuging the computers. "), False, locations, players, weapons)
        if self.location == locations[6]:   #Bathhouse
            locations[6].sabotages = locations[6].sabotages + 1
            self.message += str("You spend the hour messing with the heating systems. ")
            whoHere(self, "none", str(self.name + " spent the hour cleaning the sauna and preping the heating systems. "), str(self.trueName + " spent the hour cleaning the sauna and preping the heating systems. "), False, locations, players, weapons)
        if self.location == locations[7]:   #Communications
            locations[7].sabotages = locations[7].sabotages + 1
            self.message += str("You spend the hour messing with the communications systems. ")
            whoHere(self, "none", str(self.name + " spent the hour debuging the communications systems and trying to fix the connection to the capital, to no avail. "), str(self.trueName + " spent the hour debuging the communications systems and trying to fix the connection to the capital, to no avail. "), False, locations, players, weapons)
        if self.location == locations[8]:   #Power
            locations[8].sabotages = locations[8].sabotages + 1
            self.message += str("You spend the hour messing with the generator and trying to screw up the base's electrical systems. ")
            whoHere(self, "none", str(self.name + " spent the hour working on the generator and wiring the base's electrical systems. "), str(self.trueName + " spent the hour working on the generator and wiring the base's electrical systems. "), False, locations, players, weapons)
        if self.location == locations[9]:   #Armaments
            locations[9].sabotages = locations[9].sabotages + 1
            self.message += str("You spend the hour improperly locking up weapons. ")
            whoHere(self, "none", str(self.name + " spent the hour logging and properly locking up the base's supply of weapons. "), str(self.trueName + " spent the hour logging and properly locking up the base's supply of weapons. "), False, locations, players, weapons)
        if self.location == locations[10]:  #Security
            locations[10].sabotages = locations[10].sabotages + 1
            self.message += str("You spend the hour messing with the base's security systems. ")
            whoHere(self, "none", str(self.name + " spent the hour working on the base's security systems. "), str(self.trueName + " spent the hour working on the base's security systems. "), False, locations, players, weapons)
        if self.location == locations[11]:  #Command
            locations[11].sabotages = locations[11].sabotages + 1
            self.message += str("You spend the hour misallocating shifts and misplacing important work documents. ")
            whoHere(self, "none", str(self.name + " spent the hour allocating shifts and assigning future work. "), str(self.trueName + " spent the hour allocating shifts and assigning future work. "), False, locations, players, weapons)

    def LOITER(self, room, locations, players, weapons):
        if self.alive == False:
            self.DEAD(locations, players, weapons)
            return
        if self.location != room:
            self.message += str("Instead of loitering in " + room.name + ", ")
            self.LOITER(self.location, locations, players, weapons)
            return
        if players[0].debug == True:
            print(self.trueName + " is loitering in " + self.location.name + ". ")

        if self.location == locations[0]:   #Barraks
            self.message += str("You spend the hour lying in bed, watching to see if you can spot anything intresting. ")
            whoHere(self, "none", str(self.name + " spent the hour lying in bed, relaxing. "), str(self.trueName + " spent the hour lying in bed, relaxing. "), False, locations, players, weapons)
        if self.location == locations[1]:   #Sanitation
            self.message += str("You spend the hour leaning against the incinerator, watching to see if you can spot anything intresting. ")
            whoHere(self, "none", str(self.name + " spent the hour leaning against the incinerator, relaxing. "), str(self.trueName + " spent the hour leaning against the incinerator, relaxing. "), False, locations, players, weapons)
        if self.location == locations[2]:   #Gymnasium
            self.message += str("You spend the hour relaxing on weight bench, watching to see if you can spot anything intresting. ")
            whoHere(self, "none", str(self.name + " spent the hour relaxing on weight bench. "), str(self.trueName + " spent the hour relaxing on weight bench. "), False, locations, players, weapons)
        if self.location == locations[3]:   #Medical
            self.message += str("You spend the hour relaxing on a gurney, watching to see if you can spot anything intresting. ")
            whoHere(self, "none", str(self.name + " spent the hour relaxing on a gurney. "), str(self.trueName + " spent the hour relaxing on a gurney. "), False, locations, players, weapons)
        if self.location == locations[4]:   #Library
            self.message += str("You spend the hour casually perusing bookshelves, watching to see if you can spot anything intresting. ")
            whoHere(self, "none", str(self.name + " spent the hour casually perusing bookshelves. "), str(self.trueName + " spent the hour casually perusing bookshelves. "), False, locations, players, weapons)
        if self.location == locations[5]:   #Information
            self.message += str("You spend the hour perched ontop of a filing cabinet, watching to see if you can spot anything intresting. ")
            whoHere(self, "none", str(self.name + " spent the hour perched ontop of a filing cabinet, relaxing. "), str(self.trueName + " spent the hour perched ontop of a filing cabinet, relaxing. "), False, locations, players, weapons)
        if self.location == locations[6]:   #Bathhouse
            self.message += str("You spend the hour floating relaxingly in the pool, watching to see if you can spot anything intresting. ")
            whoHere(self, "none", str(self.name + " spent the hour floating in the pool, relaxing. "), str(self.trueName + " spent the hour floating in the pool, relaxing. "), False, locations, players, weapons)
        if self.location == locations[7]:   #Communications
            self.message += str("You spend the hour admiring the complicated display of communcation data and watching to see if you can spot anything intresting. ")
            whoHere(self, "none", str(self.name + " spent the hour admiring the complicated display of communcation data, relaxing. "), str(self.trueName + " spent the hour admiring the complicated display of communcation data, relaxing. "), False, locations, players, weapons)
        if self.location == locations[8]:   #Power
            self.message += str("You spend the hour listening to the relaxing hum of the generator, watching to see if you can spot anything intresting. ")
            whoHere(self, "none", str(self.name + " spent the hour listening to the relaxing hum of the generator. "), str(self.trueName + " spent the hour listening to the relaxing hum of the generator. "), False, locations, players, weapons)
        if self.location == locations[9]:   #Armaments
            self.message += str("You spend the hour admiring the base's large collection of deadly weapons, watching to see if you can spot anything intresting. ")
            whoHere(self, "none", str(self.name + " spent the hour admiring the base's large collection of deadly weapons. "), str(self.trueName + " spent the hour admiring the base's large collection of deadly weapons. "), False, locations, players, weapons)
        if self.location == locations[10]:  #Security
            self.message += str("You spend the hour fiddling aimlessly with camera equipment and watching to see if you can spot anything intresting. ")
            whoHere(self, "none", str(self.name + " spent the hour fiddling aimlessly with camera equipment, relaxing. "), str(self.trueName + " spent the hour fiddling aimlessly with camera equipment, relaxing. "), False, locations, players, weapons)
        if self.location == locations[11]:  #Command
            self.message += str("You spend the hour relaxing in a desk chair and watching to see if you can spot anything intresting. ")
            whoHere(self, "none", str(self.name + " spent the hour relaxing in a desk chair. "), str(self.trueName + " spent the hour relaxing in a desk chair. "), False, locations, players, weapons)

    def AMBUSH(self, room, target, locations, players, time, report, weapons):
        if self.alive == False:
            self.DEAD(locations, players, weapons)
            return
        if self.weapon == weapons[11]:
            self.message += str("You flood " + room.name + " with a deadly gas designed specifically to kill " + target.name + ". ")
            target.message += str("You have been killed by neurotoxic gas, because the player with that weapon successfully predicted you would be in " + room.name + " at " + time + ". ")
            target.alive = False

            print(type(target.shift))

            report += str(target.name + " has been ambushed by " + self.name + " in " + target.location.name + " at " + time + ". Their rank was " + str(target.rank) + ", their strength was " + str(target.strength) + ", their intellect was " + str(target.intellect) + ", their nerves was " + str(target.nerves) + ", their weapon was " + target.weapon.name + ", and their shift was " + target.shift.name + ". ")
            self.honor = self.honor - target.honor
            if self.honor == 0 and target.honor < 0:
                self.honor = 1
            if self.honor == 0 and target.honor > 0:
                self.honor = -1
            self.LOITER(self.location, locations, players, weapons)
            return
        if self.location != room:
            self.message += str("Instead of ambushing " + target.name + " in " + room.name + ", ")
            self.LOITER(self.location, locations, players, weapons)
            return
        if self.location != target.location:
            self.message += str("You prepare to ambush " + target.name + ", but they never show. ")
            self.LOITER(self.location, locations, players, weapons)
            return
        if players[0].debug == True:
            print(self.trueName + " has abushed " + target.trueName + " in " + self.location.name + ". ")

        self.message += str("Predicting that " + target.name + " would be in " + target.location.name + " at precisely " + time + ", you use your surrondings to set a trap ahead of their arrival, killing them without any struggle or chance of defense. ")
        target.message += str("Seemingly predicting that you would be in " + target.location.name + " at percisely " + time + ", " + self.name + " set a trap ahead of your arrival, killing you without any struggle or chance of defence. You are now dead, and may no longer talk to other players about the game or communicate any game relavent information. ")
        report += str(target.name + " has been ambushed by " + self.name + " in " + target.location.name + " at " + time + ". Their rank was " + str(target.rank) + ", their strength was " + str(target.strength) + ", their intellect was " + str(target.intellect) + ", their nerves was " + str(target.nerves) + ", their weapon was " + target.weapon.name + ", and their shift was " + target.shift.name + ". ")
        self.honor = self.honor - target.honor
        if self.honor == 0 and target.honor < 0:
            self.honor = 1
        if self.honor == 0 and target.honor > 0:
            self.honor = -1
        there = []
        there = whoHere(self, target, str("You witness " + self.name + " spring a trap on " + target.name + ", killing them without any struggle or chance of defense, seemingly having predicted they would be in " + target.location.name + " at precisely " + time + ". "), str("You witness " + self.trueName + " spring a trap on " + target.trueName + ", killing them without any struggle or chance of defense, seemingly having predicted they would be in " + target.location.name + " at precisely " + time + ". "), False, locations, players, weapons)
        bloodFeud(self, target, there, players, weapons, report, time, locations)
        return

    def ENEMY(self, room, locations, players, weapons, time, report):
        if self.alive == False:
            self.DEAD(locations, players, weapons)
            return
        if self.location != room:
            self.message += str("Instead of attacking The Enemy in " + room.name + ", ")
            self.LOITER(self.location, locations, players, weapons)
            return
        if self.location != players[-1].location:
            self.message += str("You prepare to attack The Enemy, but they never show. ")
            self.LOITER(self.location, locations, players, weapons)
            return
        if players[0].debug == True:
            print(self.trueName + " has abushed The Enemy in " + self.location.name + ". ")
        
        #Has no weapon
        youFailed = False
        self.message += str("Just as you predicted, The Enemy--impersonating " + players[-1].name + "--is in " + room.name + " at exactly the right time. You prepare to attempt to kill them and end this once and for all. ")
        if self.currentWeapon == "none":
            self.message += str("Unfortunatly, in your haste, you had neglected to realize that--for whatever reason--you have no weapon. ")
            youFailed = True

        #Has blunt weapon
        if self.currentWeapon.type == "blunt" and youFailed == False:
            self.message += str("You charge them with " + self.currentWeapon.name + ". ")
            self.marks.append("bruises")
            players[-1].marks.append("bruises")
            if self.strength > players[-1].strength:
                self.message += str("Stronger than them, you bash their head in and their body falls to the ground lifeless. The game is over and the soldiers win. As the hero who killed The Enemy, you win TRUE VICTORY. Congratulations!")
                for p in range(len(players)-1):
                    if players[p] != self:
                        players[p].message += str("In " + room.name + " at " + time + ", " + self.name + " bashed The Enemy's head in with " + self.currentWeapon.name + ", killing them once and for all. All living players win the game, and " + self.name + " wins TRUE VICTORY for having brought it about. Congrats! ")
                print("\n")
                for p in range(len(players)):
                    print(players[p].name + "\n")
                    print(players[p].message + "\n")
                    players[p].message = ""
                    print(players[p].endMessage + "\n \n")
                    players[p].endMessage = ""
                print(report)
                report = ""
                sys.exit()
            else:
                self.message += str("However, they are stronger than you, and after sustaining a few bruises, manage to prevent you from dealing any fatal damage. ")
                youFailed = True
                whoHere(self, players[-1], str(self.name + " attempts to bash " + players[-1].name + "'s head in, but they're strong enough to resist and make it out with only a few bruises. "), str(self.trueName + " attempts to bash " + players[-1].trueName + "'s head in, but they're strong enough to resist and make it out with only a few bruises. "), False, locations, players, weapons)

        #Has medical weapon
        if self.currentWeapon.type == "medical" and youFailed == False:
            self.message += str("You devise a plan to kill them with " + self.currentWeapon.name + ". ")
            self.marks.append("tired")
            players[-1].marks.append("tired")
            if self.intellect > players[-1].intellect:
                self.message += str("Smarter than them, you trick them in a game of wits, and they slump over dead. The game is over and the soldiers win. As the hero who killed The Enemy, you win TRUE VICTORY. Congratulations!")
                for p in range(len(players)-1):
                    if players[p] != self:
                        players[p].message += str("In " + room.name + " at " + time + ", " + self.name + " tricked The Enemy in a game of wits involving " + self.currentWeapon.name + ", killing them once and for all. All living players win the game, and " + self.name + " wins TRUE VICTORY for having brought it about. Congrats! ")
                print("\n")
                for p in range(len(players)):
                    print(players[p].name + "\n")
                    print(players[p].message + "\n")
                    players[p].message = ""
                    print(players[p].endMessage + "\n \n")
                    players[p].endMessage = ""
                print(report)
                report = ""
                sys.exit()
            else:
                self.message += str("However, they are more clever than you, and manage to prevent you from dealing any fatal damage. ")
                youFailed = True
                whoHere(self, players[-1], str(self.name + " attempts to outsmart " + players[-1].name + " in a game of wits, but they're smart enough to win and make it out alive. "), str(self.trueName + " attempts to outsmart " + players[-1].trueName + " in a game of wits, but they're smart enough to win and make it out alive. "), False, locations, players, weapons)

        #Has sharp weapon
        if self.currentWeapon.type == "sharp" and youFailed == False:
            self.message += str("You charge them with " + self.currentWeapon.name + ". ")
            self.marks.append("cuts")
            players[-1].marks.append("cuts")
            if self.nerves > players[-1].nerves:
                self.message += str("Having better nerves than them, you slice them apart and they slump over dead. The game is over and the soldiers win. As the hero who killed The Enemy, you win TRUE VICTORY. Congratulations!")
                for p in range(len(players)-1):
                    if players[p] != self:
                        players[p].message += str("In " + room.name + " at " + time + ", " + self.name + " sliced The Enemy apart with " + self.currentWeapon.name + ", killing them once and for all. All living players win the game, and " + self.name + " wins TRUE VICTORY for having brought it about. Congrats! ")
                print("\n")
                for p in range(len(players)):
                    print(players[p].name + "\n")
                    print(players[p].message + "\n")
                    players[p].message = ""
                    print(players[p].endMessage + "\n \n")
                    players[p].endMessage = ""
                print(report)
                report = ""
                sys.exit()
            else:
                self.message += str("However, they have better nerves than you, and manage to prevent you from dealing any fatal damage. ")
                youFailed = True
                whoHere(self, players[-1], str(self.name + " attempts to slice " + players[-1].name + " open, but their nerves are better and they manage to survive the ordeal with only some cuts."), str(self.trueName + " attempts to slice " + players[-1].trueName + " open, but their nerves are better and they manage to survive the ordeal with only some cuts."), False, locations, players, weapons)

        #The Enemy's Turn
        if youFailed == True:
            if players[-1].currentWeapon.type == "blunt":
                self.message += str("In response, The Enemy charges you with something blunt. ")
                self.marks.append("bruises")
                players[-1].marks.append("bruises")
                if players[-1].strength > self.strength:
                    self.message += str("They are stronger than you, and succeed at bashing your head in. Unless contradicted by future information, you are dead. You may no longer discuss the game with other players or communicate any game relevant details. ")
                    whoHere(players[-1], self, str(players[-1].name + " bashes " + self.name + "'s head in, killing them. "), str(players[-1].trueName + " bashes " + self.trueName + "'s head in, killing them. "), False, locations, players, weapons)
                else:
                    self.message += str("However, you are stronger than them, and fend them off with only a few bruises. ")
                    whoHere(players[-1], self, str(players[-1].name + " attempts to bash " + self.name + "'s head in, but they're strong enough to resist and make it out with only a few bruises. "), str(players[-1].trueName + " attempts to bash " + self.trueName + "'s head in, but they're strong enough to resist and make it out with only a few bruises. "), False, locations, players, weapons)
            if players[-1].currentWeapon.type == "medical":
                self.message += str("In response, The Enemy attempts to fool you with a game of wits. ")
                self.marks.append("tired")
                players[-1].marks.append("tired")
                if players[-1].intellect > self.intellect:
                    self.message += str("They are smarter than you, and fool you successfully to death. Unless contradicted by future information, you are dead. You may no longer discuss the game with other players or communicate any game relevant details. ")
                    whoHere(players[-1], self, str(players[-1].name + " outsmarts " + self.name + " in a game of wits, killing them. "), str(players[-1].trueName + " outsmarts " + self.trueName + " in a game of wits, killing them. "), False, locations, players, weapons)
                else:
                    self.message += str("However, you are stronger than them, and fend them off with only a few bruises. ")
                    whoHere(players[-1], self, str(players[-1].name + " attempts to outsmart " + self.name + " in a game of wits, but they're smart enough to win and make it out alive. "), str(players[-1].trueName + " attempts to outsmart " + self.trueName + " in a game of wits, but they're smart enough to win and make it out alive. "), False, locations, players, weapons)
            if players[-1].currentWeapon.type == "sharp":
                self.message += str("In response, The Enemy charges you with something sharp. ")
                self.marks.append("cuts")
                players[-1].marks.append("cuts")
                if players[-1].nerves > self.nerves:
                    self.message += str("They have better nerves than you, and slice you apart. Unless contradicted by future information, you are dead. You may no longer discuss the game with other players or communicate any game relevant details. ")
                    whoHere(players[-1], self, str(players[-1].name + " slices " + self.name + " open, and they bleed to death. "), str(players[-1].trueName + " slices " + self.trueName + " open, and they bleed to death. "), False, locations, players, weapons)
                else:
                    self.message += str("However, you are stronger than them, and fend them off with only a few bruises. ")
                    whoHere(players[-1], self, str(players[-1].name + " attempts to slice " + self.name + " open, but their nerves are better and they manage to survive the ordeal with only some cuts."), str(players[-1].trueName + " attempts to slice " + self.trueName + " open, but their nerves are better and they manage to survive the ordeal with only some cuts."), False, locations, players, weapons)
                

    def WATCH(self, locations, players, weapons):
        if self.alive == False:
            self.DEAD(locations, players, weapons)
            return
        self.LOITER(self.location, locations, players, weapons)
        
    def STEAL(self, target, locations, players, weapons):
        if self.alive == False:
            self.DEAD(locations, players, weapons)
            return
        if self.location != target.location:
            self.message += str("Instead of stealing from " + target.name + ", ")
            self.LOITER(self.location, locations, players, weapons)
            return
        if target.alive == False and target.currentWeapon != "none":
            self.message += str("You find " + target.name + " dead, and slip " + target.currentWeapon.name + " off of them. They won't be needing it now. ")
            self.LOITER(self.location, locations, players, weapons)
            return
        if target.alive == False:
            self.message += str("You find " + target.name + " dead, which makes the job of stealing from them easier--except when you search them for a weapon you find none. Someone must have beat you to it. ")
            self.LOITER(self.location, locations, players, weapons)
            return
        if target.currentWeapon == "none":
            self.message += str("You approach " + target.name + "carefully, hoping to slip away with their weapon when their not looking. Unfortunatly, you find nothing on them and slip away just in time not to be caught in the attempt. ")
            self.LOITER(self.location, locations, players, weapons)
            return
        if players[0].debug == True:
            print(self.trueName + " has attempted to steal from " + target.trueName + " in " + self.location.name + ". ")

        if self.nerves > target.nerves:
            self.message += str("Due to your greater finess, you manage to slip " + target.currentWeapon.name + " away from " + target.name + " You'll have to return it by morning to avoid trouble, but its yours in the meantime. ")
            self.currentWeapon = target.currentWeapon
            target.currentWeapon = "none"
            self.LOITER(self.location, locations, players, weapons)
        else:
            self.message += str("Unfortunatly, " + target.name + " has greater finess than you and catches you in the act of trying to slip a potencial weapon away from them. They make a scene, hoping someone will take notice, and you shuffle away embarrased. ")
            target.message += str("At some point, you catch " + self.name + " trying to steal your weapon, as your nerves are better than theres. You scold them loudly, hoping someone will take notice of their betrayal. ")
            whoHere(self, target, str("At some point there's a loud altercation. Apparently, " + self.name + " tried to steal something from " + target.name + " but was caught in the act. "), str("At some point there's a loud altercation. Apparently, " + self.trueName + " tried to steal something from " + target.trueName + " but was caught in the act. "), False, locations, players, weapons)

    def KILL(self, target, report, time, locations, players, weapons):
        if self.location != target.location:    #In the right place?
            self.LOITER(self.location, locations, players, weapons)
            return
        if target.alive == False:                   #Target alive?
            self.message += str("While looking to kill them, you find " + target.name + "'s body on the floor. ")
            self.LOITER(self.location, locations, players, weapons)
            return
        defend = doTheyDefend(self, target)         #Target defends?
        if defend == "pass":
            if target.weapon != weapons[17]:
                self.message += str("You approach " + target.name + " carefully with intent to kill, but suddenly notice how strong they are. Intimidated, you back off and decide to wait for a better moment. ")
                self.LOITER(self.location, locations, players, weapons)
                return
            else:
                self.message += str(target.name + " was prepared for your attack. They catch you off guard and cut you with their shiv. Cut up, you escape. ")
                target.message += str(self.name + " tries to attack you, but you're prepared and cut them with your shiv. They escape, wounded. ")
                whoHere(self, target, str(self.name + " tries to attack " + target.name + ", but they're prepared and cut them with a shiv. They escape, but wounded. "), str(self.trueName + " tries to attack " + target.trueName + ", but they're prepared and cut them with a shiv. They escape, but wounded. "), False, locations, players, weapons)
                self.marks.append("cuts")
                return
        if players[0].debug == True:
                print(self.trueName + " tries to kill " + target.trueName + " in " + self.location.name + ". ")

        if self.weapon == weapons[0]:               #LIFTING WEIGHT
            attributes = [self.strength, self.intellect, self.nerves]
            chosenAttribute = random.choice(attributes)
            chosenAttribute = chosenAttribute + 1
            self.message += str("Your " + str(chosenAttribute) + " is made more effective by 1 on account of your weapon bonus. ")

        if self.currentWeapon == "none":                #No weapon lmao
            self.message += str("Just as you're approaching " + target.name + " to attack them, you reach into your pocket and realize you have no weapon! ")
            self.LOITER(self.location, locations, players, weapons)

        elif self.currentWeapon.type == "blunt":      #Blunt weapon fight
            if self.weapon != weapons[9]:
                self.marks.append("bruises")
            if target.weapon != weapons[9]:
                target.marks.append("bruises")
            if self.strength > target.strength:
                target.alive = False
                report += str(target.name + " has been killed by " + self.name + " in " + target.location.name + " at " + time + " with " + self.currentWeapon.name + ". Their rank was " + str(target.rank) + ", their strength was " + str(target.strength) + ", their intellect was " + str(target.intellect) + ", their nerves was " + str(target.nerves) + ", their weapon was " + target.weapon.name + ", and their shift was " + str(target.shift) + ". ")
                self.honor = self.honor - target.honor
                if self.honor == 0 and target.honor < 0:
                    self.honor = 1
                if self.honor == 0 and target.honor > 0:
                    self.honor = -1
                self.message += str("You catch " + target.name + " off guard and bash their head in with " + self.currentWeapon.name + ". ")
                target.message += str(self.name + " catches you off guard and bashes your head in with " + self.currentWeapon.name + ". Unless contradicted by future information, you are dead. You may no longer discuss the game with other players or communicate any game relevant details. ")
                there = []
                there = whoHere(self, target, str(self.name + " bashes " + target.name + "'s head in, killing them. "), str(self.trueName + " bashes " + target.trueName + "'s head in, killing them. "), False, locations, players, weapons)
                bloodFeud(self, target, there, players, weapons, report, time, locations)
                return
            else:
                if target.weapon == weapons[13] and self != players[-1]:
                    self.alive = False
                    report += str(self.name + " has been killed by " + target.name + " in " + self.location.name + " at " + time + " by the antique sword bonus. Their rank was " + str(self.rank) + ", their strength was " + str(self.strength) + ", their intellect was " + str(self.intellect) + ", their nerves was " + str(self.nerves) + ", their weapon was " + self.weapon.name + ", and their shift was " + self.shift.name + ". ")
                    self.honor = self.honor - target.honor
                    if self.honor == 0 and target.honor < 0:
                        self.honor = 1
                    if self.honor == 0 and target.honor > 0:
                        self.honor = -1
                    target.honor = target.honor - self.honor
                    if target.honor == 0 and self.honor < 0:
                        target.honor = 1
                    if target.honor == 0 and self.honor > 0:
                        target.honor = -1
                    self.message += str("You attempt to bash " + target.name + "'s head in with your " + self.currentWeapon.name + ", but they're too strong and instead manage to slice you apart with their antique sword, killing you. You may no longer discuss the game with other players or communicate any game relevant details. ")
                    target.message += str(self.name + " comes at you in an attempt to bash your head in. Stronger than them, you instead manage to slice them apart with your antique sword, killing them. ")
                    whoHere(self, target, str(self.name + " attempts to bash " + target.name + "'s head in, but they're strong enough to resist and slice " + self.name + " apart with a sword, killing them. "), str(self.trueName + " attempts to bash " + target.trueName + "'s head in, but they're strong enough to resist and slice " + self.trueName + " apart with a sword, killing them. "), False, locations, players, weapons)
                    return
                else:
                    target.message += str(self.name + " comes at you in an attempt to bash your head in. Stronger than them, you survive the scuffle that follows, albeit with a few bruises.")
                    self.message += str("You attempt to bash " + target.name + "'s head in, but they're too strong and survive the scuffle that follows with only a few bruises.")
                    whoHere(self, target, str(self.name + " attempts to bash " + target.name + "'s head in, but they're strong enough to resist and make it out with only a few bruises. "), str(self.trueName + " attempts to bash " + target.trueName + "'s head in, but they're strong enough to resist and make it out with only a few bruises. "), False, locations, players, weapons)
                    return

        elif self.currentWeapon.type == "medical":  #Medical weapon fight
            if self.weapon != weapons[9]:
                self.marks.append("tired")
            if target.weapon != weapons[9]:
                target.marks.append("tired")
            if self.intellect > target.intellect:
                target.alive = False
                report += str(target.name + " has been killed by " + self.name + " in " + target.location.name + " at " + time + " with " + self.currentWeapon.name + ". Their rank was " + str(target.rank) + ", their strength was " + str(target.strength) + ", their intellect was " + str(target.intellect) + ", their nerves was " + str(target.nerves) + ", their weapon was " + target.weapon.name + ", and their shift was " + target.shift.name + ". ")
                self.honor = self.honor - target.honor
                if self.honor == 0 and target.honor < 0:
                    self.honor = 1
                if self.honor == 0 and target.honor > 0:
                    self.honor = -1
                self.message += str("You outsmart " + target.name + " in a game of wits involving " + self.currentWeapon.name + ", ending in their death. ")
                target.message += str(self.name + " outsmarts you in a game of wits involving " + self.currentWeapon.name + ". Unless contradicted by future information, you are dead. You may no longer discuss the game with other players or communicate any game relevant details.")
                there = []
                there = whoHere(self, target, str(self.name + " outsmarts " + target.name + " in a game of wits, killing them. "), str(self.trueName + " outsmarts " + target.trueName + " in a game of wits, killing them. "), False, locations, players, weapons)
                bloodFeud(self, target, there, players, weapons, report, time, locations)
                return
            else:
                if target.weapon == weapons[13] and self != players[-1]:
                    self.alive = False
                    report += str(self.name + " has been killed by " + target.name + " in " + self.location.name + " at " + time + " by the antique sword bonus. Their rank was " + str(self.rank) + ", their strength was " + str(self.strength) + ", their intellect was " + str(self.intellect) + ", their nerves was " + str(self.nerves) + ", their weapon was " + self.weapon.name + ", and their shift was " + self.shift.name + ". ")
                    self.honor = self.honor - target.honor
                    if self.honor == 0 and target.honor < 0:
                        self.honor = 1
                    if self.honor == 0 and target.honor > 0:
                        self.honor = -1
                    target.honor = target.honor - self.honor
                    if target.honor == 0 and self.honor < 0:
                        target.honor = 1
                    if target.honor == 0 and self.honor > 0:
                        target.honor = -1
                    self.message += str("You attempt outsmart " + target.name + " in a game of wits involving " + self.currentWeapon.name + ", but they're too smart and instead manage to slice you apart with their antique sword, killing you. You may no longer discuss the game with other players or communicate any game relevant details. ")
                    target.message += str(self.name + " attempts to outsmart you in a game of wits, but you're smarter than them and instead manage to slice them apart with your antique sword, killing them. ")
                    whoHere(self, target, str(self.name + " attempts to outsmart " + target.name + " in a game of wits, but they're smart enough to win and slice " + self.name + " apart with a sword, killing them. "), str(self.trueName + " attempts to outsmart " + target.trueName + " in a game of wits, but they're smart enough to win and slice " + self.trueName + " apart with a sword, killing them. "), False, locations, players, weapons)
                    return
                else:
                    target.message += str(self.name + " attempts to outsmart you in a game of wits, but you're smarter than them and manage to survive the challenge, though visibly exhausted.")
                    self.message += str("You attempt outsmart " + target.name + " in a game of wits involving " + self.currentWeapon.name + ", but they're too smart and survive the challenge, though visibly exhausted.")
                    whoHere(self, target, str(self.name + " attempts to outsmart " + target.name + " in a game of wits, but they're smart enough to win and make it out alive. "), str(self.trueName + " attempts to outsmart " + target.trueName + " in a game of wits, but they're smart enough to win and make it out alive. "), False, locations, players, weapons)
                    return

        elif self.currentWeapon.type == "sharp":    #Sharp weapon fight
            if self.weapon != weapons[9]:
                self.marks.append("cuts")
            if target.weapon != weapons[9]:
                target.marks.append("cuts")
            if self.nerves > target.nerves:
                target.alive = False
                report += str(target.name + " has been killed by " + self.name + " in " + target.location.name + " at " + time + " with " + self.currentWeapon.name + ". Their rank was " + str(target.rank) + ", their strength was " + str(target.strength) + ", their intellect was " + str(target.intellect) + ", their nerves was " + str(target.nerves) + ", their weapon was " + target.weapon.name + ", and their shift was " + str(target.shift) + ". ")
                self.honor = self.honor - target.honor
                if self.honor == 0 and target.honor < 0:
                    self.honor = 1
                if self.honor == 0 and target.honor > 0:
                    self.honor = -1
                self.message += str("You slice " + target.name + " open with " + self.currentWeapon.name + ", and they bleed to death. ")
                target.message += str(self.name + " slices you open with " + self.currentWeapon.name + ", and you bleed to death. Unless contradicted by future information, you are dead. You may no longer discuss the game with other players or communicate any game relevant details.")
                there = []
                there = whoHere(self, target, str(self.name + " slices " + target.name + " open, and they bleed to death. "), str(self.trueName + " slices " + target.trueName + " open, and they bleed to death. "), False, locations, players, weapons)
                bloodFeud(self, target, there, players, weapons, report, time, locations)
                return
            else:
                if target.weapon == weapons[13] and self != players[-1]:
                    self.alive = False
                    report += str(self.name + " has been killed by " + target.name + " in " + self.location.name + " at " + time + " by the antique sword bonus. Their rank was " + str(self.rank) + ", their strength was " + str(self.strength) + ", their intellect was " + str(self.intellect) + ", their nerves was " + str(self.nerves) + ", their weapon was " + self.weapon.name + ", and their shift was " + self.shift.name + ". ")
                    self.honor = self.honor - target.honor
                    if self.honor == 0 and target.honor < 0:
                        self.honor = 1
                    if self.honor == 0 and target.honor > 0:
                        self.honor = -1
                    target.honor = target.honor - self.honor
                    if target.honor == 0 and self.honor < 0:
                        target.honor = 1
                    if target.honor == 0 and self.honor > 0:
                        target.honor = -1
                    self.message += str("You attempt to slice " + target.name + " open with " + self.currentWeapon.name + ", but their nerves are better and instead they manage to slice you apart with their antique sword, killing you. You may no longer discuss the game with other players or communicate any game relevant details. ")
                    target.message += str(self.name + " attempts to slice you open, but your nerves are better than theirs and instead manage to slice them apart with your antique sword, killing them. ")
                    whoHere(self, target, str(self.name + " attempts to slice " + target.name + " open, but they're nerves are better and they slice " + self.name + " apart with a sword, killing them. "), str(self.trueName + " attempts to slice " + target.trueName + " open, but they're nerves are better and they slice " + self.trueName + " apart with a sword, killing them. "), False, locations, players, weapons)
                    return
                else:
                    target.message += str(self.name + " attempts to slice you open, but your nerves are better and you manage to survive the ordeal with only some cuts.")
                    self.message += str("You attempt to slice " + target.name + " open with " + self.currentWeapon.name + ", but their nerves are better and they manage to survive the ordeal with only some cuts.")
                    whoHere(self, target, str(self.name + " attempts to slice " + target.name + " open, but their nerves are better and they manage to survive the ordeal with only some cuts."), str(self.trueName + " attempts to slice " + target.trueName + " open, but their nerves are better and they manage to survive the ordeal with only some cuts."), False, locations, players, weapons)
                    return

#Is called to insert players into the game by reading their data of of playerData.txt
def readPlayerData(players, amount, startingLocation):
    print("\n")
    contents = open('playerData.txt').readlines()
    for p in range(amount):
        players.append(
            Player(
                contents[p * 8].strip(),
                int(contents[(p * 8) + 1]),
                int(contents[(p * 8) + 2]),
                int(contents[(p * 8) + 3]),
                int(contents[(p * 8) + 4]),
                contents[(p * 8) + 5].strip(),
                contents[(p * 8) + 6].strip(),
                startingLocation
        ))
        print(players[p].name + " logged! ")

#This is for generating a player set with random stats for testing
def randomPlayers(players, amount, locations, weapons, startingLocation):
    namesToChoose = [
        "Scott",
        "Jack",
        "Ryan",
        "Sebby",
        "Paul",
        "Nathan",
        "Nate",
        "Ed",
        "Lisa",
        "Eddie",
        "Kevin",
        "Ish",
        "Skylar",
        "Christian",
        "Morgan",
        "Susu",
        "Jun"
    ]
    stats = ["rank", "strength", "intellect", "nerves"]
    weaponsToChoose = weapons.copy()

    for p in range(amount):
        roll = random.randint(0,len(namesToChoose) - 1)
        playerName = namesToChoose[roll]
        namesToChoose.pop(roll)
        playerRank = 1
        playerStrength = 1
        playerIntellect = 1
        playerNerves = 1
        for s in range(6):
            stat = random.choice(stats)
            if stat == "rank":
                playerRank = playerRank + 1
            elif stat == "strength":
                playerStrength = playerStrength + 1
            elif stat == "intellect":
                playerIntellect = playerIntellect + 1
            elif stat == "nerves":
                playerNerves = playerNerves + 1
        roll = random.randint(0,len(weaponsToChoose) - 1)
        playerWeapon = weaponsToChoose[roll]
        weaponsToChoose.pop(roll)
        playerShift = random.choice(locations)

        players.append(
            Player(
                playerName,
                playerRank,
                playerStrength,
                playerIntellect,
                playerNerves,
                playerWeapon,
                playerShift,
                startingLocation
        ))
        print(" ")
        print("NAME: " + players[p].name)
        print("rank: " + str(players[p].rank))
        print("str: " + str(players[p].strength))
        print("int: " + str(players[p].intellect))
        print("ner: " + str(players[p].nerves))
        print("WEAPON: " + players[p].weapon.name)
        print("SHIFT: " + players[p].shift.name)

#Creates the enemy
def spawnEnemy(players, weapons, startingLocation):
    enemyRanks = [1, 2, 3, 4, 5, 6]
    enemyStats = [1, 2, 3, 4, 5, 6, 7, 8]
    enemyWeapons = []
    for w in range(len(weapons)):
        x = 0
        for p in range(len(players)):
            if players[p].weapon == weapons[w]:
                x = x + 1
        if x == 0:
            enemyWeapons.append(weapons[w])

    players.append(
        Player(
            "enemy",
            random.choice(enemyRanks),
            random.choice(enemyStats),
            random.choice(enemyStats),
            random.choice(enemyStats),
            random.choice(enemyWeapons),
            "none",
            startingLocation
        ))

    print(players[-1].weapon.name + " has been successfully assignged too The Enemy! ")


