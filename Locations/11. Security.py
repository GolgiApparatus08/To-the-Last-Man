class security(location):
    def __init__(self, rank):
        self.rank = rank
        self.sabotages = 0
        self.workload = 0
        self.functionality = True
        
    def visit(player, target):
        
        #Check Rank
        location = security
        locationRank = 6
        Access = rankCheck()
        if Access is false:
            return

        #Change Location
        player.location = location
            
        #Effect
        player.message += str("Around " + time + ", you visit security and search " + target.name + "'s name in the tracking database. On a projected map, you see a blip light up in " + target.location + ". ")