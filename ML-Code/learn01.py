#-*- coding:utf-8 -*-
import numpy as np          #numpy的常用函数
from scipy._lib.six import xrange
from sklearn import datasets          #使用datasets创建随机数据集
from sklearn.linear_model import LogisticRegressionCV          #Logistics函数
import matplotlib.pyplot as plt


# Generate a dataset and plot it
np.random.seed(0)
X, y = datasets.make_moons(200, noise=0.20)
#plt.scatter(X[:,0], X[:,1], s=40, c=y, cmap=plt.cm.Spectral)
# plt.show()

def plot_decision_boundary(pred_func):
#设定最大最小值，附加一点点边缘填充
    x_min,x_max=X[:,0].min()-.5,X[:,0].max()+.5
    y_min,y_max=X[:,1].min()-.5,X[:,1].max()+.5
    h=0.01
    xx,yy = np.meshgrid(np.arange(x_min,x_max,h),np.arange(y_min,y_max,h))
    #用预测函数预测一下
    Z = pred_func( np.c_[xx.ravel(),yy.ravel()])
    Z = Z.reshape(xx.shape)
    #然后画出图
    plt.contourf(xx,yy,Z,cmap=plt.cm.Spectral)
    plt.scatter(X[:,0],X[:,1],c=y, cmap = plt.cm.Spectral)

def Logistic(X,y):
    # Train the logistic rgeression classifier
    clf = LogisticRegressionCV()
    clf.fit(X, y)
    # Plot the decision boundary
    plot_decision_boundary(lambda x: clf.predict(x))
    plt.title("Logistic Regression")
    plt.show()

num_examples = len(X)  # training set size
nn_input_dim = 2  # input layer dimensionality
nn_output_dim = 2  # output layer dimensionality
# Gradient descent parameters (I picked these by hand)
epsilon = 0.01  # learning rate for gradient descent
reg_lambda = 0.01  # regularization strength#正则化强度

def softmax(Z):
    #softmax
    exp_scores = np.exp(Z)
    return exp_scores / np.sum(exp_scores, axis=1, keepdims=True)

def calculate_loss(model):
    #model是一个字典
    W1, b1, W2, b2 = model['W1'], model['b1'], model['W2'], model['b2']
    # Forward propagation to calculate our predictions
    z1 = X.dot(W1) + b1
    a1 = np.tanh(z1)
    z2 = a1.dot(W2) + b2
    probs = softmax(z2)
    # Calculating the loss
    #corect_logprobs = -np.log(probs[range(num_examples), y])
    corect_logprobs = -np.log(probs[range(num_examples),1])*y#检测差别
    data_loss = np.sum(corect_logprobs)
    # Add regulatization term to loss (optional)
    data_loss += reg_lambda/2 * (np.sum(np.square(W1)) + np.sum(np.square(W2)))
    return 1./num_examples * data_loss
# Helper function to predict an output (0 or 1)
def predict(model,x):
    W1, b1, W2, b2 = model['W1'], model['b1'], model['W2'], model['b2']
    # Forward propagation
    z1 = x.dot(W1) + b1
    a1 = np.tanh(z1)
    z2 = a1.dot(W2) + b2
    probs = softmax(z2)
    return np.argmax(probs, axis=1)

def build_model(nn_hdim, num_passes=20000, print_loss=False):
    # Initialize the parameters to random values. We need to learn these.
    np.random.seed(0)
    W1 = np.random.randn(nn_input_dim, nn_hdim) / np.sqrt(nn_input_dim)
    b1 = np.zeros((1, nn_hdim))
    W2 = np.random.randn(nn_hdim, nn_output_dim) / np.sqrt(nn_hdim)
    b2 = np.zeros((1, nn_output_dim))
    # This is what we return at the end
    model = {}
    # Gradient descent. For each batch...
    for i in xrange(0, num_passes):
        # Forward propagation
        z1 = X.dot(W1) + b1
        a1 = np.tanh(z1)
        z2 = a1.dot(W2) + b2
        exp_scores = np.exp(z2)
        probs = exp_scores / np.sum(exp_scores, axis=1, keepdims=True)
        # Backpropagation
        delta3 = probs
        delta3[range(num_examples), y] -= 1
        dW2 = (a1.T).dot(delta3)
        db2 = np.sum(delta3, axis=0, keepdims=True)
        delta2 = delta3.dot(W2.T) * (1 - np.power(a1, 2))
        dW1 = np.dot(X.T, delta2)
        db1 = np.sum(delta2, axis=0)
        # Add regularization terms (b1 and b2 don't have regularization terms)
        dW2 += reg_lambda * W2
        dW1 += reg_lambda * W1
        # Gradient descent parameter update
        W1 += -epsilon * dW1
        b1 += -epsilon * db1
        W2 += -epsilon * dW2
        b2 += -epsilon * db2
        # Assign new parameters to the model
        model = {
            'W1': W1,
            'b1': b1,
            'W2': W2,
            'b2': b2
        }
        # Optionally print the loss.
        # This is expensive because it uses the whole dataset, so we don't want to do it too often.
        if print_loss and i % 1000 == 0:
            print("Loss after iteration %i: %f" ,(i, calculate_loss(model)))
    return model


if __name__=="__main__":
    print("ss")
    # Build a model with a 3-dimensional hidden layer
    model = build_model(5, print_loss=True)
    # Plot the decision boundary
    plot_decision_boundary(lambda x: predict(model, x))
    plt.title("Decision Boundary for hidden layer size 3")
    plt.show()
