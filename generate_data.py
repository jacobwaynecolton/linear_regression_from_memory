# imports
import random

# function to generate inputs and labels
def generate(size):
    X = []
    y = []
   for i in range(size) 
        # appending a random int between 0 and 200 to X
        X.append(random.randint(0,200))
        # appending a random int between 0 and 10 to y
        y.append(random.randint(0,10))

# returning the inputs and corresponding labels as a list
    return X,y
