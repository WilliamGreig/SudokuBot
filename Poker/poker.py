import pydealer

PokerHandRankings = [
    "High Card",
    "Pair",
    "Two Pair",
    "Three of a Kind",
    "Straight",
    "Flush",
    "Full House",
    "Four of a Kind",
    "Straight Flush",
    "Royal Flush"
]


# define the poker game
class Poker:
    # init. a poker table / game
    def __init__(self):
        self.list_players = [Player("Logan", 30, True), Player("Khalil", 30, True)]
        self.pot = 0
        self.small_blind = 5
        self.big_blind = self.small_blind * 2
        self.deck = pydealer.Deck()

    def play(self):
        # game loop: while there are still players in the game,
        while len(self.list_players) != 1:
            self.reset()
            self.deal()
            self.collectBlind()
            # --- betting ---
            self.preFlop()
            self.flop()
            self.turn()
            self.river()
            # --- betting ---
            self.shift()

    # betting round
    def preFlop(self):
        start_index = 2 % len(self.list_players)
        i = start_index


    def flop(self):
        pass

    def turn(self):
        pass

    def river(self):
        pass

    # collect blinds from the first (big blind) and second (small blind) player
    def collectBlind(self):
        self.pot = self.pot + self.list_players[0].bet(self.small_blind) + self.list_players[1].bet(self.big_blind)

    # deal cards to all players in the game
    def deal(self):
        self.deck.shuffle()
        for p in self.list_players:
            p.hand = self.deck.deal(2)

    # shift the table, the list of players
    def shift(self):
        # first position is big blind
        # second position is small blind
        last_plc = self.list_players[len(self.list_players) - 1]
        self.list_players.pop()
        self.list_players.insert(index=0, __object=last_plc)

    def reset(self):
        self.pot = 0
        for p in self.list_players:
            p.hand = pydealer.Stack()
            p.active = True


# player represents a... player (AI or controlled)
class Player:
    def __init__(self, name, chip_amt, AI):
        self.name = name
        self.chips = chip_amt
        self.hand = pydealer.Stack()
        self.AI = AI

        # by default, assume players are active (playing)
        # if they fold, they are not active (not playing)
        self.active = True


    # bet into the pot, big/small blinds
    def bet(self, num):
        val = max(self.chips - num, 0)
        self.chips = max(self.chips - num, 0)
        return val

    def fold(self):
        self.hand = pydealer.Stack()
        self.active = False

    def call(self):
        pass

    def __str__(self):
        return self.name + "(" + str(self.chips) + " Chips):" + "\n" + str(self.hand)

    def randomAction(self):
        pass

p = Poker()
p.play()

