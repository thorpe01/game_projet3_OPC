from gardien import Gardien
from player import Player
from seringue import Seringue


class Game:
    def __init__(self):
        self.player = Player()
        self.pressed = {}
        self.gardien = Gardien()
        self.seringue = Seringue()
