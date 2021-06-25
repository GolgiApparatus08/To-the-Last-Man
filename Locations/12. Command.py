class command(location):
    def __init__(self, rank):
        self.rank = rank
        self.sabotages = 0
        self.workload = 0
        self.functionality = True
        
    def visit(player, target):
        
        #Check Rank
        location = command
        locationRank = 6
        Access = rankCheck()
        if Access is false:
            return

        #Change Location
        player.location = location

        #Effect
        player.message += str("Around " + time + ", you visit command to see if the base's highest ranking records might reveal something useful about " + target.name + ". You discover that their rank is " + target.rank + " and their currently assigned to the " + shift + " shift. ")