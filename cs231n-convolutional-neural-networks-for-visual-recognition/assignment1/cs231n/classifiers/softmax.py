from builtins import range
import numpy as np
from random import shuffle
from past.builtins import xrange

def softmax_loss_naive(W, X, y, reg):
    """
    Softmax loss function, naive implementation (with loops)

    Inputs have dimension D, there are C classes, and we operate on minibatches
    of N examples.

    Inputs:
    - W: A numpy array of shape (D, C) containing weights.
    - X: A numpy array of shape (N, D) containing a minibatch of data.
    - y: A numpy array of shape (N,) containing training labels; y[i] = c means
      that X[i] has label c, where 0 <= c < C.
    - reg: (float) regularization strength

    Returns a tuple of:
    - loss as single float
    - gradient with respect to weights W; an array of same shape as W
    """
    # Initialize the loss and gradient to zero.
    loss = 0.0
    dW = np.zeros_like(W)

    #############################################################################
    # TODO: Compute the softmax loss and its gradient using explicit loops.     #
    # Store the loss in loss and the gradient in dW. If you are not careful     #
    # here, it is easy to run into numeric instability. Don't forget the        #
    # regularization!                                                           #
    #############################################################################
    # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
    num_train = X.shape[0]
    num_class = W.shape[1]

    for i in range(num_train):
        f = X[i].dot(W)
        f -= f.max()  # Avoiding Numeric problem, potential blowup
        f_exp = np.exp(f)
        prob_dist = f_exp[y[i]] / np.sum(f_exp)
        loss += - np.log(prob_dist)

        for j in range(num_class):
            if y[i] == j:
                dW[:, y[i]] += -(np.sum(f_exp) - f_exp[y[i]]) / np.sum(f_exp) * X[i]
            dW[:, j] += X[i] * f_exp[j] / np.sum(f_exp)
    loss /= num_train
    loss += reg * np.sum(W * W)
    dW = dW / num_train
    dW += 2 * reg * W

    pass
    # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

    return loss, dW


def softmax_loss_vectorized(W, X, y, reg):
    """
    Softmax loss function, vectorized version.

    Inputs and outputs are the same as softmax_loss_naive.
    """
    # Initialize the loss and gradient to zero.
    loss = 0.0
    dW = np.zeros_like(W)

    #############################################################################
    # TODO: Compute the softmax loss and its gradient using no explicit loops.  #
    # Store the loss in loss and the gradient in dW. If you are not careful     #
    # here, it is easy to run into numeric instability. Don't forget the        #
    # regularization!                                                           #
    #############################################################################
    # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

    # forward calculation
    num_train = X.shape[0]
    f = X.dot(W)
    f -= f.max()  # Avoiding Numeric problem, potential blowup
    f_exp = np.exp(f)

    numerator = np.exp(f[range(num_train), y])
    denominator = np.sum(f_exp, axis=1)
    # loss calculation
    loss = np.sum(-np.log(numerator / denominator))
    loss = loss / num_train
    loss += reg * np.sum(W * W)

    # backward calculation
    mask = f_exp / np.sum(f_exp, axis=1).reshape(num_train, 1)
    mask[range(num_train), y] = - (denominator - numerator) / denominator

    dW = X.T.dot(mask)
    dW /= num_train
    dW += 2 * reg * W

    pass
    # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

    return loss, dW
