from app.models.environment.wumpus_world.wumpus_universe import WumpusUniverse
from app.models.environment.wumpus_world.agent import Agent
from app.views.wumpus_world.wumpus_view import WumpusView
import logging
import pygame
import sys

logger = logging.getLogger(__name__)

class WumpusController:
    """
    Controller class for Wumpus World
    """

    def __init__(self, size):
        """
        Constructor
        """
        self.my_universe = WumpusUniverse(size=size)
        self.my_agent = Agent(self.my_universe)
        self.time_velocity = 1
        self.pause = False
    
    def advanceSimulation(self) -> None:
        """
        Run the simulation, Advance the simulation on iteration
        """
        if not self.my_universe.matrix:
            logger.error("Universe is empty")
            raise Exception("Universe is not initialized properly")
        
        # new_pos = self.my_agent.chooseDirection()
        new_pos = self.my_agent.chooseDirectionFOL()
        self.my_agent.move(new_pos[0], new_pos[1])
        if new_pos == [0,0] and self.my_agent.gold:
            self.pause = True
            

    def startSimulation(self) -> None:
        """
        Start the simulation
        """
        try:
            logger.info("Starting Wumpus World simulation")
            self.view = WumpusView(self.my_universe.size)
            
            pygame.init()
            pygame.mixer.init()
            self.screen = pygame.display.set_mode((self.view.WIDTH, self.view.HEIGHT))
            pygame.display.set_caption("Wumpus Isométrico con Sprites")
            self.view.loadImages()
            self.view.scaleImages()
            self.view.loadSounds()
            self.my_universe.wumpus_scream_effect = self.view.wumpus_scream
            self.view.global_music.play(-1)
            logger.debug("Pygame initialized and screen created")
            clock = pygame.time.Clock()

            running = True

            while running:
                clock.tick(self.time_velocity)
                self.screen.fill(self.view.BLACK)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        logger.debug("End of Wumpus World Simulation")
                        pygame.quit()
                        sys.exit()

                if not self.pause:
                    self.advanceSimulation()
                else:
                    self.view.draw_win_title(self.screen, "GANASTE !")
                self.view.draw_grid(self.screen, self.my_universe)

                pygame.display.flip()
                
        except Exception as e:
            logger.error("Error in Wumpus simulation: %s", e, exc_info=True)
            sys.exit()