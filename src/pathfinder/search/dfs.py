from ..models.grid import Grid
from ..models.frontier import StackFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class DepthFirstSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """
        Encuentra la ruta entre dos puntos en una cuadrícula usando Búsqueda en profundidad.


        Args:
            grid (Grid): Grid of points
           
        Returns:
            Solution: Solution found
        """
        # Inicializamos el nodo en la posicion inicial
        node = Node("", grid.start, 0)

        # Inicializamos el diccionaio de nodos explorados vacio
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

            # Conseguimos todos los posibles movimientos para al nodo actual
            posibles_directions = grid.get_neighbours(node.state)
            for direction in posibles_directions:


                # Seleccionamos el nuevo estado
                new_state = posibles_directions[direction]
                if not explored.get(new_state,False):
                    new_node = Node("", new_state,
                                    node.cost + grid.get_cost(new_state),
                                    parent=node, action=direction)


                    if new_node.state == grid.end:
                        return Solution(new_node, explored)
                   
                    # Se marca al nuevo estado como alcanzado
                    explored[new_state] = True
                    frontier.add(new_node)