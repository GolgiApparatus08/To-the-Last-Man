class medical(location):
    def __init__(self, rank):
        self.rank = rank
        self.sabotages = 0
        self.workload = 0
        self.functionality = True
        
    def visit(player):
        
        #Check Rank
        Access = rankCheck(player)
        if Access is false:
            return

        #Change Location
        player.location = location
            
        #Effect
        if "cuts" in player.marks and "bruises" not in player.marks:
            player.marks.clear()
            player.message += str("Around " + time + ", you use the advanced systems in medical to seal up most of your cuts from the earlier fight. Tomorrow morning, no one will be the wiser. ")
        elif "cuts" not in player.marks and "bruises" in player.marks:
            player.marks.clear()
            player.message += str("Around " + time + ", you use the advanced systems in medical to rapidly heal most of your bruises from the earlier fight. Tomorrow morning, no one will be the wiser. ")
        elif "cuts" in player.marks and "bruises" in player.marks:
            player.marks.clear()
            player.message += str("Around " + time + ", you use the advanced systems in medical to rapidly heal all of your cuts and bruises from those earlier fights. Tomorrow morning, no one will be the wiser. ")
        else:
            player.message += str("Around " + time + ", you visit medical. )