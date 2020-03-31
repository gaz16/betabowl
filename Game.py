class Game:
    myID = 1
    teams = []
    def __init__(self):
        self.teams.append(Team())
        self.teams.append(Team())
        print (len(self.teams))

    def pickTeam()

    def getCards(self):
        pass
    def getPlayers(self):
        pass
    def placePlayerOnTeam(self, Player):
        pass

class Team:
    def numPlayers(self):
        pass

class Player:
    name = None
    def __init__(self, name):
        self.name = name

class Card:
    pass

class Round:
    pass

class PlayService:
    g = Game()
    def newPlayer(self, Player, Card):
        print(Player.name)


c = Card()
p = Player("michael")  
ps = PlayService()
ps.newPlayer(p,c)