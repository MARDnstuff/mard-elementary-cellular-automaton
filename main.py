from app.config.logging import setUpLogging
from app.controllers.game_of_life.life_controller import LifeController
from app.controllers.elementary_cellular_automaton.elementary_controller import ElementaryController

def startLife() -> None:
    """
    LIFE Cellular Automaton Simulation (Conway's Game of Life)
    """
    life = LifeController(10, 0.5)
    life.startSimulation()

def startElementary() -> None:
    """
    Elementary Cellular Automaton Simulation
    """
    elementary = ElementaryController(100, 37)
    elementary.startSimulation()
    pass

def startWumpusWorld() -> None:
    """
    Wumpus World Simulation
    """
    pass

def main() -> None:
    setUpLogging()
    # startLife()
    startElementary()

if __name__ == "__main__":
    main()