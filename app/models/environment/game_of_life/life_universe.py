from app.models.environment.universe import Universe

class LifeUniverse(Universe):
    def __init__(self, size = 3):
        super().__init__(size)
        self.Smin: int = 2
        self.Smax: int = 3
        self.Nmin: int = 3
        self.Nmax: int = 3
        




