from Players import addPlayers, askCommands, howMany
from Weapons import findWeapons, liquorHandle, combatAward, encryptedLaptop, heavyBriefcase, thePrince, alarmClock, exoticPoison, aggressiveStimulants, petSnake, firstAid, sleepingPills, neurotoxicGas, kitchenKnife, decorativeSword, forgedKeycard, sacredDagger, throwingShurikens, improvisedShiv
from Locations import Barraks, Sanitation, Gymnasium, Medical, Library, Information, Bathhouse, Communications, Power, Armaments, Security, Command, findShifts

weapons = []
weapons.append(liquorHandle)
weapons.append(combatAward)
weapons.append(encryptedLaptop)
weapons.append(heavyBriefcase)
weapons.append(thePrince)
weapons.append(alarmClock)
weapons.append(exoticPoison)
weapons.append(aggressiveStimulants)
weapons.append(petSnake)
weapons.append(firstAid)
weapons.append(sleepingPills)
weapons.append(neurotoxicGas)
weapons.append(kitchenKnife)
weapons.append(decorativeSword)
weapons.append(forgedKeycard)
weapons.append(sacredDagger)
weapons.append(throwingShurikens)
weapons.append(improvisedShiv)

locations = []
locations.append(Barraks)
locations.append(Sanitation)
locations.append(Gymnasium)
locations.append(Medical)
locations.append(Library)
locations.append(Information)
locations.append(Bathhouse)
locations.append(Communications)
locations.append(Power)
locations.append(Armaments)
locations.append(Security)
locations.append(Command)

players = []
amount = howMany()
addPlayers(players, amount, Barraks)
findShifts(players, locations)
findWeapons(players, weapons)

#################################################################### Day-Night Loop ####################################################################

days = int(amount/2+1)
for nights in range(days):

    numberWords = ["First", "Second", "Third", "Fourth", "Fifth", "Sixth", 'Seventh', "Eighth", "Ninth", "Tenth", "Eleventh", "Twelfth"]
    dayNumberWord = numberWords[nights]
    input("Press ENTER to begin the " + dayNumberWord + "night.")

    moderatorMessage = ""
    time = ["11 PM", "12 AM", "1 AM", "2 AM", "3 AM", "4 AM", "5 AM", "6 AM"]

    askCommands(players)

    #Hour Cycle
    for h in range(0, 7):
        hour = time[h]

        


'''
THINGS TO UPDATE EVERY NIGHT
    moderatorMessage
    shifts
    
'''