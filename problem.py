from shapely.geometry import LineString
import heapq
import math

class PriorityQueue:
    def __init__(self):
        self.elements = []

    def push(self, f, vertex):
        heapq.heappush(self.elements, (f, vertex))

    def pop(self):
        return heapq.heappop(self.elements)[1]

    def is_empty(self):
        return len(self.elements) == 0
    
    def is_within(self, vertex):
        if vertex in self.elements:
            return True
        return False

class Problem:
    def __init__(self, env):
        self.polygons = env.obstacles
        self.vertices = []
        self.environment = env
        for pol in self.polygons:
            verts = list(pol.exterior.coords)
            for v in verts:
                self.vertices.append(v)
        self.vertices.append((800,600))

    
    def check_cross(self, start, end):
        line = LineString([start, end])
        for polygon in self.polygons:
            if line.crosses(polygon) == True:
                return True
        return False
        
    #This function returns a list of possible vertices to travel to next
    def successor(self, node):
        children = []
        for v in self.vertices:
            if self.check_cross(node, v) == False: #and self.intersects_edge(node, v) == False:
                children.append(v)
        unique_list = []
        [unique_list.append(item) for item in children if item not in unique_list]

        return unique_list
        pass
    
    def path_cost(self, start, end):
        # Calculate the Euclidean distance between two points
        dx = start[0] - end[0]
        dy = start[1] - end[1]
        return math.sqrt(dx**2 + dy**2)

    
    def reconstruct_path(self, came_from, current):
        path = []
        while current in came_from:
            path.append(current)
            current = came_from[current]
        path.append((0,0))
        path.reverse()
        return path

    def astar(self):
        open_set = PriorityQueue()
        open_set.push(0, self.environment.start)
        came_from = {}
        g_score = {vertex: float('inf') for vertex in self.vertices}
        g_score[self.environment.start] = 0

        while not open_set.is_empty():
            curr_vertex = open_set.pop()

            if curr_vertex == self.environment.goal:
                # Goal reached, reconstruct the path
                path = self.reconstruct_path(came_from, curr_vertex)
                return path

            for neighbor in self.successor(curr_vertex):
                tentative_g_score = g_score[curr_vertex] + self.path_cost(curr_vertex, neighbor)

                if tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = curr_vertex
                    g_score[neighbor] = tentative_g_score
                    f_score = g_score[neighbor] + self.path_cost(neighbor, self.environment.goal)

                    if not open_set.is_within(neighbor):
                        open_set.push(f_score, neighbor)

        # If the loop completes without finding the goal, return None or handle accordingly
        return None


