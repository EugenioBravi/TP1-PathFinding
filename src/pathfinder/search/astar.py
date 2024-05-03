from ..models.grid import Grid
from ..models.frontier import PriorityQueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class AStarSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """
        Encuentra la ruta entre dos puntos en una cuadrícula usando la búsqueda A*


        Args:
            grid (Grid): Grid of points
           
        Returns:
            Solution: Solution found
        """
        #Suma la distancia en la coordenada X de la posicion actual al destino
        # y la distancia en la coordenada Y de la posicion actuual al destino
        def heuristic_manhattan(nodo: Node, destino: tuple[int, int]) -> int:
            x1, y1 = nodo.state
            x2, y2 = destino
            return abs(x2 - x1) + abs(y2 - y1)
       
        # Creamos el nodo con la posicion inicial
        node = Node("", grid.start, 0)


        # Inicializamos el diccionario de explorados
        explored = {}
       
        # Añadimos el nodo al diccionario de explorados
        explored[node.state] = node.cost
        if node.state == grid.end:
            return Solution(node, explored)
       
        # Inicializamos la frontera con el nodo inicial
        # En este ejemplo, la frontera es una cola
        frontier = PriorityQueueFrontier()
        frontier.add(node, node.cost + heuristic_manhattan(node, grid.end))


        while True:
            # Falla si la frontera esta vacia
            if frontier.is_empty():
                return NoSolution(explored)


            # Sacamos un nodo de la frontera
            node = frontier.pop()


            # Conseguimos todos los posibles movimientos para al nodo actual
            posibles_directions = grid.get_neighbours(node.state)
            for direction in posibles_directions:


                # Seleccionamos el nuevo estado
                new_state = posibles_directions[direction]
                cost = node.cost + grid.get_cost(new_state)
                if not explored.get(new_state,False) or cost < explored[new_state]:
                    new_node = Node("", new_state, cost, parent=node, action=direction)


                    if new_node.state == grid.end:
                        return Solution(new_node, explored)
                   
                   # Guardamos el costo del nuevo estado
                    explored[new_state] = cost
                    frontier.add(new_node, cost + heuristic_manhattan(new_node, grid.end))