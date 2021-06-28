class Barraks:
    def __init__(self, rank):
        self.name = "the barraks"
        self.rank = 1
        self.sabotages = 0
        self.workload = 0
        self.functionality = True
        self.input = "BARRAKS"

    def visit(player):

        player.sleep = player.sleep + 1
        player.message += str("At " + time + ", you manage to get a good hour of geniune sleep in. You will be able to stave off rest more effectively tomorrow, should the need arise. ")

class Sanitation:
    def __init__(self, rank):
        self.name = "sanitation"
        self.rank = 1
        self.sabotages = 0
        self.workload = 0
        self.functionality = True
        self.input = "SANITATION"
        
    def visit(player):

        global moderatorMessage
        
        if player.weapon is player.currentweapon:
            player.message += str("Around " + time + ", you sneak into sanitation and slip your " + player.weapon + " into the trash. It will never be used again. ")
            player.weapon = nothing
            player.currentweapon = nothing
        else:
            player.message += str("Around " + time + ", you sneak into sanitation and slip " + player.owner.name + "'s " + player.currentweapon + " into the trash. It will never be used again. ")
            player.owner.weapon = nothing
            player.currentweapon = nothing
            moderatorMessage += str("Tell " + player.owner.name + " that someone trashed their weapon last night. ")

class Gymnasium:
    def __init__(self, rank):
        self.name = "the gymnasium"
        self.rank = 2
        self.sabotages = 0
        self.workload = 0
        self.functionality = True
        self.input = "GYMNASIUM"
        
    def visit(player):
            
        player.gymnasiumVisits = player.gymnasiumVisits + 1
        player.message += str("At " + time + ", you workout for a good hour in the gym. ")

class Medical:
    def __init__(self, rank):
        self.name = "medical"
        self.rank = 2
        self.sabotages = 0
        self.workload = 0
        self.functionality = True
        self.input = "MEDICAL"
        
    def visit(player):
            
        if "cuts" in player.marks and "bruises" not in player.marks:
            player.marks.clear()
            player.message += str("Around " + time + ", you use the advanced systems in medical to seal up most of your cuts from the earlier fight. Tomorrow morning, no one will be the wiser. ")
        elif "cuts" not in player.marks and "bruises" in player.marks:
            player.marks.clear()
            player.message += str("Around " + time + ", you use the advanced systems in medical to rapidly heal most of your bruises from the earlier fight. Tomorrow morning, no one will be the wiser. ")
        elif "cuts" in player.marks and "bruises" in player.marks:
            player.marks.clear()
            player.message += str("Around " + time + ", you use the advanced systems in medical to rapidly heal all of your cuts and bruises from those earlier fights. Tomorrow morning, no one will be the wiser. ")
        else:
            player.message += str("Around " + time + ", you visit medical. ")

class Library:
    def __init__(self, rank):
        self.name = "the library"
        self.rank = 3
        self.sabotages = 0
        self.workload = 0
        self.functionality = True
        self.input = "LIBRARY"

    def visit(player):
        
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
        player.message += str("At " + time + ", you peruse the books in the base's library for about an hour. Deep in the shelves, you find an old book that explains: '" + random.choice(bookFacts) + "' Inspiration strikes, and you suddenly get a wonderful idea of how to deal with your current predicament. ")

class Information:
    def __init__(self, rank):
        self.name = "information"
        self.rank = 3
        self.sabotages = 0
        self.workload = 0
        self.functionality = True
        self.input = "INFORMATION"
        
    def visit(player, target):

        player.message += str("Around " + time + ", you scour all the files you can find on " + target.name + " in information, and eventually discover their intellect is " + target.intellect + " and their nerves is " + target.nerves + ". ")

class Bathhouse:
    def __init__(self, rank):
        self.name = "the bathhouse"
        self.rank = 4
        self.sabotages = 0
        self.workload = 0
        self.functionality = True
        self.input = "BATHHOUSE"
        
    def visit(player):

        player.bathhouseVisits = player.bathhouseVisits + 1
        player.message += str("At " + time + ", you spend an hour plugged into simulated combat in bathhouse. Your reflexes honed, you feel more precise than ever. ")

class Communications:
    def __init__(self, rank):
        self.name = "communications"
        self.rank = 4
        self.sabotages = 0
        self.workload = 0
        self.functionality = True
        self.input = "COMMUNICATIONS"
        
    def visit(player, target1, target2):
        
        player.message += str("Around " + time + ", you visit communications to audit the comms shared between " + target1.name + " and " + target2.name + " this morning and afternoon. The computer returns that it has noted your attempt and will, if accepted, send you the result of the audit by morning. ")
        moderatorMessage += str("Send " + player.name + " any comms shared between " + target1.name + " and " + target2.name " yesterday. ")

class Power:
    def __init__(self, rank):
        self.name = "power"
        self.rank = 5
        self.sabotages = 0
        self.workload = 0
        self.functionality = True
        self.input = "POWER"
        
    def visit(player):
        
        player.power = player.power + 1
        player.message += str("At " + time + ", you spend an hour fueling and watching over the generator, an activiy that will excuse you of some of your responsiblities tomorrow night. ")

class Armaments:
    def __init__(self, rank):
        self.name = "armaments"
        self.rank = 5
        self.sabotages = 0
        self.workload = 0
        self.functionality = True
        self.input = "ARMAMENTS"
        
    def visit(player, target):
        
        player.message += str("Around " + time + ", you stop by armaments to see if you can learn anything useful about " + target.name + ". From the training logs, you discover that their strength is " + target.strength + " and that they have " + target.weapon + " (" + target.weaponType + ") on hand that that they could use to kill. ")

class Security:
    def __init__(self, rank):
        self.name = "security"
        self.rank = 6
        self.sabotages = 0
        self.workload = 0
        self.functionality = True
        self.input = "SECURITY"
        
    def visit(player, target):
            
        player.message += str("Around " + time + ", you visit security and search " + target.name + "'s name in the tracking database. On a projected map, you see a blip light up in " + target.location + ". ")

class Command:
    def __init__(self, rank):
        self.name = "command"
        self.rank = 6
        self.sabotages = 0
        self.workload = 0
        self.functionality = True
        self.input = "COMMAND"
        
    def visit(player, target):

        player.message += str("Around " + time + ", you visit command to see if the base's highest ranking records might reveal something useful about " + target.name + ". You discover that their rank is " + target.rank + " and their currently assigned to the " + shift + " shift. ")