import random
from Functions import addPlayers, askCommands, checkAccess, clearLoop, findShifts, findWeapons, howMany, locate
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

days = int(amount/2+1)
for nights in range(days):

    numberWords = ["First", "Second", "Third", "Fourth", "Fifth", "Sixth", 'Seventh', "Eighth", "Ninth", "Tenth", "Eleventh", "Twelfth"]
    dayNumberWord = numberWords[nights]
    input("Press ENTER to begin the " + dayNumberWord + "night.")

    report = ""
    time = ["11 PM", "12 AM", "1 AM", "2 AM", "3 AM", "4 AM", "5 AM", "6 AM"]

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
                        locations[r].visit(actor, hour)

                if actor.commands[h][0] is "WORK":
                    for r in range(len(locations)):
                        if locations[r].input is actor.commands[h][1]:
                            actor.WORK(locations[r], locations, players)
                if actor.commands[h][0] is "SABOTAGE":
                    for r in range(len(locations)):
                        if locations[r].input is actor.commands[h][1]:
                            actor.SABOTAGE(locations[r], locations, players)
                if actor.commands[h][0] is "LOITER":
                    for r in range(len(locations)):
                        if locations[r].input is actor.commands[h][1]:
                            actor.LOITER(locations[r], locations, players)
                if actor.commands[h][0] is "AMBUSH":
                    for r in range(len(locations)):
                        if locations[r].input is actor.commands[h][1]:
                            for p in range(len(players)):
                                if players[p].name is actor.commands[h][2]:
                                    actor.AMBUSH(locations[r], players[p], locations, players, hour)
                if actor.commands[h][0] is "INFILTRATOR":
                    for r in range(len(locations)):
                        if locations[r].input is actor.commands[h][1]:
                            actor.INFILTRATOR(locations[r])

                if actor.commands[h][0] is "KILL":
                    for p in range(len(players)):
                        if players[p].name is actor.commands[h][1]:
                            actor.KILL(players[p], report, hour)
                if actor.commands[h][0] is "STEAL":
                    for p in range(len(players)):
                        if players[p].name is actor.commands[h][1]:
                            actor.STEAL(players[p], locations, players)
                if actor.commands[h][0] is "WATCH":
                    actor.WATCH(locations, players)
                


            
            
            
            
            
            
            
            
            
            
            
            #No move

                #DEFEND
                #REST
                #DEAD

            #The rooms
                #BARRAKS
                #SANITATION
                #GYMNASIUM
                #MEDICAL
                #LIBRARY
                #INFORMATION
                #BATHHOUSE
                #COMMUNICATIONS
                #POWER
                #ARMAMENTS
                #SECURITY
                #COMMAND

            #Need to find room

                #WORK
                #SABOTAGE
                #LOITER
                #AMBUSH
                #INFILTRATOR

            #The comlicated ones that require tracking

                #WATCH
                #KILL
                #STEAL