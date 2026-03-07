from app.models.environment.wumpus_world.wumpus_universe import WumpusUniverse
from app.views.wumpus_world.wumpus_view import WumpusView
import logging
import pygame
import sys



logger = logging.getLogger(__name__)

class WumpusController:
    """
    Controller class for Wumpus World
    """

    def __init__(self):
        """
        Constructor
        """
        self.my_universe = WumpusUniverse()
        self.my_view = WumpusView(self.my_universe.size)
        self.time_velocity = 60
    
    def advanceSimulation(self) -> None:
        """
        Run the simulation, Advance the simulation on iteration
        """
        pass
    
    def startSimulation(self) -> None:
        """
        Start the simulation
        """
        try:
            logger.info("Starting Wumpus World simulation")
            
            pygame.init()
            screen = pygame.display.set_mode((self.my_view.WIDTH, self.my_view.HEIGHT))
            pygame.display.set_caption("Wumpus Isométrico con Sprites")
            logger.debug("Pygame initialized and screen created")
            clock = pygame.time.Clock()

            running = True

            while running:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_UP and self.my_universe.agent_pos[1] > 0:
                            self.my_universe.agent_pos[1] -= 1
                        if event.key == pygame.K_DOWN and self.my_universe.agent_pos[1] < self.my_universe.size - 1:
                            self.my_universe.agent_pos[1] += 1
                        if event.key == pygame.K_LEFT and self.my_universe.agent_pos[0] > 0:
                            self.my_universe.agent_pos[0] -= 1
                        if event.key == pygame.K_RIGHT and self.my_universe.agent_pos[0] < self.my_universe.size - 1:
                            self.my_universe.agent_pos[0] += 1

                screen.fill(self.my_view.WHITE)
                self.my_view.draw_grid(screen, self.my_universe)

                pygame.display.flip()
                clock.tick(self.time_velocity)
        except Exception as e:
            logger.error("Error in Wumpus simulation: %s", e)
            sys.exit()