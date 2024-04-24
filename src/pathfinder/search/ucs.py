from ..models.grid import Grid
from ..models.frontier import PriorityQueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node

class UniformCostSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Uniform Cost Search

        Args:
            grid (Grid): Grid of points

        Returns:
            Solution: Solution found
        """
        # Creamos el nodo con la posicion inicial
        node = Node("", grid.start, 0)

        # Inicializamos el diccionario de explorados
        explored = {}
       
        # Añadimos el nodo al diccionario de explorados
        explored[node.state] = node.cost
        if node.state == grid.end:
            return Solution(node, explored)
        
        # Initialize the frontier with the initial node
        # In this example, the frontier is a queue
        frontier = PriorityQueueFrontier()
        frontier.add(node)

        while True:
            #  Fail if the frontier is empty
            if frontier.is_empty():
                return NoSolution(explored)

            # Remove a node from the frontier
            node = frontier.pop()

            # Go right
            successors = grid.get_neighbours(node.state)
            for direccion_movimiento in successors:

                # Get the successor
                movimiento = successors[direccion_movimiento]
                cost = node.cost + grid.get_cost(movimiento)
                if not explored.get(movimiento,False) or cost < explored.get(movimiento,False):
                    new_node = Node("", movimiento,
                                    cost,
                                    parent=node, action=direccion_movimiento)

                    if new_node.state == grid.end:
                        return Solution(new_node, explored)
                    
                   # Mark the successor as reached
                    explored[movimiento] = cost
                    frontier.add(new_node,cost)