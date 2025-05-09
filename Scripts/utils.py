class SessionState:
    sessionStarted = False

    @classmethod
    def reset(cls):
        cls.sessionStarted = False

class GameMode:
    gameModes = {
        1: "Grid",
        2: "Random"
    }

    currentGameMode = None

    @classmethod
    def switch(cls, mode):
        if mode in cls.gameModes:
            cls.currentGameMode = mode
        else:
            print("Gamemode index above game mode amounts")
            
    
    @classmethod
    def reset(cls):
        cls.currentGameMode = None

targetsOnScreen = 0