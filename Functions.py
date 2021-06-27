from Players import Player
import sys
import string

numberWords = ["First", "Second", "Third", "Fourth", "Fifth", "Sixth", 'Seventh', "Eighth", "Ninth", "Tenth", "Eleventh", "Twelfth"]
lowerNumberWords = ["first", "second", "third", "fourth", "fifth", "sixth", 'seventh', "eighth", "ninth", "tenth", "eleventh", "twelfth"]

#Takes the string for "shift" input by the player and matches it with a location
def findShifts(players, locations):
    for p in range(len(players)):
        for l in range(len(locations)):
            if locations[l].name is players[p].enteredShift:
                players[p].shift = locations[l]

#Takes the string for "weapon" input by the player and matches it with a real weapon
def findWeapons(players, weapons):
    for p in range(len(players)):
        for i in range(len(weapons)):
            if weapons[i].name is players[p].weapons:
                players[p].weapons = weapons[i]

#Asks how many players there will be and returns the value as amount
def howMany():
    amount = input("Number of soldiers (2-12): \n")
    if amount <= 0:
        input("You don't have a base without soldiers. Come back with some players!\n")
        sys.exit()
    elif amount is 1:
        input("There's already a last man, silly!")
        sys.exit()
    else:
        return amount

#Uses the amount of players to ask for information about each
def addPlayers(players, amount, startingLocation):    

    for p in range(amount):
        players.append(
            Player(
                input(numberWords[p] + " soldier's name: \n"),
                input(numberWords[p] + " soldier's rank: \n"),
                input(numberWords[p] + " soldier's strength: \n"),
                input(numberWords[p] + " soldier's intellect: \n"),       
                input(numberWords[p] + " soldier's nerves: \n"),
                input(numberWords[p] + " soldier's weapon: \n"),
                input(numberWords[p] + " soldier's shift: \n"),
                startingLocation
            )
        )

        print(players[p].name + " logged! \n")

#Is called each night to ask what players will be doing for each action
def askCommands(players):
    for p in range(len(players)):
        players[p].commands.append(
            input("What is " + players[p].name + "'s first command? \n"),
            input("What is " + players[p].name + "'s second command? \n"),
            input("What is " + players[p].name + "'s third command? \n"),
            input("What is " + players[p].name + "'s fourth command? \n"),
            input("What is " + players[p].name + "'s fifth command? \n"),
            input("What is " + players[p].name + "'s sixth command? \n"),
            input("What is " + players[p].name + "'s seventh command? \n"),
            input("What is " + players[p].name + "'s eighth command? \n")
        )
        for c in range(len(players[p].commands)):
            players[p].commands[c] = string.split(players[p].commands)

#Attempts to send a player to a room. Is called anytime a players location might require updating. Checks if they can access the room, sends them to a location accordingly and tells them about it.
def checkAccess(player, room, WORK, hour):
    if (player.location.rank >= room.rank) or (player.rank >= room.rank) or ((player.shift is room) and (WORK is True)):
        if player.location is room:
            player.message += str("At " + hour + " you stay in " + room.name + ". ")
        else:
            player.location = room
            player.message += str("Around " + hour + " you make your way to " + room.name + ". ")
    else:
        player.message += str("Around " + hour + " you fail to access " + room.name + ", and return to " + player.location.name + ". ")

#If the locate function gets caught in a loop, this fixes it and then abandons the function so it can try again
def resolveLoop(inALoop, time):
    for r in range(6):
        for l in range(len(inALoop)):
            if inALoop[l].location.rank is r + 1:
                inALoop[l].located = True
                checkAccess(inALoop[l], inALoop[l].location, False, time)
                return

#Finds the player in questions target and sees if they have been located. If they are, it sends the player there, if not it trys to locate them.
def locate(players, player, time, inALoop):
    player.visited = True
    inALoop.append(player)
    for p in range(len(players)):
        if players[p].name is player.commands[time][1]:
            if players[p].visited is True:
                resolveLoop(inALoop, time)
                return "loop"
            else:
                if players[p].located is True:
                    player.located = True
                    checkAccess(player, players[p].location, False, time)
                    return "located"
                else:
                    outcome = locate(players, players[p], time, inALoop)
                    if outcome is "located":
                        player.located = True
                        checkAccess(player, players[p].location, False, time)
                        return "located"
                    else:
                        return "loop"

#Resets the loop list and visited attribute at the end of a locate attempt
def clearLoop(players, inALoop):
            for p in range(len(players)):
                players[p].visited = False
                inALoop = []
                return inALoop

def whoHere(player, players):
    whoHere = []
    for p in range(len(players)):
        if players[p].location is player.location:
            whoHere.append(players[p])
    return whoHere
