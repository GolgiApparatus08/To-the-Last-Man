class armaments(location):
    def __init__(self, rank):
        self.rank = rank
        self.sabotages = 0
        self.workload = 0
        self.functionality = True
        
    def visit(player, target):
        
        #Check Rank
        location = armaments
        locationRank = 5
        Access = rankCheck()
        if Access is false:
            return

        #Change Location
        player.location = location
            
        #Effect
        player.message += str("Around " + time + ", you stop by armaments to see if you can learn anything useful about " + target.name + ". From the training logs, you discover that their strength is " + target.strength + " and that they have " + target.weapon + " (" + target.weaponType + ") on hand that that they could use to kill. ")