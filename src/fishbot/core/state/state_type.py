from enum import Enum, auto

class StateType(Enum):
    STARTING = auto()
    CHECKING_ROD = auto()
    CASTING_BAIT = auto()
    WAITING_FOR_BITE = auto()
    PLAYING_MINIGAME = auto()
    FINISHING = auto()