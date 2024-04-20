from ..models.grid import Grid
from ..models.frontier import StackFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class DepthFirstSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Depth First Search

        Args:
            grid (Grid): Grid of points
           
        Returns:
            Solution: Solution found
        """
        # Initialize a node with the initial position
        node = Node("", grid.start, 0)

        # Initialize the explored dictionary to be empty
        explored = {}
       
        # Add the node to the explored dictionary
        explored[node.state] = True
        if node.state == grid.end:
            return Solution(node, explored)
        # Initialize the frontier with the initial node
        # In this example, the frontier is a queue
        frontier = StackFrontier()
        frontier.add(node)

        while True:
            #  Fail if the frontier is empty
            if frontier.is_empty():
                return NoSolution(explored)

            # Remove a node from the frontier
            node = frontier.remove()

            # Go right
            successors = grid.get_neighbours(node.state)
            for direccion_movimiento in successors:

                # Get the successor
                movimiento = successors[direccion_movimiento]
                if not explored.get(movimiento,False):
                    new_node = Node("", movimiento,
                                    node.cost + grid.get_cost(movimiento),
                                    parent=node, action=direccion_movimiento)

                    # Mark the successor as reached
                    if new_node.state == grid.end:
                        return Solution(new_node, explored)
                   
                    explored[movimiento] = True
                    frontier.add(new_node)