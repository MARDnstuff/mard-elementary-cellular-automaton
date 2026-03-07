from app.config.logging import setUpLogging
from app.controllers.game_of_life.life_controller import LifeController
from app.controllers.elementary_cellular_automaton.elementary_controller import ElementaryController
from app.controllers.wumpus_world.wumpus_controller import WumpusController

def startLife() -> None:
    """
    LIFE Cellular Automaton Simulation (Conway's Game of Life)
    """
    life = LifeController(100, 0.5)
    life.startSimulation()

def startElementary() -> None:
    """
    Elementary Cellular Automaton Simulation
    """
    elementary = ElementaryController(100, 57)
    elementary.startSimulation()
    pass

def startWumpusWorld() -> None:
    """
    Wumpus World Simulation
    """
    wumpus_world = WumpusController()
    wumpus_world.startSimulation()
    pass

def main() -> None:
    setUpLogging()
    # startLife()
    # startElementary()
    startWumpusWorld()

if __name__ == "__main__":
    main()