from app.models.environment.wumpus_world.wumpus_universe import WumpusUniverse, cellPerception
import logging
import pygame

logger = logging.getLogger(__name__)

class Agent:
    def __init__(self, env: WumpusUniverse):
        # identification
        self.id = env.AGENT
        # Initial configuration
        self.my_pos: tuple[int,int] = env.agent_pos
        self.my_curr_perception: cellPerception = env.matrix[self.my_pos[0]][self.my_pos[1]]
        self.env = env
        
        # False means the agent it's not carrying the gold
        self.gold = False
        # True means the agent has one arrow available
        self.arrow = True
        # True means the agent is alive
        self.alive = True
        # Memory
        self.visited = set()
        # Previous position
        self.prev_pos = [0, 0]

        # Gold sound effect
        pygame.mixer.init()
        self.gold_effect = pygame.mixer.Sound("assets/gold_sound.wav")
        self.gold_effect.set_volume(0.5)
        
    def move(self, x: int, y: int) -> None:
        # save previous position
        self.prev_pos = self.my_pos
        # End game
        if [x, y] == [0, 0] and self.gold:
            logger.info("Agent has returned with the Gold!")

        # Clean
        self.env.matrix[self.my_pos[0]][self.my_pos[1]].type = None
        # Move
        self.my_pos = [x, y]
        self.my_curr_perception = self.env.matrix[x][y]
        self.env.agent_pos = self.my_pos
        self.visited.add((x,y))
        logger.info(f"Agent is now in [{x}, {y}]")
        

    def takeGold(self, x: int, y: int) -> None:
        self.gold = True
        self.env.matrix[x][y].perception[2] = 0
        self.env.matrix[x][y].type = None
        self.gold_effect.play(fade_ms=1)
        logger.info("Agent has taken the gold")
        pass

    def shotArrow(self, x: int, y: int) -> None:
        # Kill Wumpus
        self.env.matrix[x][y].type = None
        self.arrow = False
        self.env.wumpus_scream_effect.play()

    def chooseDirection(self) -> tuple[int, int]:
        x, y = self.my_pos
        self.visited.add(tuple(self.my_pos))
        valid_option = []

        logger.info(f" -> {self.env.matrix[x][y].type}")
        # Take the gold
        if self.env.matrix[x][y].type == self.env.GOLD:
            self.takeGold(x, y)
            

        # Find Wumpus in same room
        if self.env.matrix[x][y].type == self.env.WUMPUS:
            self.alive = False
            return

        directions = [
            (x-1, y),  # up
            (x+1, y),  # down
            (x, y+1),  # right
            (x, y-1)   # left
        ]

        for nx, ny in directions:
            if 0 <= nx < self.env.size and 0 <= ny < self.env.size:
                # found a PIT or a WUMPUS
                if self.env.matrix[nx][ny].type != self.env.PIT and self.env.matrix[nx][ny].type != self.env.WUMPUS:
                    cell = self.env.matrix[nx][ny]
                    weight = cell.perception[0] + cell.perception[1]
                    # Penalización si trata de visitar una posición anterior
                    if self.prev_pos == [nx, ny]:
                        weight += 3
                    visited = (nx, ny) in self.visited
                    valid_option.append((weight, visited, [nx, ny]))
                elif self.env.matrix[nx][ny].type == self.env.WUMPUS and self.arrow:
                    self.shotArrow(nx,ny)

            else:
                logger.info("Bump")
        
        # Sort the array, the first element should be the best option
        valid_option.sort()
        if valid_option:
            best_move = valid_option[0][2]
            return best_move
        else:
            raise Exception("The Agent is stuck")
    
    def chooseDirectionFOL(self) -> tuple[int, int]:
        x, y = self.my_pos
        self.visited.add((x, y))

        current_cell = self.env.matrix[x][y]

        logger.info(f" -> {current_cell.type}")

        # Regla FOL: At(x,y) ∧ Gold(x,y) -> TakeGold
        if current_cell.type == self.env.GOLD:
            self.takeGold(x, y)

        # Regla FOL: At(x,y) ∧ Wumpus(x,y) -> Dead
        if current_cell.type == self.env.WUMPUS:
            self.alive = False
            return

        # Percepciones actuales
        breeze = current_cell.perception[0]  # Breeze -> posible PIT cerca
        stench = current_cell.perception[1]  # Stench -> posible Wumpus cerca

        directions = [
            (x-1, y),  # up
            (x+1, y),  # down
            (x, y+1),  # right
            (x, y-1)   # left
        ]

        safe_moves = []
        risky_moves = []

        for nx, ny in directions:
            # Regla: Adjacent(x,y,nx,ny)
            if 0 <= nx < self.env.size and 0 <= ny < self.env.size:

                cell = self.env.matrix[nx][ny]

                # Regla FOL:
                # ¬Breeze ∧ ¬Stench -> Safe(nx,ny)
                is_safe = (breeze == 0 and stench == 0)

                if is_safe:
                    # Safe(nx,ny)
                    if (nx, ny) not in self.visited:
                        safe_moves.append((nx, ny))
                    else:
                        # visitado pero seguro
                        risky_moves.append((nx, ny))

                else:
                    # No es seguro -> posible riesgo
                    if cell.type == self.env.WUMPUS and self.arrow:
                        # Regla: Stench -> posible Wumpus -> acción
                        self.shotArrow(nx, ny)
                    else:
                        risky_moves.append((nx, ny))
            else:
                logger.info("Bump")

        # Regla: elegir Safe ∧ ¬Visited primero
        if safe_moves:
            return safe_moves[0]

        # Regla fallback: Safe aunque ya visitado
        if risky_moves:
            return risky_moves[0]

        raise Exception("The Agent is stuck")