from app.models.environment.game_of_life.life_universe import LifeUniverse

class LifeController:
    def __init__(self):
        pass

    def helloToModel(self):
        my_universe = LifeUniverse(10)
        my_universe.helloWorld()