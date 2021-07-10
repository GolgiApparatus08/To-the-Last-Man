from Players import readPlayerData
import random
import sys
from Functions import askShifts, checkAccess, chooseYourWeapon, clearLoop, findShifts, findWeapons, howMany, locate, readCommands, requiredSleep, requiredWork, roomPoints, theTribunal, weSeeDeadPeople
from Weapons import liftingWeight, encryptedLaptop, heavyBriefcase, majorAward, strongBourbon, thePrince, alarmClock, aggressiveStimulants, petSnake, firstAid, sleepingPills, neurotoxicGas, kitchenKnife, decorativeSword, forgedKeycard, sacredDagger, throwingShurikens, improvisedShiv
from Locations import Barraks, Sanitation, Gymnasium, Medical, Library, Information, Bathhouse, Communications, Power, Armaments, Security, Command

weapons = []
weapons.append(liftingWeight())
weapons.append(majorAward())
weapons.append(encryptedLaptop())
weapons.append(heavyBriefcase())
weapons.append(thePrince())
weapons.append(alarmClock())
weapons.append(strongBourbon())
weapons.append(aggressiveStimulants())
weapons.append(petSnake())
weapons.append(firstAid())
weapons.append(sleepingPills())
weapons.append(neurotoxicGas())
weapons.append(kitchenKnife())
weapons.append(decorativeSword())
weapons.append(forgedKeycard())
weapons.append(sacredDagger())
weapons.append(throwingShurikens())
weapons.append(improvisedShiv())

locations = []
locations.append(Barraks())
locations.append(Sanitation())
locations.append(Gymnasium())
locations.append(Medical())
locations.append(Library())
locations.append(Information())
locations.append(Bathhouse())
locations.append(Communications())
locations.append(Power())
locations.append(Armaments())
locations.append(Security())
locations.append(Command())

players = []
amount = howMany()
readPlayerData(players, amount, locations[0])
findShifts(players, locations)
findWeapons(players, weapons)

#################################################################### Day-Night Loop ####################################################################

report = ""
time = ["11 PM", "12 AM", "1 AM", "2 AM", "3 AM", "4 AM", "5 AM", "6 AM"]
numberWords = ["First", "Second", "Third", "Fourth", "Fifth", "Sixth", 'Seventh', "Eighth", "Ninth", "Tenth", "Eleventh", "Twelfth"]
days = int(amount/2+1)

for nights in range(days):
    dayNumberWord = numberWords[nights]
    input("Press ENTER to begin the " + dayNumberWord + " night.")

    readCommands(players)
    chooseYourWeapon(players, locations, weapons)
    
    #Hour Cycle
    for h in range(0, 7):
        hour = time[h]

        for p in range(len(players)):
            players[p].located = False

        #We go through and move people around based on their commands
        for p in range(len(players)):
            actor = players[p]
            if actor.alive == False:
                actor.located = True
            else:
                if actor.commands[h][0] is "REST":
                    actor.located = True
                    actor.message += str("At " + hour + " you stay in " + actor.location + ". ")
            
                for r in range(len(locations)):
                    if locations[r].input == actor.commands[h][0]:
                        actor.located = True
                        checkAccess(actor, locations[r], False, hour, locations)
                
                if actor.commands[h][0] == "SABOTAGE" and actor.weapon == weapons[2]:
                    actor.located = True
                    actor.message += str("At " + hour + " you stay in " + actor.location + ". ")
                elif actor.commands[h][0] == ("WORK" or "SABOTAGE"):
                    for r in range(len(locations)):
                        if locations[r].input == actor.commands[h][1]:
                            actor.located = True
                            checkAccess(actor, locations[r], True, hour, locations)
                if actor.commands[h][0] == ("LOITER" or "AMBUSH" or "INFILTRATOR"):
                    for r in range(len(locations)):
                        if locations[r].input == actor.commands[h][1]:
                            actor.located = True
                            checkAccess(actor, locations[r], False, hour, locations)

        #We go through and move around the tricky buggers that reference other players locations (KILL, WATCH, STEAL)
        for p in range(len(players)):
            for p in range(len(players)):
                players[p].visited = False
            inALoop = []
            if players[p].located == False:
                outcome = locate(players, players[p], h, inALoop, locations)
                if outcome == "loop":
                    clearLoop(players, inALoop)
                    if players[p].located == False:
                        locate(players, players[p], h, inALoop, locations)

        #Ok, now for the actions themselves
        playersRandomized = []
        while len(playersRandomized) < len(players):
            choice = random.choice(players)
            if choice not in playersRandomized:
                playersRandomized.append(choice)
        for pr in range(len(playersRandomized)):
            actor = playersRandomized[pr]
            if actor.alive == False:
                actor.DEAD(players, weapons)
            else:
                if actor.commands[h][0] == "REST":
                    actor.REST(locations, players, weapons)
            
                for r in range(len(locations)):
                    if locations[r].input == actor.commands[h][0]:
                        if locations[r] == locations[7]:
                            locations[r].visit(actor, actor.commands[h][1], actor.commands[h][2], locations, players, report, weapons)
                        if actor.commands[h][1] == "learn":
                            locations[r].learn(actor, locations, players, weapons)
                        if actor.commands[h][1] == "use":
                            locations[r].use(actor, locations, players, weapons)
                        else:
                            locations[r].visit(actor, locations, players, weapons)

                if actor.commands[h][0] == "WORK":
                    for r in range(len(locations)):
                        if locations[r].input == actor.commands[h][1]:
                            actor.WORK(locations[r], locations, players, weapons)
                if actor.commands[h][0] == "SABOTAGE":
                    for r in range(len(locations)):
                        if locations[r].input == actor.commands[h][1]:
                            actor.SABOTAGE(locations[r], locations, players, weapons)
                if actor.commands[h][0] == "LOITER":
                    for r in range(len(locations)):
                        if locations[r].input == actor.commands[h][1]:
                            actor.LOITER(locations[r], locations, players, weapons)
                if actor.commands[h][0] == "AMBUSH":
                    for r in range(len(locations)):
                        if locations[r].input == actor.commands[h][1]:
                            for p in range(len(players)):
                                if players[p].name == actor.commands[h][2]:
                                    actor.AMBUSH(locations[r], players[p], locations, players, hour, report, weapons)
                if actor.commands[h][0] == "INFILTRATOR":
                    for r in range(len(locations)):
                        if locations[r].input == actor.commands[h][1]:
                            actor.INFILTRATOR(locations[r], weapons)

                if actor.commands[h][0] == "KILL":
                    for p in range(len(players)):
                        if players[p].name == actor.commands[h][1]:
                            actor.KILL(players[p], report, hour, locations, players, weapons)
                if actor.commands[h][0] == "STEAL":
                    for p in range(len(players)):
                        if players[p].name == actor.commands[h][1]:
                            actor.STEAL(players[p], locations, players, weapons)
                if actor.commands[h][0] == "WATCH":
                    actor.WATCH(locations, players, weapons)

        if weapons[8].present == True:
            spotter = weapons[8].owner
            playersWithoutYou = players
            playersWithoutYou.pop(spotter)
            spotted = random.choice(playersWithoutYou)
            spotter.message += str("You learn through your trained pet snake that " + spotted.name + " was in " + spotted.location.name + " during this hour. ")
                
    #Now for the bits that have to happen at the end of the night
        #Stuff that happened to weapons
    for p in range(len(players)):
        if players[p].weaponDestroyed == True:
            players[p].endMessage += str("You weapon is nowhere to be found, and must have been destroyed last night. ")
            players[p].weaponDestroyed = False
        elif players[p].weapon.used == True:
            players[p].endMessage += str("Your weapon was used by someone else to attack last night. ")
            players[p].weapon.used = False

        #New attributes
    for p in range(len(players)):
        actor = players[p]
        roomPoints(actor, actor.gymnasiumVisits, "strength", actor.strength)
        roomPoints(actor, actor.libraryVisits, "intellect", actor.intellect)
        roomPoints(actor, actor.bathhouseVisits, "nerves", actor.nerves)

        #Room functionality
    for l in range(len(locations)):
        room = locations[l]
        room.functionality = True
        if room.workload > 0:
            room.functionality = False
            report += str(room.name + " is disfunctional. ")
            for p in range(len(players)):
                if players[p].shift == room and players[p].rank != 1:
                    players[p].rank = players[p].rank - 1
                    players[p].message += str("Because you failed to complete your shift, you've been demoted to rank " + str(players[p].rank) + ". ")
        else:
            for p in range(len(players)):
                if players[p].shift == room and players[p].rank != 6:
                    players[p].rank = players[p].rank + 1
                    players[p].message += str("Because you completed your shift, you've been promoted to rank " + str(players[p].rank) + ". ")
        if room.sabotages > 0:
            room.workload = room.workload + room.sabotages
            report += str(room.name + " has " + str(room.sabotages) + " sabotages. ")
            room.sabotages = 0

        #Personal rules for tomorrow night
    for p in range(len(players)):
        requiredWork(players[p])
        requiredSleep(players[p], locations)

        #DEAD PEOPLE
    if locations[10].functionality == True:
        for p in range(len(players)):
            weSeeDeadPeople(players[p], locations, report)

        #And finally, print the messages.
    print("\n")
    for p in range(len(players)):
        actor = players[p]
        print(actor.name + "\n")
        print(actor.message + "\n")
        actor.message = ""
        print(actor.endMessage + "\n \n")
        actor.endMessage = ""
    print(report)
    report = ""

        #Get people there new random shifts
    askShifts(players)
    findShifts(players, locations)

        #Do the tribunal
    theTribunal(players, locations, weapons)

        #Check for game ends
    livingPlayers = []
    for p in range(len(players[p])):    
        if players[p].alive == True:
            livingPlayers.append(players[p])
    if len(livingPlayers) == 1:     #Only one player left
        print(livingPlayers[0] + " is the last player left alive. They have won the game. ")
        sys.exit()
    if len(livingPlayers) == 0:     #No players left (can this happen?)
        print("Everyone died. Nobody wins. ")
        sys.exit()
    if nights == days - 1:          #Game time is up
        honor = False
        for l in range(len(livingPlayers)):
            if livingPlayers[l].honor > 0:
                honor = True
        if honor == False:
            print("Nobody left alive has any honor. Everyone loses. ")
            sys.exit()
        mostHonor = [livingPlayers[0]]
        for l in range(len(livingPlayers)):
            if mostHonor[0].honor < livingPlayers[l].honor:
                mostHonor = [livingPlayers[l]]
            if mostHonor[0].honor == livingPlayers[l].honor:
                mostHonor.append(livingPlayers[l])
        print("The game is over. Players that have the most honor and therefore win: \n")
        print(mostHonor)
        sys.exit()
