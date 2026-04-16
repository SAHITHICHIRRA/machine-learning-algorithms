# Simple Decision Tree using Gini index

dataset = [
    [2.7,0],
    [1.7,0],
    [3.6,1],
    [4.5,1],
    [3.2,1]
]

def gini(groups, classes):
    total = 0
    for group in groups:
        size = len(group)
        if size == 0:
            continue
        score = 0
        for class_val in classes:
            count = 0
            for row in group:
                if row[-1] == class_val:
                    count += 1
            p = count / size
            score += p * p
        total += (1 - score) * (size)
    return total


def split(index, value, dataset):
    left = []
    right = []
    for row in dataset:
        if row[index] < value:
            left.append(row)
        else:
            right.append(row)
    return left, right


classes = [0,1]
best_gini = 999
best_value = None

for row in dataset:
    groups = split(0,row[0],dataset)
    g = gini(groups,classes)

    if g < best_gini:
        best_gini = g
        best_value = row[0]

print("Best Split Value:",best_value)
print("Best Gini:",best_gini)
