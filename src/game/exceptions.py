class GameError(Exception):
    pass 

class NotAbleToMatchError(GameError):
    pass

class CardAlreadyFlippedError(GameError):
    pass

class CardAlreadyMatchedError(GameError):
    pass

class PositionIsIncorrect(GameError):
    pass
