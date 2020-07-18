import numpy as np

def MSE(y, y_hat):
    """
    Compute mean squared error.
    See: https://en.wikipedia.org/wiki/Mean_squared_error
    Args:
        y (numpy 1d array of floats): actual values of data.
        y_hat (numpy 1d array of floats): estimated values via model.
    Returns:
        ecm (float): mean squared error result.
    """
    
    v_size=y.size
    ecm=(1/v_size)*np.sum(np.power((y-y_hat),2))
                      
    return ecm

def MSE_mod(y, y_hat):
    """
    Compute mean squared error.
    See: https://en.wikipedia.org/wiki/Mean_squared_error
    Args:
        y (numpy 1d array of floats): actual values of data.
        y_hat (numpy 1d array of floats): estimated values via model.
    Returns:
        ecm (float): mean squared error result.
    """
    
    v_size=y.size
    ecm=(1/v_size)*np.sum(np.power((y-y_hat),2))
                      
    return ecm