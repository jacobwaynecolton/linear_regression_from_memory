# imports
import random
import numpy
import generate_data

# global variables
EPOCHS = 50
LEARNING_RATE = 0.1 # function for the model to make a prediction
def predict(input, weight,bias):
    prediction = input * weight + bias
    return prediction

# Calculate the error
def calculate_error(prediction,true_label):
    error = true_label - prediction
    return error

# calcuate loss using Mean Squared Error (MSE) loss function
def MSE(data_size, y, y_hat):
    # calculating mean squared error
    L = (1/(2 * data_size)) * numpy.sum([calculate_error(y[i], y_hat[i]) for i in range(data_size))**2
    return L

# update the weight and bias
def update_params():
    a = LEARNING_RATE    
    w = w - a * ((-1/n) * numpy.sum())




# for the main execution
def main():
    # generating the data 
    X, y = generate_data.generate(data_size) 
    y_hat = []

    # setting the weight and the bias to default values
    weight = 0.5
    bias = -40

    # looping over the whole data set
    for epoch in range(EPOCHS):
        # creating the training loop over the whole data set
        for i in range(data_size):
            # the model makes a prediction
            y_hat[i] = predict(X[i], y[i]) 

        # calculate loss
        L = MSE(data_size, y, y_hat)


            


# If we are running the main file
if __name__ == "__main__":
    main()
