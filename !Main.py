import random
import sys
from Functions import addPlayers, askCommands, askShifts, checkAccess, clearLoop, findShifts, findWeapons, howMany, locate, nightRules, roomPoints, theTribunal, weSeeDeadPeople
from Weapons import liquorHandle, combatAward, encryptedLaptop, heavyBriefcase, thePrince, alarmClock, exoticPoison, aggressiveStimulants, petSnake, firstAid, sleepingPills, neurotoxicGas, kitchenKnife, decorativeSword, forgedKeycard, sacredDagger, throwingShurikens, improvisedShiv
from Locations import Barraks, Sanitation, Gymnasium, Medical, Library, Information, Bathhouse, Communications, Power, Armaments, Security, Command

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

report = ""
time = ["11 PM", "12 AM", "1 AM", "2 AM", "3 AM", "4 AM", "5 AM", "6 AM"]
numberWords = ["First", "Second", "Third", "Fourth", "Fifth", "Sixth", 'Seventh', "Eighth", "Ninth", "Tenth", "Eleventh", "Twelfth"]
days = int(amount/2+1)

for nights in range(days):
    dayNumberWord = numberWords[nights]
    input("Press ENTER to begin the " + dayNumberWord + "night.")

    askCommands(players)

    #Hour Cycle
    for h in range(0, 7):
        hour = time[h]

        for p in range(len(players)):
            players[p].located = False

        #We go through and move people around based on their commands
        for p in range(len(players)):
            actor = players[p]
            if actor.alive is False:
                actor.located = True
            else:
                if actor.commands[h][0] is "REST":
                    actor.located = True
                    actor.message += str("At " + hour + " you stay in " + actor.location + ". ")
            
                for r in range(len(locations)):
                    if locations[r].input is actor.commands[h][0]:
                        actor.located = True
                        checkAccess(actor, locations[r], False, hour)
                
                if actor.commands[h][0] is "SABOTAGE" and actor.weapon is weapons[2]:
                    actor.located = True
                    actor.message += str("At " + hour + " you stay in " + actor.location + ". ")
                if actor.commands[h][0] is ("WORK" or "SABOTAGE"):
                    for r in range(len(locations)):
                        if locations[r].input is actor.commands[h][1]:
                            actor.located = True
                            checkAccess(actor, locations[r], True, hour)
                if actor.commands[h][0] is ("LOITER" or "AMBUSH" or "INFILTRATOR"):
                    for r in range(len(locations)):
                        if locations[r].input is actor.commands[h][1]:
                            actor.located = True
                            checkAccess(actor, locations[r], False, hour)

        #We go through and move around the tricky buggers that reference other players locations (KILL, WATCH, STEAL)
        for p in range(len(players)):
            inALoop = clearLoop(players, inALoop)
            if players[p].located is False:
                outcome = locate(players, players[p], h, inALoop)
                if outcome is "loop":
                    clearLoop(players, inALoop)
                    if players[p].located is False:
                        locate(players, players[p], h, inALoop)

        #Ok, now for the actions themselves
        playersRandomized = random.shuffle(players)
        for pr in range(len(playersRandomized)):
            actor = playersRandomized[pr]
            if actor.alive is False:
                actor.DEAD(players)
            else:
                if actor.commands[h][0] is "REST":
                    actor.REST(locations, players)
            
                for r in range(len(locations)):
                    if locations[r].input is actor.commands[h][0]:
                        if locations[r] is locations[7]:
                            locations[r].visit(actor, actor.commands[h][1], actor.commands[h][2], locations, players, report)
                        if actor.commands[h][1] is "learn":
                            locations[r].learn(actor, locations, players)
                        if actor.commands[h][1] is "use":
                            locations[r].use(actor, locations, players)
                        else:
                            locations[r].visit(actor, locations, players)

                if actor.commands[h][0] is "WORK":
                    for r in range(len(locations)):
                        if locations[r].input is actor.commands[h][1]:
                            actor.WORK(locations[r], locations, players)
                if actor.commands[h][0] is "SABOTAGE":
                    for r in range(len(locations)):
                        if locations[r].input is actor.commands[h][1]:
                            actor.SABOTAGE(locations[r], locations, players, weapons)
                if actor.commands[h][0] is "LOITER":
                    for r in range(len(locations)):
                        if locations[r].input is actor.commands[h][1]:
                            actor.LOITER(locations[r], locations, players)
                if actor.commands[h][0] is "AMBUSH":
                    for r in range(len(locations)):
                        if locations[r].input is actor.commands[h][1]:
                            for p in range(len(players)):
                                if players[p].name is actor.commands[h][2]:
                                    actor.AMBUSH(locations[r], players[p], locations, players, hour, report)
                if actor.commands[h][0] is "INFILTRATOR":
                    for r in range(len(locations)):
                        if locations[r].input is actor.commands[h][1]:
                            actor.INFILTRATOR(locations[r])

                if actor.commands[h][0] is "KILL":
                    for p in range(len(players)):
                        if players[p].name is actor.commands[h][1]:
                            actor.KILL(players[p], report, hour, locations, players, weapons)
                if actor.commands[h][0] is "STEAL":
                    for p in range(len(players)):
                        if players[p].name is actor.commands[h][1]:
                            actor.STEAL(players[p], locations, players)
                if actor.commands[h][0] is "WATCH":
                    actor.WATCH(locations, players)
                
    #Now for the bits that have to happen at the end of the night
        #Stuff that happened to weapons
    for p in range(len(players)):
        if players[p].weaponDestroyed is True:
            players[p].endMessage += str("You weapon is nowhere to be found, and must have been destroyed last night. ")
            players[p].weaponDestroyed = False
        elif players[p].weapon.used is True:
            players[p].endMessage += str("Your weapon was used by someone else to attack last night. ")
            players[p].weapon.used = False

        #New attributes
    for p in range(len(players)):
        actor = players[p]
        roomPoints(actor, actor.gymnasiumVisits, "strength", actor.strength)
        roomPoints(actor, actor.libraryVisits, "intellect", actor.intellect)
        roomPoints(actor, actor.bathhouseVisits, "nerves", actor.nerves)

        #Personal rules for tomorrow night
    for p in range(len(players)):
        nightRules(players[p], "work")
        nightRules(players[p], "sleep")

        #Room functionality
    for l in range(len(locations)):
        room = locations[l]
        room.functionality = True
        if room.workload > 0:
            room.functionality = False
            report += str(room.name + " is disfunctional. ")
        if room.sabotages > 0:
            room.workload = room.workload + room.sabotages
            report += str(room.name + " has " + room.sabotages + " sabotages. ")
            room.sabotages = 0

        #DEAD PEOPLE
    if locations[10].functionality is True:
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
    theTribunal(players, weapons)

        #Check for game ends
    livingPlayers = []
    for p in range(len(players[p])):    
        if players[p].alive is True:
            livingPlayers.append(players[p])
    if len(livingPlayers) is 1:     #Only one player left
        print(livingPlayers[0] + " is the last player left alive. They have won the game. ")
        sys.exit()
    if len(livingPlayers) is 0:     #No players left (can this happen?)
        print("Everyone died. Nobody wins. ")
        sys.exit()
    if nights is days - 1:          #Game time is up
        honor = False
        for l in range(len(livingPlayers)):
            if livingPlayers[l].honor > 0:
                honor = True
        if honor is False:
            print("Nobody left alive has any honor. Everyone loses. ")
            sys.exit()
        mostHonor = [livingPlayers[0]]
        for l in range(len(livingPlayers)):
            if mostHonor[0].honor < livingPlayers[l].honor:
                mostHonor = [livingPlayers[l]]
            if mostHonor[0].honor is livingPlayers[l].honor:
                mostHonor.append(livingPlayers[l])
        print("The game is over. Players that have the most honor and therefore win: \n")
        print(mostHonor)
        sys.exit()
