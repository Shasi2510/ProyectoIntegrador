import random

def generate_random_coordinates(num_points, min_lat, max_lat, min_lon, max_lon):
    coordinates = []
    for _ in range(num_points):
        lat = random.uniform(min_lat, max_lat)
        lon = random.uniform(min_lon, max_lon)
        coordinates.append((lat, lon))
    return coordinates

num_points = 10
min_lat, max_lat = -90, 90
min_lon, max_lon = -180, 180

random_coordinates = generate_random_coordinates(num_points, min_lat, max_lat, min_lon, max_lon)
print(random_coordinates)
