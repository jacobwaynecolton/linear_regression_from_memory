# imports
import random
import numpy
import generate_data

# global variables
EPOCHS = 5000
LEARNING_RATE = 0.1
DATA_SIZE = 2000

def predict(input, weight,bias):
    prediction = input * weight + bias
    return prediction

# Calculate the error
def calculate_error(prediction,true_label):
    error = true_label - prediction
    return error

# calcuate loss using Mean Squared Error (MSE) loss function
def MSE(y, y_hat):
    # calculating mean squared error
    L = (1/(2 * DATA_SIZE)) * numpy.sum([calculate_error(y[i], y_hat[i])**2 for i in range(DATA_SIZE)])
    return L

# update the weight and bias
def update_params(x,y,w,b):
    a = LEARNING_RATE    
    dw = ((-1/DATA_SIZE) * numpy.sum([x[i]*(y[i] - (w*x[i] +b)) for i in range(DATA_SIZE)]))
    db = ((-1/DATA_SIZE) * numpy.sum([(y[i] - (w * x[i] + b)) for i in range(DATA_SIZE)] ))

    w = w - a * dw
    b = b - a * db
    return w,b


# for the main execution
def main():
    # generating the data 
    X, y = generate_data.generate(DATA_SIZE)
    # Converting to numpy arrays so i can normalize the data
    X, y = numpy.array(X), numpy.array(y)
    # normalizing the data
    X = (X - X.mean()) / X.std()
    y = (y - y.mean()) / y.std()
    y_hat = []

    # setting the weight and the bias to default values
    weight = 0.5
    bias = -40

    # making predictions before training
    for i in range(20):
        print(f"Prediction : {predict(X[i],weight,bias)}, Answer = {y[i]}")

    # looping over the whole data set
    for epoch in range(EPOCHS):
        # creating the training loop over the whole data set
        y_hat = []
        for i in range(DATA_SIZE):
            # the model makes a prediction
            y_hat.append(predict(X[i],weight,  bias))

        # calculate loss
        L = MSE(y, y_hat)
        
        print(weight,bias)
        # update the parameters
        weight,bias = update_params(X,y,weight,bias)
        print(weight,bias)

    # making predictions after model training
    for i in range(20):
        print(f"Prediction post-training : {predict(X[i],weight,bias)}, Answer = {y[i]}")
    


            


# If we are running the main file
if __name__ == "__main__":
    main()
