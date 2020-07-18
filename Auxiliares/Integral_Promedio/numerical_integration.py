def Tcf(f,a,b,n): #Tcf: composite trapezoidal method for f
    """
    Compute numerical approximation using trapezoidal method in 
    an interval.
    Nodes are generated via formula: x_i = a+ih_hat for i=0,1,...,n and h_hat=(b-a)/n
    Args:
        f (function): function expression of integrand
        a (float): left point of interval
        b (float): right point of interval
        n (float): number of subintervals
    Returns:
        sum_res (float): numerical approximation to integral of f in the interval a,b
    """
    h_hat = (b-a)/n
    sum_aux = 0
    i = 0
    for i in range(0,n-1):
        x = a + i*h_hat
        sum_aux += f(x)
    sum_res = (h_hat/2)*(f(a) + f(b) + 2*sum_aux)
    return sum_res

def Rf(f,a,b):
    node=(a+b)/2 #middle point
    h=b-a
    return h*f(node) #polynomial of zero degree

def Rcf(f,a,b,n): #Rcf: composite rectangle method
    """
    Compute numerical approximation using rectangle or mid-point method in 
    an interval.
    Nodes are generated via formula: x_i = a+(i+1/2)h_hat for i=0,1,...,n-1 and h_hat=(b-a)/n
    Args:
        f (function): function expression of integrand
        a (float): left point of interval
        b (float): right point of interval
        n (float): number of subintervals
    Returns:
        sum_res (float): numerical approximation to integral of f in the interval a,b
    """
    h_hat=(b-a)/n
    sum_res = 0
    for i in np.arange(n):
        x = a + (i+1/2)*h_hat
        sum_res+= f(x)
    return h_hat*sum_res 