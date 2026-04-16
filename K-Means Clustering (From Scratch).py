import random
import math

data = [
    [1,2],
    [1.5,1.8],
    [5,8],
    [8,8],
    [1,0.6],
    [9,11]
]

k = 2

centroids = random.sample(data,k)

for iteration in range(5):

    clusters = [[] for _ in range(k)]

    for point in data:

        distances = []

        for c in centroids:
            d = math.sqrt((point[0]-c[0])**2 + (point[1]-c[1])**2)
            distances.append(d)

        min_index = distances.index(min(distances))
        clusters[min_index].append(point)

    new_centroids = []

    for cluster in clusters:
        x_sum = 0
        y_sum = 0

        for point in cluster:
            x_sum += point[0]
            y_sum += point[1]

        new_centroids.append([x_sum/len(cluster),y_sum/len(cluster)])

    centroids = new_centroids

print("Final Centroids:",centroids)
