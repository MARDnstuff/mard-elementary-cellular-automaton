from app.models.environment.wumpus_world.wumpus_universe import WumpusUniverse
from app.models.environment.wumpus_world.cellPerception import cellPerception
import math
import logging
import pygame

logger = logging.getLogger(__name__) 

class WumpusView:
    """
    View class for Wumpus World
    """

    def __init__(self, size: int):
        """
        Constructor
        """
        # Configuration
        self.GRID_SIZE = size
        self.TILE_WIDTH = 128
        self.TILE_HEIGHT = 64
        self.WIDTH = 900
        self.HEIGHT = 700

        # Colors
        self.WHITE = (255, 255, 255)
        self.GRAY = (200, 200, 200)
        self.BLACK = (0, 0, 0)
        self.AGENT_TILE = (179, 88, 86)
        self.RED = (200, 0, 0)
        self.STENCH = (40, 97, 61)
        self.BREEZE = (57, 129, 179)
        
        # Assets
        self.agent_img_path = "assets/knight_2.png"
        self.wumpus_img_path = "assets/monster_2.png"
        self.gold_img_path = "assets/gold.png"
        self.pit_img_path = "assets/tile_pit.png"
        self.tile_img_path = "assets/tile.png"
        self.tile_breeze_img_path = "assets/tiles_breeze.png"
        self.tile_stench_img_path = "assets/tile_stench.png"
        self.tile_breeze_and_stench_img_path = "assets/tile_breeze_and_stench.png"
        self.wumpus_scream_sound_path = "assets/scream.wav"
        self.music_maze_sound_path = "assets/music_maze.wav"

        # Center map
        self.offset_x = self.WIDTH // 2
        self.offset_y = 100


    def cart_to_iso(self, x: int, y: int) -> tuple[int, int]:
        """
        Convert from cartesian to isometric coordinates
        
        :param x: x coordinate in cartesian system
        :param y: y coordinate in cartesian system
        """
        iso_x = (x - y) * (self.TILE_WIDTH // 2)
        iso_y = (x + y) * (self.TILE_HEIGHT // 2)
        return iso_x +  self.offset_x, iso_y + self.offset_y
    
    def loadImages(self) -> None:
        self.agent_img = pygame.image.load(self.agent_img_path).convert_alpha()
        self.wumpus_img = pygame.image.load(self.wumpus_img_path).convert_alpha()
        self.gold_img = pygame.image.load(self.gold_img_path).convert_alpha()
        self.pit_img = pygame.image.load(self.pit_img_path).convert_alpha()
        self.tile_img = pygame.image.load(self.tile_img_path).convert_alpha()
        self.tile_breeze_img = pygame.image.load(self.tile_breeze_img_path).convert_alpha()
        self.tile_stench_img = pygame.image.load(self.tile_stench_img_path).convert_alpha()
        self.tile_breeze_and_stench_img = pygame.image.load(self.tile_breeze_and_stench_img_path).convert_alpha()

        self.tiles = {
            (0,0): self.tile_img,
            (1,0): self.tile_stench_img,
            (0,1): self.tile_breeze_img ,
            (1,1): self.tile_breeze_and_stench_img
        }
        logger.info("Images were loaded correctly")
    
    def loadSounds(self) -> None:
        self.wumpus_scream = pygame.mixer.Sound(self.wumpus_scream_sound_path)
        self.global_music = pygame.mixer.Sound(self.music_maze_sound_path)
        self.wumpus_scream.set_volume(0.5)
        self.global_music.set_volume(0.2)


    def scaleImages(self) -> None:
        self.agent_img = pygame.transform.scale(self.agent_img, (70, 110))
        self.wumpus_img = pygame.transform.scale(self.wumpus_img, (80, 110))
        self.gold_img = pygame.transform.scale(self.gold_img, (60, 60))
        self.pit_img = pygame.transform.scale(self.pit_img, (self.TILE_WIDTH, self.TILE_HEIGHT))
        for key in self.tiles:
            self.tiles[key] = pygame.transform.scale(
                self.tiles[key],
                (self.TILE_WIDTH, self.TILE_HEIGHT)
            )
        logger.info("Images were scaled correctly")
    
    def draw_win_title(self, screen, text: str) -> None:
        font = pygame.font.SysFont("Arial", 72)
        win_text = font.render(text, True, (255,215,0))
        screen.blit(win_text, (self.WIDTH // 2,450))
        

    def draw_tile(self, screen, x: int, y: int, cell: cellPerception) -> None:
        iso_x, iso_y = self.cart_to_iso(x, y)

        # get perceptions
        stench = cell.perception[0]
        breeze = cell.perception[1]

        # select tile
        tile = self.tiles[(stench, breeze)]
        
        if cell.type == "P":
            tile = self.pit_img
        
        # ajustar posición porque iso_x es el centro superior
        draw_x = iso_x - self.TILE_WIDTH // 2
        draw_y = iso_y

        screen.blit(tile, (draw_x, draw_y))
        # logger.debug("Tile has been drawn")

    def draw_character(self, screen, img, x: int, y: int) -> None:
        iso_x, iso_y = self.cart_to_iso(x, y)

        sprite_width = img.get_width()
        sprite_height = img.get_height()

        screen.blit(
            img,
            (
                iso_x - sprite_width // 2,
                iso_y + self.TILE_HEIGHT // 2 - sprite_height
            )
        )
        # logger.debug("Character has been drawn")


    def draw_grid(self, screen, my_universe: WumpusUniverse) -> None:
        for x, row  in enumerate(my_universe.matrix):
            for y, col in enumerate(row):
                self.draw_tile(screen, x, y, col)

                # Draw Wumpus
                if my_universe.matrix[x][y].type == my_universe.WUMPUS:
                    self.draw_character(screen, self.wumpus_img, x, y)

                # Draw Agent and his tile
                if [x, y] == my_universe.agent_pos:
                    self.draw_character(screen, self.agent_img, x, y)

                # Draw Gold
                if my_universe.matrix[x][y].type == my_universe.GOLD:
                    self.draw_character(screen, self.gold_img, x, y)
        # logger.debug("Grid has been drawn correctly")
                