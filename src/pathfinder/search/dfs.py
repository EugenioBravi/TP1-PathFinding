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
        # Inicializamos el nodo en la posicion inicial
        node = Node("", grid.start, 0)

        # Inicializamos el diccionaio vacio
        explored = {}
       
        # Agregamos el nodo al diccionario de explorados
        explored[node.state] = True
        if node.state == grid.end:
            return Solution(node, explored)
        # Inicializamos la pila con el nodo inicial
        frontier = StackFrontier()
        frontier.add(node)

        while True:
            # Si la frontera esta vacia, no hay solucion
            if frontier.is_empty():
                return NoSolution(explored)

            # Sacamos un nodo de la frontera
            node = frontier.remove()

            # Conseguimos todos los posibles movimientos
            successors = grid.get_neighbours(node.state)
            for direccion_movimiento in successors:

                # Seleccionamos el sucesor
                movimiento = successors[direccion_movimiento]
                if not explored.get(movimiento,False):
                    new_node = Node("", movimiento,
                                    node.cost + grid.get_cost(movimiento),
                                    parent=node, action=direccion_movimiento)

                    if new_node.state == grid.end:
                        return Solution(new_node, explored)
                   
                    # Se marca al sucesor como alcanzado
                    explored[movimiento] = True
                    frontier.add(new_node)