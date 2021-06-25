import sys

weapons = []

weapons.append(liquorHandle)



########################################################################## Locations ##########################################################################

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

#Setup location idenitifiers

def selfIdentify():
    eyes = []
    for i in range(len(players)):
        if players[i].location is target.location:
            eyes.append(player[i])
    for i in range(len(eyes)):
        if eyes[i] is alive and eyes[i] is not self:
            eyes[i].message += str(self.name + " is also present. ")
            self.message += str(eyes[i].name + " is also present. ")
        else if eyes[i] is not alive and is not self:
            self.message += str(eyes[i].name + "'s body is also laying on the floor. ")
    clear(eyes)
    return

def playerIdentify():
    eyes = []
    for i in range(len(players)):
        if players[i].location is player.location:
            eyes.append(player[i])
    for i in range(len(eyes)):
        if eyes[i] is alive and eyes[i] is not player:
            eyes[i].message += str(player.name + " is also present. ")
            player.message += str(eyes[i].name + " is also present. ")
        else if eyes[i] is not alive and is not player:
            player.message += str(eyes[i].name + "'s body is also laying on the floor. ")
    clear(eyes)
    return

######################################################################### Add Players #########################################################################

#Ask for player amount
playerNumber = input("Number of soldiers (2-12): \n")

#Tell 0 players to fuck off
if int(playerNumber) <= 0:                                                       
    input("You don't have a base without soldiers. Come back with some players!\n")
    sys.exit()

#Tell 1 player to fuck off
if int(playerNumber) is 1:
    input("There's already a last man, silly!")
    sys.exit()

#Create players
for i in range(0,int(playerNumber)):
    addPlayer(players)

#################################################################### Day-Night Loop ####################################################################

days = int(playerNumber/2+1)

#Day Cycle
for nights in range(0, days):

    #Readiness check
    dayNumberWord = numberWords[nights + 1]
    input("Press ENTER to begin the " + dayNumberWords + "night.")

    #Moderator's Message
    moderatorMessage = ""

    #Define Time
    time = {
        0 : "11 PM",
        1 : "12 AM"
    }

    #Hour Cylce
    for hour in range(0, 7):
        time[hour]