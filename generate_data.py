import random

# generating the data
def generate(size):
    X = []
    y = []
    for i in range(size):
        x = random.randint(0, 200)
        noise = random.uniform(-2, 2)   # small randomness
        label = 0.5 * x + 3 + noise

        X.append(x)
        y.append(label)

    return X, y
