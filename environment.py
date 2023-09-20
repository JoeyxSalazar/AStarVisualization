import random
import shapely.geometry as sg
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from shapely.geometry import Polygon, Point, LineString


class Environment:
    def __init__(self, num_polygons):
        self.width = 800
        self.height = 600
        self.start = (0,0)
        self.goal = (self.width, self.height)
        self.obstacles = self.generate_non_overlapping_polygons(num_polygons)

    def generate_random_polygon(self):
        """Generates a random polygon with 3 to 4 vertices. 
        Returns:
          A Shapely polygon object.
        """ 
        while True:
            n = random.randint(3, 4)  # Random number of vertices (3 to 4)  
            # Create polygon
            x_min = random.uniform(0.01 * self.width, 0.5 * self.width)
            y_min = random.uniform(0.01 * self.height, 0.5 * self.height)
            x_max = random.uniform(x_min, self.width)
            y_max = random.uniform(y_min, self.height)
            num_points = n
            points = []
            for _ in range(n):
                x = random.uniform(x_min, x_max)
                y = random.uniform(y_min, y_max)
                points.append((x, y))   
            # Create the Shapely polygon
            p = Polygon(points)
            if p.is_valid:
                return p

    # Function to generate non-overlapping polygons
    def generate_non_overlapping_polygons(self, num_polygons):
        """Generates a list of non-overlapping polygons.    
        Args:
          num_polygons: The number of polygons to generate. 
        Returns:
          A list of Shapely polygon objects.
        """ 
        polygons = []
        for _ in range(num_polygons):
            attempts = 0
            while True:
                polygon = self.generate_random_polygon()
                if all(not polygon.intersects(existing_polygon) for existing_polygon in polygons):
                    polygons.append(polygon)
                    break
                attempts += 1
                if attempts > 1000:
                    break  # Avoid infinite loop in case of overlapping polygons  
        return polygons
    
    def display_solution(self, coords):
        line_string = sg.LineString(coords)

        # Create a figure and axis
        fig, ax = plt.subplots(figsize=(8, 6))

        # Draw the polygons on the grid
        for polygon in self.obstacles:
            x, y = polygon.exterior.xy
            ax.fill(x, y, alpha=0.7)

        #Draw Solution
        ax.plot(*line_string.xy, linestyle='-', color='blue')


        # Set axis limits and display the grid
        ax.set_xlim(0, self.width)
        ax.set_ylim(0, self.height)
        ax.set_aspect('equal', 'box')
        plt.axis('off')
        # Add text labels for "Start" and "End"
        ax.text(0, 0, "Start", fontsize=12, color='green', verticalalignment='bottom')
        ax.text(800, 600, "End", fontsize=12, color='red', verticalalignment='bottom')
        plt.show()
