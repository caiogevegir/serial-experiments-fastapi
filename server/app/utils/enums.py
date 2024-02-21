from enum import Enum

# ------------------------------------------------------------------------------

class GameStatus(Enum):
  BACKLOG = 'BACKLOG'
  PLAYING = 'PLAYING'
  CONTINUOUS = 'CONTINUOUS'
  HIATUS = 'HIATUS'
  FINISHED = 'FINISHED'
  DROPPED = 'DROPPED'


class OwnershipStatus(Enum):
  PHYSICAL = 'PHYSICAL'
  DIGITAL = 'DIGITAL'
  SERVICE = 'SERVICE'
  BORROWED = 'BORROWED'
  PIRATED = 'PIRATED'
