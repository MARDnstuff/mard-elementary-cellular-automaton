from app.config.logging import setUpLogging
from app.controllers.game_of_life.life_controller import LifeController

def startLife() -> None:
    """
    LIFE Cellular Automaton Simulation (Conway's Game of Life)
    """
    life = LifeController(200, 0.5)
    life.startLife()

def startElementary() -> None:
    """
    Elementary Cellular Automaton Simulation
    """
    pass

def startWumpusWorld() -> None:
    """
    Wumpus World Simulation
    """
    pass

def main() -> None:
    setUpLogging()
    startLife()

if __name__ == "__main__":
    main()