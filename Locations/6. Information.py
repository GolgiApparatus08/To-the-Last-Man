class information(location):
    def __init__(self, rank):
        self.rank = rank
        self.sabotages = 0
        self.workload = 0
        self.functionality = True
        
    def visit(player, target):
        
        #Check Rank
        location = information
        locationRank = 3
        Access = rankCheck()
        if Access is false:
            return

        #Change Location
        player.location = location
            
        #Effect
        player.message += str("Around " + time + ", you scour all the files you can find on " + target.name + " in information, and eventually discover their intellect is " + target.intellect + " and their nerves is " + target.nerves + ". ")