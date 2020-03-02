class matchinfo:
    def __init__(self, matchtime, hometeam, awayteam, fullmatch, halfmatch):
        self.matchtime = matchtime
        self.hometeam = hometeam
        self.awayteam = awayteam
        self.fullmatch = fullmatch
        self.halfmatch = halfmatch


# class gameplay(object):
#     def __init__(self, id=[],flag=[]):
#         self.id = id
#         self.flag = flag


class fullmatch:
    def __init__(self, fullsolowin, letball=[], bigball=[]):
        self.solowin = fullsolowin
        self.letball = letball
        self.bigball = bigball


class halfmatch:
    def __init__(self, halfsolowin, letball=[], bigball=[]):
        self.solowin = halfsolowin
        self.letball = letball
        self.bigball = bigball
        

class halfsolowin:
    def __init__(self, oddswin, oddsdraw, oddslose):
        self.oddswin = oddswin
        self.oddsdraw = oddsdraw
        self.oddslose = oddslose


class fullsolowin:
    def __init__(self, oddswin, oddsdraw, oddslose):
        self.oddswin = oddswin
        self.oddsdraw = oddsdraw
        self.oddslose = oddslose


class letball:
    def __init__(self, pankou, left, right):
        self.pankou = pankou
        self.left = left
        self.right = right


class bigball:
    def __init__(self, pankou, left, right):
        self.pankou = pankou
        self.left = left
        self.right = right
