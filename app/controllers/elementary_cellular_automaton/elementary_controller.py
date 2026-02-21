from app.models.environment.elementary_cellular_automaton.elementary_universe import ElementaryUniverse
from app.views.elementary_cellular_automaton.elementary_view import ElementaryView
from app.controllers.simulation import Simulation
from app.controllers.utils.utils import positive
import logging
import pygame
import sys

logger = logging.getLogger(__name__)

class ElementaryController(Simulation):
    """
    Controller class for Elementary Cellular Automaton
    """

    def __init__(self, size: int = 3, rule: int = 30):
        """
        Constructor
        
        :param size: Size of the grid
        :type size: int
        """
        self.my_universe = ElementaryUniverse(size, rule)
        self.my_universe.populateSpace()
        self.time_velocity = 5
        self.age = 0

    def advanceSimulation(self):
        """
        Advance Simulation by one time step
        """
        if not self.my_universe.matrix:
            logger.error("Universe is empty")
            raise Exception("Universe is not initialized properly")

        new_row = []
        row = self.my_universe.matrix[-1]
        for j, _ in enumerate(row):

            right = self.my_universe.matrix[-1][(j + 1)%self.my_universe.size]
            center = self.my_universe.matrix[-1][j]
            left = self.my_universe.matrix[-1][positive(j - 1, self.my_universe.size)%self.my_universe.size]
            
            # 001 << 1 = 100 OR 001 << 1 = 010 OR 001 == 111
            curr_state  = (left << 2) | (center << 1) | right
            next_state = self.my_universe.rule[curr_state]

            new_row.append(next_state)

        self.my_universe.matrix.append(new_row)
        self.age += 1
        self.view.ROWS = len(self.my_universe.matrix)
        logger.debug("Simulation advanced by one iteration -> Age: %d", self.age)

    def startSimulation(self):
        """
        Start Simulation
        """
        try:
            logger.info("Starting Elementary CA simulation")
            self.view = ElementaryView(self.my_universe.size)
            
            pygame.init()
            self.screen = pygame.display.set_mode((self.view.WIDTH, self.view.HEIGHT))
            logger.debug("Pygame initialized and screen created")
            pygame.display.set_caption("Grid con Pygame")

            clock = pygame.time.Clock()
            
            # Main loop
            running = True
            n = 0
            while running:
                clock.tick(self.time_velocity)
                self.screen.fill(self.view.BG_COLOR)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        logger.info("Ending Elementary CA simulation")
                        running = False
                self.view.draw_grid(self.screen)
                if n <= (self.my_universe.size // 2) - 1:
                    self.advanceSimulation()
                self.view.update_grid(self.screen, self.my_universe.matrix, self.my_universe.size)
                pygame.display.flip()
                n += 1

            pygame.quit()
            sys.exit()
        except Exception as e:
            logger.error("Error in Elementary CA simulation: %s", e, exc_info=True)
            sys.exit()


