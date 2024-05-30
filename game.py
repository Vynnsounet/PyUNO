import random
from cards import Card
from player import Player

MAX_PLAYER = 8
COLORS = 'RGBY'

class Game:

    def __init__(self,nb_players):

        self.nb_players = nb_players
        self.pioche = self.init_drawpile()
        self.player_names = [Player(input(f"Enter player's {i+1} name"),self.give_deck()) for i in range(nb_players)]
        random.shuffle(self.player_names)

    def give_deck(self):
        pass


    def init_drawpile(self):
        pass
    
