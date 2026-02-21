from abc import ABC, abstractmethod

class Simulation(ABC):
    """
    Abstract base class for simulations
    """
    @abstractmethod
    def advanceSimulation(self) -> list[list]:
        """
        Advance the simulation by one step
        
        :return: The updated matrix representing the simulation state
        :rtype: list[list]
        """
        pass
    
    @abstractmethod
    def startSimulation(self) -> None:
        """
        Initiates the Simulation 
        """
        pass
