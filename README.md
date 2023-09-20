# Requirements
    - Shapely (pip install shapely)
    - Matplotlib

# Build Instructions
    -Simply run main.py and the plot will show the path. The console will also show iterative steps.
    -The polygon plot is random each time

# Design
###     environment.py
        -This class is responsible for setting up the polygons and the plot/graph
        -Environment takes an integer on construction for the amount of desired polygons
        -Only creates valid polygons
        -Display function takes a list of tuples to draw the path taken.
### problem.py
        -Priority Queue is built to pop the tuple correlated with the smallest f-value
            -f = g + h which are defined in Problem Class
        -Problem Class contains astar, successor, and helpers
