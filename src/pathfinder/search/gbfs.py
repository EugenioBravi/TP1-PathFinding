from ..models.grid import Grid
from ..models.frontier import PriorityQueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node
from math import sqrt


class GreedyBestFirstSearch:
    @staticmethod


    def search(grid: Grid) -> Solution:
        """
        Find path between two points in a grid using Greedy Best First Search


        Args:
            grid (Grid): Grid of points


        Returns:
            Solution: Solution found
        """
        #Calcula la distancia en linea recta del nodo actual al destino
        def heuristic(nodo: Node, destiny: tuple[int, int]) -> int:
            distance = round(sqrt((destiny[0]-nodo.state[0])**2 + (destiny[1]-nodo.state[1])**2))
            return distance
       
        # Creamos el nodo con la posicion inicial
        node = Node("", grid.start, 0)


        # Inicializamos el diccionario de explorados
        explored = {}
       
        # Añadimos el nodo al diccionario de explorados
        explored[node.state] = node.cost
        if node.state == grid.end:
            return Solution(node, explored)
       
        # Se inicializa la frontera con el nodo inicial
        # En este ejemplo la frontera es una cola de prioridad
        frontier = PriorityQueueFrontier()
        frontier.add(node,heuristic(node, grid.end))


        while True:
            # Si la frontera esta vacia, no hay solucion
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
                    new_node = Node("", new_state,
                                    cost,
                                    parent=node, action=direction)


                    if new_node.state == grid.end:
                        return Solution(new_node, explored)
                   
                   # Guardamos el costo del nuevo estado
                    explored[new_state] = cost
                    frontier.add(new_node,heuristic(new_node, grid.end))