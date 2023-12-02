My very own neural network made in Python.

A upto 5 hidden layer based neutral network capability. Using 4 layers as ReLU and 1 (last weight) as Sigmoid activation function. The Neural network allows to build both a training based model as well as a one based on Neuro-Evolution as well as save the model with pickle/ load the saved model.

However,the neural network is not optimised, not using np arrays and multiple optimisations but rather dealing with the weight and biases in more traditional way i.e loops and if statements which definately hurt the network in training against complex problems.

The network has variable 5 layers which you can initialise at your will. There is a input/ output layer which takes in an array and outputs an array. The weights are itself connected without strict layer implementation so each previous layer is connected to all it's next layers. This both makes the network better at finding solution but makes the training period longer.


A sample video of the network training a xor gate

https://github.com/NubSh0t/Python-projects/assets/113845503/891fef5b-61b6-490e-8e25-9ea3ce4a84e4

