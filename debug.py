#!/usr/bin/env python3

import ipdb
from lib import CONN, CURSOR
from lib.classes.game import Game
from lib.classes.player import Player

if __name__ == '__main__':
    # testing data
    player1 = Player.query_all()[0]
    player2 = Player.query_all()[1]

    ipdb.set_trace()
