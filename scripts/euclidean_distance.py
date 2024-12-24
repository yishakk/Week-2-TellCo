import numpy as np

def calculate_euclidean_distance(row, cluster_center):
    return np.sqrt(np.sum((row - cluster_center) ** 2))