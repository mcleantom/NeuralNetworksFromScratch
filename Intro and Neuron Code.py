inputs = [1.2, 5.1, 2.1]
weights = [3.1, 2.1, 8.7]
bias = 3

output = sum([i*w for i, w in zip(inputs, weights)]) + bias