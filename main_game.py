from enum import Enum, auto
import enum
import datetime

import pgzrun

# Window Size
WIDTH = 1024
HEIGHT = 768

# Simple Enum for items
class FactoryTypes(Enum):
    IronBuyer = auto()
    IronFoundry = auto()
    IronSeller = auto()

# Expandable class for the factory items
class ProcessItem(object):
    def __init__(self, factory_item):
        self.FacType = factory_item

# Overall game state, ticks, items purchased, positions
class GameState(object):
    def __init__(self, ticks=0):
        self.game_time = datetime.datetime.now()
        self.ticks_passed = ticks
        self.tickTime = 0

        self.ticksPerSecond = 10
        self.totalTickTime = 1/self.ticksPerSecond

        self.owned = []
        self.score = 0

    def IncrementTicks(self, by=1):
        # Update the counter
        self.ticks_passed += by
        # Reset the time passed for the tick
        self.tickTime = 0

# New instance of the game
the_game = GameState()
the_game.owned.append(ProcessItem(FactoryTypes.IronBuyer))

def update(dt):
    # Add the interval to the tick time
    the_game.tickTime += dt

    # Has there been enough time passed to do a tick?
    if the_game.tickTime >= the_game.totalTickTime:
        # Add a "tick" to the game counter
        the_game.IncrementTicks()

    the_game.game_time = datetime.datetime.now()

def draw():
    screen.clear()
    screen.draw.text("Number of ticks: " + str(the_game.ticks_passed), (10, 10))


if __name__ == "__main__":
    pgzrun.go()
