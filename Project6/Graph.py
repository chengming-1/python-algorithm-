"""
Name:chengming Wang
CSE 331 FS20 (Onsay)
"""

import heapq
import itertools
import math
import queue
import random
import time
from typing import TypeVar, Callable, Tuple, List, Set

import matplotlib.cm as cm
import matplotlib.patches as patches
import matplotlib.pyplot as plt
import numpy as np

T = TypeVar('T')
Matrix = TypeVar('Matrix')  # Adjacency Matrix
Vertex = TypeVar('Vertex')  # Vertex Class Instance
Graph = TypeVar('Graph')  # Graph Class Instance


class Vertex:
    """ Class representing a Vertex object within a Graph """

    __slots__ = ['id', 'adj', 'visited', 'x', 'y']

    def __init__(self, idx: str, x: float = 0, y: float = 0) -> None:
        """
        DO NOT MODIFY
        Initializes a Vertex
        :param idx: A unique string identifier used for hashing the vertex
        :param x: The x coordinate of this vertex (used in a_star)
        :param y: The y coordinate of this vertex (used in a_star)
        """
        self.id = idx
        self.adj = {}  # dictionary {id : weight} of outgoing edges
        self.visited = False  # boolean flag used in search algorithms
        self.x, self.y = x, y  # coordinates for use in metric computations

    def __eq__(self, other: Vertex) -> bool:
        """
        DO NOT MODIFY
        Equality operator for Graph Vertex class
        :param other: vertex to compare
        """
        if self.id != other.id:
            return False
        elif self.visited != other.visited:
            print(f"Vertex '{self.id}' not equal")
            print(f"Vertex visited flags not equal: self.visited={self.visited},"
                  f" other.visited={other.visited}")
            return False
        elif self.x != other.x:
            print(f"Vertex '{self.id}' not equal")
            print(f"Vertex x coords not equal: self.x={self.x}, other.x={other.x}")
            return False
        elif self.y != other.y:
            print(f"Vertex '{self.id}' not equal")
            print(f"Vertex y coords not equal: self.y={self.y}, other.y={other.y}")
            return False
        elif set(self.adj.items()) != set(other.adj.items()):
            diff = set(self.adj.items()).symmetric_difference(set(other.adj.items()))
            print(f"Vertex '{self.id}' not equal")
            print(f"Vertex adj dictionaries not equal:"
                  f" symmetric diff of adjacency (k,v) pairs = {str(diff)}")
            return False
        return True

    def __repr__(self) -> str:
        """
        DO NOT MODIFY
        Represents Vertex object as string.
        :return: string representing Vertex object
        """
        lst = [f"<id: '{k}', weight: {v}>" for k, v in self.adj.items()]

        return f"<id: '{self.id}'" + ", Adjacencies: " + "".join(lst) + ">"

    def __str__(self) -> str:
        """
        DO NOT MODIFY
        Represents Vertex object as string.
        :return: string representing Vertex object
        """
        return repr(self)

    def __hash__(self) -> int:
        """
        DO NOT MODIFY
        Hashes Vertex into a set; used in unit tests
        :return: hash value of Vertex
        """
        return hash(self.id)

    # ============== Modify Vertex Methods Below ==============#

    def degree(self) -> int:
        """
        Description.
        Returns the number of outgoing edges from this vertex
        :return: number of outgoing edges from this vertex
        """
        return len(self.adj)

    def get_edges(self) -> Set[Tuple[str, float]]:
        """
        Description.
        :return:
        """
        output: Set[Tuple[str, float]] = set()
        for key in self.adj:
            output.add((key, self.adj[key]))
        return output

    def euclidean_distance(self, other: Vertex) -> float:
        """
        Description.
        :param other:
        :return:
        """
        return math.sqrt(pow(other.x - self.x, 2) + pow(other.y - self.y, 2))

    def taxicab_distance(self, other: Vertex) -> float:
        """
        Description.
        :param other:
        :return:
        """
        return abs(other.x - self.x) + abs(other.y - self.y)


class Graph:
    """ Class implementing the Graph ADT using an Adjacency Map structure """

    __slots__ = ['size', 'vertices', 'plot_show', 'plot_delay']

    def __init__(self, plt_show: bool = False, matrix: Matrix = None, csv: str = "") -> None:
        """
        DO NOT MODIFY
        Instantiates a Graph class instance
        :param: plt_show : if true, render plot when plot() is called; else, ignore calls to plot()
        :param: matrix : optional matrix parameter used for fast construction
        :param: csv : optional filepath to a csv containing a matrix
        """
        matrix = matrix if matrix else np.loadtxt(csv, delimiter=',') if csv else None
        self.size = 0
        self.vertices = {}

        self.plot_show = plt_show
        self.plot_delay = 0.2

        if matrix is not None:
            self.matrix2graph(matrix)

    def __eq__(self, other: Graph) -> bool:
        """
        DO NOT MODIFY
        Overloads equality operator for Graph class
        :param other: graph to compare
        """
        if self.size != other.size or len(self.vertices) != len(other.vertices):
            print(f"Graph size not equal: self.size={self.size}, other.size={other.size}")
            return False
        else:
            for vertex_id, vertex in self.vertices.items():
                other_vertex = other.get_vertex(vertex_id)
                if other_vertex is None:
                    print(f"Vertices not equal: '{vertex_id}' not in other graph")
                    return False

                adj_set = set(vertex.adj.items())
                other_adj_set = set(other_vertex.adj.items())

                if not adj_set == other_adj_set:
                    print(f"Vertices not equal: adjacencies of '{vertex_id}' not equal")
                    print(f"Adjacency symmetric difference = "
                          f"{str(adj_set.symmetric_difference(other_adj_set))}")
                    return False
        return True

    def __repr__(self) -> str:
        """
        DO NOT MODIFY
        Represents Graph object as string.
        :return: String representation of graph for debugging
        """
        return "Size: " + str(self.size) + ", Vertices: " + str(list(self.vertices.items()))

    def __str__(self) -> str:
        """
        DO NOT MODIFY
        Represents Graph object as string.
        :return: String representation of graph for debugging
        """
        return repr(self)

    def plot(self) -> None:
        """
        DO NOT MODIFY
        Creates a plot a visual representation of the graph using matplotlib
        :return: None
        """
        if self.plot_show:

            # if no x, y coords are specified, place vertices on the unit circle
            for i, vertex in enumerate(self.get_vertices()):
                if vertex.x == 0 and vertex.y == 0:
                    vertex.x = math.cos(i * 2 * math.pi / self.size)
                    vertex.y = math.sin(i * 2 * math.pi / self.size)

            # show edges
            num_edges = len(self.get_edges())
            max_weight = max([edge[2] for edge in self.get_edges()]) if num_edges > 0 else 0
            colormap = cm.get_cmap('cool')
            for i, edge in enumerate(self.get_edges()):
                origin = self.get_vertex(edge[0])
                destination = self.get_vertex(edge[1])
                weight = edge[2]

                # plot edge
                arrow = patches.FancyArrowPatch((origin.x, origin.y),
                                                (destination.x, destination.y),
                                                connectionstyle="arc3,rad=.2",
                                                color=colormap(weight / max_weight),
                                                zorder=0,
                                                **dict(arrowstyle="Simple,tail_width=0.5,"
                                                                  "head_width=8,head_length=8"))
                plt.gca().add_patch(arrow)

                # label edge
                plt.text(x=(origin.x + destination.x) / 2 - (origin.x - destination.x) / 10,
                         y=(origin.y + destination.y) / 2 - (origin.y - destination.y) / 10,
                         s=weight, color=colormap(weight / max_weight))

            # show vertices
            x = np.array([vertex.x for vertex in self.get_vertices()])
            y = np.array([vertex.y for vertex in self.get_vertices()])
            labels = np.array([vertex.id for vertex in self.get_vertices()])
            colors = np.array(
                ['yellow' if vertex.visited else 'black' for vertex in self.get_vertices()])
            plt.scatter(x, y, s=40, c=colors, zorder=1)

            # plot labels
            for j, _ in enumerate(x):
                plt.text(x[j] - 0.03 * max(x), y[j] - 0.03 * max(y), labels[j])

            # show plot
            plt.show()
            # delay execution to enable animation
            time.sleep(self.plot_delay)

    # ============== Modify Graph Methods Below ==============#

    def reset_vertices(self) -> None:
        """
        to reset vertices
        :return: orinal
        """
        for vertex_id in self.vertices:
            vertex: Vertex = self.vertices[vertex_id]
            vertex.visited = False

    def get_vertex(self, vertex_id: str) -> Vertex:
        """
        get the vertex
        :param vertex_id:the point
        :return: self.vertices
        """
        for v_id in self.vertices:
            if v_id == vertex_id:
                return self.vertices[v_id]
        return None

    def get_vertices(self) -> Set[Vertex]:
        """
        add to store
        :return:list of vertex
        """
        outputSet: Set[Vertex] = set()
        for vertex_id in self.vertices:
            outputSet.add(self.vertices[vertex_id])
        return outputSet

    def get_edge(self, start_id: str, dest_id: str) -> Tuple[str, str, float]:
        """
        get the edge info
        :param start_id: start point
        :param dest_id:end point
        :return: the compose of edge
        """
        for vertex_id in self.vertices:
            if vertex_id == start_id:
                start_vertex: Vertex = self.vertices[vertex_id]
                for end_vertex in start_vertex.adj:
                    if end_vertex == dest_id:
                        return start_id, dest_id, start_vertex.adj[end_vertex]
        return None

    def get_edges(self) -> Set[Tuple[str, str, float]]:
        """
        store edges
        :return: edges list
        """
        edges: Set[Tuple[str, str, float]] = set()
        for vertex_id in self.vertices:
            for adjacent in self.vertices[vertex_id].adj:
                edges.add((vertex_id, adjacent, self.vertices[vertex_id].adj[adjacent]))
        return edges

    def add_to_graph(self, start_id: str, dest_id: str = None, weight: float = 0) -> None:
        """
        add the edge to graph
        :param start_id:start point
        :param dest_id:end point
        :param weight:weight
        :return:priority
        """
        if start_id not in self.vertices:
            self.vertices[start_id] = Vertex(start_id)
            self.size += 1

        if dest_id is not None:
            if dest_id not in self.vertices:
                self.vertices[dest_id] = Vertex(dest_id)
                self.size += 1
            self.vertices[start_id].adj[dest_id] = weight

    def matrix2graph(self, matrix: Matrix) -> None:
        """
        change to size
        :param matrix:total length
        :return:size
        """
        for x in range(1, len(matrix)):
            for y in range(1, len(matrix)):
                if matrix[x][0] not in self.vertices:
                    self.vertices[matrix[x][0]] = Vertex(matrix[x][0])
                    self.size += 1

                if matrix[0][y] not in self.vertices:
                    self.vertices[matrix[0][y]] = Vertex(matrix[0][y])
                    self.size += 1
                if matrix[x][y] is not None:
                    self.vertices[matrix[x][0]].adj[matrix[0][y]] = matrix[x][y]

    def graph2matrix(self) -> Matrix:
        """
        calculate the length
        :return:length of matrix
        """
        if self.size == 0:
            return None
        # outputMatrix: Matrix = np.tile(np.arange(self.size + 1), (self.size+1, 1))
        # outputMatrix: Matrix = np.zeros((self.size+1, self.size+1))
        pos = 1
        matrixLength = self.size + 1
        outputMatrix: Matrix = [[None] * matrixLength for i in range(matrixLength)]

        for vertex in self.vertices:
            outputMatrix[0][pos] = vertex
            outputMatrix[pos][0] = vertex
            pos += 1
        pos = 0
        for vertex in self.vertices:
            pos += 1
            for adjacent in self.vertices[vertex].adj:
                idx = outputMatrix[0].index(adjacent)
                outputMatrix[pos][idx] = self.vertices[vertex].adj[adjacent]
        return outputMatrix

    def bfs(self, start_id: str, target_id: str) -> Tuple[List[str], float]:
        """
        visit neighbors
        :param start_id: start point
        :param target_id: end point
        :return:path and distance
        """
        path: List[str] = []
        distance: float = 0
        remaining: queue.SimpleQueue = queue.SimpleQueue()
        remaining.put(start_id)
        parents = {start_id: "INVALID"}
        found = False
        while not remaining.empty():
            curr_id = remaining.get()
            if curr_id not in self.vertices:
                break
            self.vertices[curr_id].visited = True
            if curr_id == target_id:
                found = True
                break

            for adj_id in self.vertices[curr_id].adj:
                if not self.vertices[adj_id].visited:
                    remaining.put(adj_id)
                    if adj_id not in parents:
                        parents[adj_id] = curr_id
        if not found:
            return [], 0
        curr_id = target_id
        while parents[curr_id] != "INVALID":
            path.append(curr_id)
            distance += self.vertices[parents[curr_id]].adj[curr_id]
            curr_id = parents[curr_id]
        path.append(curr_id)
        path.reverse()
        return path, distance

    def dfs(self, start_id: str, target_id: str) -> Tuple[List[str], float]:
        """
        Wrapper function for dfs_inner
        :param start_id: start point
        :param target_id: target point
        :return: inner function
        """

        def dfs_inner(current_id: str, target_id: str, path: List[str] = []) \
                -> Tuple[List[str], float]:
            """
            inner func
            :param current_id:current point
            :param target_id: target point
            :param path:list of path
            :return:path and distances tuple
            """
            search_path = []
            distance_inner = 0
            if current_id == target_id:
                path.append(current_id)
                return path, 0
            self.vertices[current_id].visited = True
            for vertex_id in self.vertices[current_id].adj:
                if not self.vertices[vertex_id].visited:
                    inner_path, inner_distance = dfs_inner(vertex_id, target_id, [*path, current_id])
                    if len(inner_path) > 0 and inner_path[-1] == target_id:
                        return inner_path, inner_distance + self.vertices[current_id].adj[vertex_id]
            return search_path, distance_inner
        if self.size == 0 or start_id not in self.vertices or target_id not in self.vertices:
            return [], 0
        path, distance = dfs_inner(start_id, target_id)
        return path, distance

    def a_star(self, start_id: str, target_id: str, metric: Callable[[Vertex, Vertex], float]) \
            -> Tuple[List[str], float]:
        """
        :param start_id:start point
        :param target_id:target point
        :param metric: the list of vert
        :return:path and distance
        """
        if start_id not in self.vertices or target_id not in self.vertices:
            return [], 0
        parents = {start_id: "INVALID"}
        priority_queue = AStarPriorityQueue()
        path: List[str] = []
        distance: float = 0
        priority_queue.push(0, self.vertices[start_id])
        source_distance = {start_id: 0}
        while not priority_queue.empty():
            x, curr_vertex = priority_queue.pop()
            self.vertices[curr_vertex.id].visited = True
            if curr_vertex.id == target_id:
                found = True
                break
            for adj_id in self.vertices[curr_vertex.id].adj:
                if not self.vertices[adj_id].visited:
                    if adj_id not in source_distance:
                        source_distance[adj_id] = source_distance[curr_vertex.id] + self.vertices[curr_vertex.id].adj[adj_id]
                        priority_queue.push(source_distance[adj_id] + metric(self.vertices[adj_id], self.vertices[target_id]), self.vertices[adj_id])
                        parents[adj_id] = curr_vertex.id
                    else:
                        if source_distance[adj_id] > source_distance[curr_vertex.id] + self.vertices[curr_vertex.id].adj[adj_id]:
                            source_distance[adj_id] = source_distance[curr_vertex.id] + self.vertices[curr_vertex.id].adj[adj_id]
                            priority_queue.update(source_distance[adj_id] + metric(self.vertices[adj_id], self.vertices[target_id]), self.vertices[adj_id])
                            parents[adj_id] = curr_vertex.id
        if not found:
            return [], 0
        curr_id = target_id
        while parents[curr_id] != "INVALID":
            path.append(curr_id)
            distance += self.vertices[parents[curr_id]].adj[curr_id]
            curr_id = parents[curr_id]
        path.append(curr_id)
        path.reverse()
        return path, distance

    def make_equivalence_relation(self) -> int:
        """
        Description.
        :return:
        """
        pass


class AStarPriorityQueue:
    """
    Priority Queue built upon heapq module with support for priority key updates
    Created by Andrew McDonald
    Inspired by https://docs.python.org/3/library/heapq.html
    """

    __slots__ = ['data', 'locator', 'counter']

    def __init__(self) -> None:
        """
        Construct an AStarPriorityQueue object
        """
        self.data = []  # underlying data list of priority queue
        self.locator = {}  # dictionary to locate vertices within priority queue
        self.counter = itertools.count()  # used to break ties in prioritization

    def __repr__(self) -> str:
        """
        Represent AStarPriorityQueue as a string
        :return: string representation of AStarPriorityQueue object
        """
        lst = [f"[{priority}, {vertex}], " if vertex is not None else "" for
               priority, count, vertex in self.data]
        return "".join(lst)[:-1]

    def __str__(self) -> str:
        """
        Represent AStarPriorityQueue as a string
        :return: string representation of AStarPriorityQueue object
        """
        return repr(self)

    def empty(self) -> bool:
        """
        Determine whether priority queue is empty
        :return: True if queue is empty, else false
        """
        return len(self.data) == 0

    def push(self, priority: float, vertex: Vertex) -> None:
        """
        Push a vertex onto the priority queue with a given priority
        :param priority: priority key upon which to order vertex
        :param vertex: Vertex object to be stored in the priority queue
        :return: None
        """
        node = [priority, next(self.counter), vertex]
        self.locator[vertex.id] = node
        heapq.heappush(self.data, node)

    def pop(self) -> Tuple[float, Vertex]:
        """
        Remove and return the (priority, vertex) tuple with lowest priority key
        :return: (priority, vertex) tuple where priority is key,
        and vertex is Vertex object stored in priority queue
        """
        vertex = None
        while vertex is None:
            # keep popping until we have valid entry
            priority, count, vertex = heapq.heappop(self.data)
        del self.locator[vertex.id]  # remove from locator dict
        vertex.visited = True  # indicate that this vertex was visited
        while len(self.data) > 0 and self.data[0][2] is None:
            heapq.heappop(self.data)  # delete trailing Nones
        return priority, vertex

    def update(self, new_priority: float, vertex: Vertex) -> None:
        """
        Update given Vertex object in the priority queue to have new priority
        :param new_priority: new priority on which to order vertex
        :param vertex: Vertex object for which priority is to be updated
        :return: None
        """
        node = self.locator.pop(vertex.id)  # delete from dictionary
        node[-1] = None  # invalidate old node
        self.push(new_priority, vertex)  # push new node