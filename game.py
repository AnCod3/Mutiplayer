class Game:
    def __init__(self, id):
        #whether or not the player went
        self.p1Went = False
        self.p2Went = False
        self.ready = False
        #game session id
        self.id = id
        self.moves = [None, None]
        self.wins = [0,0]
        self.ties = 0
    #get player moves
    def get_player_move(self, p):
        """
        pass the value of 0 or 1
        0=p1
        1=p2
        :param p: [0,1]
        :return: Move
        """
        return self.moves[p]

    def play(self, player, move):
        self.moves[player] = move
        if player == 0:
            self.p1Went = True
        else:
            self.p2Went = True

    def connected(self):
        #if two players are connected to the game
        return self.ready

    def bothWent(self):
        return self.p1Went and self.p2Went

    def winner(self):
        #check the first letter of each move so to see who won
        #we don't want to check the whole word just first letter
        p1 = self.moves[0].upper()[0]
        p2 = self.moves[1].upper()[0]

        #winner value is -1 because if player 1 wins it will be 0
        #if player 2 wins it's one
        winner = -1
        if p1 == "R" and p2 == "S":
            winner = 0
        elif p1 == "S" and p2 == "R":
            winner = 1
        elif p1 == "P" and p2 == "R":
            winner = 0
        elif p1 == "R" and p2 == "P":
            winner = 1
        elif p1 == "S" and p2 == "P":
            winner = 0
        elif p1 == "P" and p2 == "S":
            winner = 1
        return winner

    def resetWent(self):
        self.p1Went = False
        self.p2Went = False