class SessionState:
    sessionStarted = False

    @classmethod
    def reset(cls):
        cls.sessionStarted = False