from Functions import whoHere
import random

class Barraks:
    def __init__(self):
        self.name = "the barraks"
        self.rank = 1
        self.sabotages = 0
        self.workload = 0
        self.functionality = True
        self.input = "BARRAKS"
        self.blips = 0

    def visit(self, player, locations, players):
        if player.alive is False:
            player.DEAD(locations, players)
            return
        if player.location is not self:
            player.LOITER(player.location, locations, players)
            return
        if self.functionality is False:
            player.message += str("Unfortunatly, " + player.location.name + " is not currently functional, so instead, ")
            player.LOITER(player.location, locations, players)
            return

        player.sleep = player.sleep + 1
        player.message += str("You manage to get a good hour of geniune sleep in. You will be able to stave off rest more effectively tomorrow, should the need arise. ")
        whoHere(player, "none", str(player.name + " is sleeping soundly in his bed. "), False, locations, players)

class Sanitation:
    def __init__(self):
        self.name = "sanitation"
        self.rank = 1
        self.sabotages = 0
        self.workload = 0
        self.functionality = True
        self.input = "SANITATION"
        self.blips = 0
        
    def visit(self, player, locations, players):
        if player.alive is False:
            player.DEAD(locations, players)
            return
        if player.location is not self:
            player.LOITER(player.location, locations, players)
            return
        if self.functionality is False:
            player.message += str("Unfortunatly, " + player.location.name + " is not currently functional, so instead, ")
            player.LOITER(player.location, locations, players)
            return
        if player.currentWeapon is "none":
            player.LOITER(player.location, locations, players)
            return
        
        if player.weapon is player.currentweapon:
            player.message += str("You sneak into sanitation and slip " + player.weapon.name + " into the trash. It will never be used again. ")
            player.weapon.owner = "no one"
            player.weapon.present = False
            player.weapon = "none"
            player.currentWeapon = "none"
            whoHere(player, "none", str(player.name + " throws something into the trash. "), False, locations, players)
        else:
            player.message += str("You sneak into sanitation and slip " + player.owner.name + "'s " + player.currentWeapon.name + " into the trash. It will never be used again. ")
            player.currentWeapon.owner.weaponDestroyed = True
            player.currentWeapon.owner = "no one"
            player.currentWeapon.present = False
            player.owner.weapon = "none"
            player.currentWeapon = "none"
            whoHere(player, "none", str(player.name + " throws something into the trash. "), False, locations, players)

class Gymnasium:
    def __init__(self):
        self.name = "the gymnasium"
        self.rank = 2
        self.sabotages = 0
        self.workload = 0
        self.functionality = True
        self.input = "GYMNASIUM"
        self.blips = 0
        
    def use(self, player, locations, players):
        if player.alive is False:
            player.DEAD(locations, players)
            return
        if player.location is not self:
            player.LOITER(player.location, locations, players)
            return
        if self.functionality is False:
            player.message += str("Unfortunatly, " + player.location.name + " is not currently functional, so instead, ")
            player.LOITER(player.location, locations, players)
            return

        player.gymnasiumVisits = player.gymnasiumVisits + 1
        player.message += str("You workout for a good hour in the gym. You feel stronger than ever. ")
        whoHere(player, "none", str(player.name + " is lifting weights. "), False, locations, players)

    def learn(self, player, locations, players):
        if player.alive is False:
            player.DEAD(locations, players)
            return
        if player.location is not self:
            player.LOITER(player.location, locations, players)
            return
        if self.functionality is False:
            player.message += str("Unfortunatly, " + player.location.name + " is not currently functional, so instead, ")
            player.LOITER(player.location, locations, players)
            return

        strengths = ""
        for p in range(len(players) - 1):
            strengths += str(players[p].strength + ", ")
        strengths += str("and " + players[len(players)-1].strength)
        player.message += str("You look through the gym's profile logs and find that the strengths of the base's soldiers are: " + strengths + ". ")
        whoHere(player, "none", str(player.name + " is looking through the gym's profile logs. "), False, locations, players)

class Medical:
    def __init__(self):
        self.name = "medical"
        self.rank = 2
        self.sabotages = 0
        self.workload = 0
        self.functionality = True
        self.input = "MEDICAL"
        self.blips = 0
        
    def visit(self, player, locations, players):
        if player.alive is False:
            player.DEAD(locations, players)
            return
        if player.location is not self:
            player.LOITER(player.location, locations, players)
            return
        if self.functionality is False:
            player.message += str("Unfortunatly, " + player.location.name + " is not currently functional, so instead, ")
            player.LOITER(player.location, locations, players)
            return
            
        if "cuts" in player.marks and "bruises" not in player.marks and "tired" not in player.marks:
            player.marks.clear()
            player.message += str("You use the advanced systems to seal up most of your cuts from the earlier fight. Tomorrow morning, no one will be the wiser. ")
            whoHere(player, "none", str(player.name + " used the advanced medical systems. "), False, locations, players)
        elif "cuts" not in player.marks and "bruises" in player.marks and "tired" not in player.marks:
            player.marks.clear()
            player.message += str("You use the advanced systems to rapidly heal most of your bruises from the earlier fight. Tomorrow morning, no one will be the wiser. ")
            whoHere(player, "none", str(player.name + " used the advanced medical systems. "), False, locations, players)
        elif "cuts" not in player.marks and "bruises" not in player.marks and "tired" in player.marks:
            player.marks.clear()
            player.message += str("You use the coffee machine to ensure that your exhaustion from that early ordeal doesn't show. Tomorrow morning, no one will be the wiser. ")
            whoHere(player, "none", str(player.name + " used the advanced medical systems. "), False, locations, players)
        elif "cuts" in player.marks and "bruises" in player.marks and "tired" not in player.marks:
            player.marks.clear()
            player.message += str("You use the advanced systems to rapidly heal all of your cuts and bruises from those earlier fights. Tomorrow morning, no one will be the wiser. ")
            whoHere(player, "none", str(player.name + " used the advanced medical systems. "), False, locations, players)
        elif "cuts" in player.marks and "bruises" not in player.marks and "tired" in player.marks:
            player.marks.clear()
            player.message += str("You use the coffee machine and advanced systems to ensure that your exhaustion and cuts from those early ordeals don't show. Tomorrow morning, no one will be the wiser. ")
            whoHere(player, "none", str(player.name + " used the advanced medical systems. "), False, locations, players)
        elif "cuts" not in player.marks and "bruises" in player.marks and "tired" in player.marks:
            player.marks.clear()
            player.message += str("You use the coffee machine and advanced systems to ensure that your exhaustion and bruises from those early ordeals don't show. Tomorrow morning, no one will be the wiser. ")
            whoHere(player, "none", str(player.name + " used the advanced medical systems. "), False, locations, players)
        elif "cuts" in player.marks and "bruises" in player.marks and "tired" in player.marks:
            player.marks.clear()
            player.message += str("You use the coffee machine and advanced systems to ensure that your exhaustion, bruises, and cuts from all those early ordeals don't show. Tomorrow morning, no one will be the wiser. ")
            whoHere(player, "none", str(player.name + " used the advanced medical systems. "), False, locations, players)
        else:
            player.LOITER(player.location, locations, players)

class Library:
    def __init__(self):
        self.name = "the library"
        self.rank = 3
        self.sabotages = 0
        self.workload = 0
        self.functionality = True
        self.input = "LIBRARY"
        self.blips = 0

    def use(self, player, locations, players):
        if player.alive is False:
            player.DEAD(locations, players)
            return
        if player.location is not self:
            player.LOITER(player.location, locations, players)
            return
        if self.functionality is False:
            player.message += str("Unfortunatly, " + player.location.name + " is not currently functional, so instead, ")
            player.LOITER(player.location, locations, players)
            return
        
        bookFacts = []
        bookFacts.append("Fish brought from the bottom most depths of the ocean will literally melt upon reaching the surface, physically incapable of dealing with the lower pressure.")                                   
        bookFacts.append("The distinction between straight and gay individuals was not made at all until the 19th century. Previous to this, only specific sexual acts--not people types--were considered abberations.")   
        bookFacts.append("Under the philosophy known as 'platonism', the creator of the universe is not God, but rather an evil force known as 'the Demiurge' that has trapped humanity in a false prison of matter.")      
        bookFacts.append("During the golden age of piracy, many captains were hired by governments to raid and steal from merchant ships belonging to enemy nations. These would become know as 'privateers'.")             
        bookFacts.append("The ancient greeks considered direct tax equivalent to slavery, and financed their city-states entirely on fees for public services.")                                                           
        bookFacts.append("The vast majority of gladitorial matches did not end in death for either party, and most gladiators fought professionally for many years.")                                                       
        bookFacts.append("In traditional astrology, marriage and love are represented by two different areas of one's chart, as marriage was mostly political/economic for most of human history.")                    
        bookFacts.append("Humans can guess (at above expected rates) whether another human is looking at them through a two-way mirror. The mechanism behind this is currently unknown.")                                  
        bookFacts.append("Black holes are completly invisible, and so can only be distinguished by the human eye as areas absent of matter or light.")
        bookFacts.append("Previous to Darwin's theory of evolution, an alternative theory was proposed in which physical changes over an organisms lifetime could be transmitted to their offspring.")
        bookFacts.append("LSD was invented when a researcher spilled just the right amount of the chemical he was working with on his skin and experienced a trip. If he had spilled more, he would have died.")

        player.libraryVisits = player.libraryVisits + 1
        player.message += str("You spend the hour scouring the shelves for useful information. Deep in the shelves, you find an old book that explains: '" + random.choice(bookFacts) + "' Inspiration strikes, and you suddenly get a wonderful idea of how to deal with your current predicament. ")
        whoHere(player, "none", str(player.name + " is scouring the shelves for literary materials. "), False, locations, players)

    def learn(self, player, locations, players):
        if player.alive is False:
            player.DEAD(locations, players)
            return
        if player.location is not self:
            player.LOITER(player.location, locations, players)
            return
        if self.functionality is False:
            player.message += str("Unfortunatly, " + player.location.name + " is not currently functional, so instead, ")
            player.LOITER(player.location, locations, players)
            return

        intellects = ""
        for p in range(len(players) - 1):
            intellects += str(players[p].intellect + ", ")
        intellects += str("and " + players[len(players)-1].intellect)
        player.message += str("You look through the lists of checked out books and discover that the intellects of the base's soldiers are: " + intellects + ". ")
        whoHere(player, "none", str(player.name + " is looking through the library's database for information. "), False, locations, players)

class Information:
    def __init__(self):
        self.name = "information"
        self.rank = 3
        self.sabotages = 0
        self.workload = 0
        self.functionality = True
        self.input = "INFORMATION"
        self.blips = 0
        
    def visit(self, player, locations, players):
        if player.alive is False:
            player.DEAD(locations, players)
            return
        if player.location is not self:
            player.LOITER(player.location, locations, players)
            return
        if self.functionality is False:
            player.message += str("Unfortunatly, " + player.location.name + " is not currently functional, so instead, ")
            player.LOITER(player.location, locations, players)
            return

        ranks = ""
        for p in range(len(players) - 1):
            ranks += str(players[p].rank + ", ")
        ranks += str("and " + players[len(players)-1].rank)
        player.message += str("You search through all the files you can find and discover that the ranks of the base's soldiers are: " + ranks + ". ")
        whoHere(player, "none", str(player.name + " is looking through the base's ranking files. "), False, locations, players)

class Bathhouse:
    def __init__(self):
        self.name = "the bathhouse"
        self.rank = 4
        self.sabotages = 0
        self.workload = 0
        self.functionality = True
        self.input = "BATHHOUSE"
        self.blips = 0
        
    def use(self, player, locations, players):

        player.bathhouseVisits = player.bathhouseVisits + 1
        player.message += str("You spend the hour steaming in the sauna, and come out feeling refreshed and calmer than ever.")
        whoHere(player, "none", str(player.name + " is steaming in the sauna. "), False, locations, players)

    def learn(self, player, locations, players):
        if player.alive is False:
            player.DEAD(locations, players)
            return
        if player.location is not self:
            player.LOITER(player.location, locations, players)
            return
        if self.functionality is False:
            player.message += str("Unfortunatly, " + player.location.name + " is not currently functional, so instead, ")
            player.LOITER(player.location, locations, players)
            return

        nerves = ""
        for p in range(len(players) - 1):
            nerves += str(players[p].nerves + ", ")
        nerves += str("and " + players[len(players)-1].nerves)
        player.message += str("You look through the bathhouse records and discover that the nerves of the base's soldiers are: " + nerves + ". ")
        whoHere(player, "none", str(player.name + " is looking through the bathhouse records for information on other soldier's nerves. "), False, locations, players)


class Communications:
    def __init__(self):
        self.name = "communications"
        self.rank = 4
        self.sabotages = 0
        self.workload = 0
        self.functionality = True
        self.input = "COMMUNICATIONS"
        self.blips = 0
        
    def visit(self, player, target1, target2, locations, players, report):
        
        player.message += str("You audit the comms shared between " + target1.name + " and " + target2.name + " this morning and afternoon. The computer returns that it has noted your attempt and will, if accepted, send you the result of the audit by morning. ")
        target1.endMessage += str("At some point during the night, someone audited the comms between " + target2.name + " and you from the previous day. ")
        target2.endMessage += str("At some point during the night, someone audited the comms between " + target1.name + " and you from the previous day. ")
        report += str("Audit the comms between " + target1.name + " and " + target2.name + " for " + player.name + ". ")
        whoHere(player, "none", str(player.name + " is requesting an audit of someone's communications from the previous day. "), False, locations, players)

class Power:
    def __init__(self):
        self.name = "power"
        self.rank = 5
        self.sabotages = 0
        self.workload = 0
        self.functionality = True
        self.input = "POWER"
        self.blips = 0
        
    def visit(self, player, locations, players):
        if player.alive is False:
            player.DEAD(locations, players)
            return
        if player.location is not self:
            player.LOITER(player.location, locations, players)
            return
        if self.functionality is False:
            player.message += str("Unfortunatly, " + player.location.name + " is not currently functional, so instead, ")
            player.LOITER(player.location, locations, players)
            return
        
        player.power = player.power + 1
        player.message += str("You spend the hour fueling and watching over the generator, an activiy that will excuse you of some of your responsiblities tomorrow night. ")
        whoHere(player, "none", str(player.name + " is tending to the generator to excuse themselves from future work. "), False, locations, players)

class Armaments:
    def __init__(self):
        self.name = "armaments"
        self.rank = 5
        self.sabotages = 0
        self.workload = 0
        self.functionality = True
        self.input = "ARMAMENTS"
        self.blips = 0
        
    def visit(self, player, locations, players):
        if player.alive is False:
            player.DEAD(locations, players)
            return
        if player.location is not self:
            player.LOITER(player.location, locations, players)
            return
        if self.functionality is False:
            player.message += str("Unfortunatly, " + player.location.name + " is not currently functional, so instead, ")
            player.LOITER(player.location, locations, players)
            return

        weapons = []
        for p in range(len(players)):
            if players[p].weapon is not "none":
                weapons.append(players[p].weapon)
        player.message += str("You search the combat logs and discover that " + random.choice(weapons) + " is being used as a weapon. ")
        whoHere(player, "none", str(player.name + " is looking through the base's combat logs. "), False, locations, players)

class Security:
    def __init__(self):
        self.name = "security"
        self.rank = 6
        self.sabotages = 0
        self.workload = 0
        self.functionality = True
        self.input = "SECURITY"
        self.blips = 0
        
    def visit(self, player, locations, players):
        if player.alive is False:
            player.DEAD(locations, players)
            return
        if player.location is not self:
            player.LOITER(player.location, locations, players)
            return
        if self.functionality is False:
            player.message += str("Unfortunatly, " + player.location.name + " is not currently functional, so instead, ")
            player.LOITER(player.location, locations, players)
            return
            
        for l in range(len(locations)):
            locations[l].blips = 0
        for p in range(len(players)):
            for l in range(len(locations)):
                if players[p].location is locations[l]:
                    locations[l].blips = locations[l].blips + 1
        player.message += "You check the security systems and discover that there are: "
        locationsWithBlips = []
        for l in range(len(locations)):
            if locations[l].blips > 0:
                locationsWithBlips.append(locations[l])
        for l in range(len(locationsWithBlips)-1):
            player.message += str(locationsWithBlips[l].blips + " warm bodies in " + locationsWithBlips[l].name + ", ")
        player.message += str("and " + locationsWithBlips[len(locationsWithBlips)-1].blips + " warm bodies in " + locationsWithBlips[len(locationsWithBlips)-1].name + ". ")
        whoHere(player, "none", str(player.name + " is checking the security systems to see which rooms are occupied. "), False, locations, players)

class Command:
    def __init__(self):
        self.name = "command"
        self.rank = 6
        self.sabotages = 0
        self.workload = 0
        self.functionality = True
        self.input = "COMMAND"
        self.blips = 0
        
    def visit(self, player, locations, players):
        if player.alive is False:
            player.DEAD(locations, players)
            return
        if player.location is not self:
            player.LOITER(player.location, locations, players)
            return
        if self.functionality is False:
            player.message += str("Unfortunatly, " + player.location.name + " is not currently functional, so instead, ")
            player.LOITER(player.location, locations, players)
            return

        shifts = ""
        for p in range(len(players) - 1):
            shifts += str(players[p].shift.name + ", ")
        shifts += str("and " + players[len(players)-1].shift.name)
        player.message += str("You look through command's files and discover that the shifts currently assigned are: " + shifts + ". ")
        whoHere(player, "none", str(player.name + " is looking through command's files to learn about current shifts. "), False, locations, players)