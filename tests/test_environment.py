import pytest
from environment import Environment  

# Test the Environment class

def test_environment_creation():
    # Test creating an instance of the Environment class
    env = Environment(num_polygons=5)
    assert isinstance(env, Environment)

def test_generate_non_overlapping_polygons():
    # Test if non-overlapping polygons are generated
    env = Environment(num_polygons=5)
    polygons = env.obstacles
    for i, polygon in enumerate(polygons):
        for j, other_polygon in enumerate(polygons):
            if i != j:
                assert not polygon.intersects(other_polygon)

# Add more test functions for other methods of the Environment class
# For example, test draw_solution(), display(), etc.
