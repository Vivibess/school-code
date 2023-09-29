import numpy as np
import math

def generate_points(num_of_points):
    points = []
    point = [0, 0]
    for i in range(0, num_of_points):
        point[0] = np.random.uniform(-1,1)
        point[1] = np.random.uniform(-1,1)
        points.append(point.copy())
    return points

def distance_from_0(point):
    distance = math.sqrt((point[0] ** 2 ) + (point[1] ** 2))
    return distance

def number_of_hits(points):
    hits = 0
    for i in range(0, len(points)):
        if distance_from_0(points[i]) <=1:
            hits += 1
    return hits

def montecarlo(num_of_points):
    points = generate_points(num_of_points)
    # pi = 3.1415
    # approximation will become more accurate with bigger num_of_points
    pi_approx = (4 * number_of_hits(points))/num_of_points
    return pi_approx

print(montecarlo(1000000))