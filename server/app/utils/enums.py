from enum import Enum

# ------------------------------------------------------------------------------

class GameStatus(Enum):
  BACKLOG = 'BACKLOG'         # To be played
  PLAYING = 'PLAYING'         # Currently playing the game
  CONTINUOUS = 'CONTINUOUS'   # Game can't be finished (e.g. MMORPGs and MOBAs)
  FINISHED = 'FINISHED'       # Game is finished :)
  HIATUS = 'HIATUS'           # Stopped playing the game, but will return later
  DROPPED = 'DROPPED'         # Stopped playing the game, but won't return


class OwnershipStatus(Enum):
  PHYSICAL = 'PHYSICAL'       # Owns a physical copy of the game
  DIGITAL = 'DIGITAL'         # Owns a digital copy of the game
  SERVICE = 'SERVICE'         # Uses a service to play the game (e.g. Game Pass)
  BORROWED = 'BORROWED'       # Borrows the game from another player
  OTHER = 'OTHER'             # Plays the game by other ways
