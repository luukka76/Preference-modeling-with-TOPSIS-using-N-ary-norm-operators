from numpy import ones
from numpy import zeros
from numpy import array
from numpy import diagonal
from random import random as rand
from sklearn.preprocessing import MinMaxScaler


scaler = MinMaxScaler()

# Recursivetnorm/tconormstandardn function
def recursivetnorm(A, w):
    A = array(A)
    [n] = A.shape
    inorm = i_yager(A[0], A[1], w)

    for i in range(0, n):
        inorm = i_yager(A[i], inorm, w)

    return inorm


# function mu=i_bd(a,b,w) or i_yager(a, b, w)
def i_yager(a, b, w):
    mu = (1 - min([1, ((1 - a) ** w + (1 - b) ** w) ** (1 / w)]))
    return mu


# function d=distM(x,y,p)
# [m,n]=size(x);
# d=1/n*(sum(abs(x-y ).^p).^(1/p));

def distM(x, y, p):
    # Cast x into a numpy array
    x = array(x)
    [n] = x.shape

    d = []
    for i in range(0, p):
        # Looping through the list to achieve element wise power and division operations
        d.append(1/n * (sum(abs(x-y )**p) ** (1/p)))

    # Cast d into a numpy array
    d = array(d)
    return d


# function [c,Dplus,Dminus]=topsis(data,p,w,w2,crit,we)

def narytopsis(data, p, w, w2, crit, we = 1):
    Dplus = []
    Dminus = []
    x = array(data)

    [m, n] = x.shape
    nargin = 5 # Initialized to 5 because 5 arguments are passed when this function is called

    if nargin < 6:
        we = ones((1, n))
    elif nargin < 5:
        crit = ones((1, n))

    # Normalization to unit interval
    # a = normalize(x, 'range')
    scaler.fit(x)
    a = scaler.transform(x)

    # weigted normalized decision matrix
    # Multiplying every element of array a with weight we
    r = a * we

    # Positive and negative ideal solutions
    PIS = zeros(n)
    NIS = zeros(n)

    # Convert numpy arrays to python lists to achieve mutability
    PIS = list(PIS)
    NIS = list(NIS)

    crit = list(crit)

    for j in range(0, n):
        if crit[j] == 1:
            PIS[j] = recursivetconorm(r[:, j].transpose(), w)
            NIS[j] = recursivetnorm(r[:, j], w2)
        else:
            NIS[j] = recursivetconorm(r[:, j].transpose(), w)
            PIS[j] = recursivetnorm(r[:, j], w2)

    # Distances to PIS and NIS
    DPISB = zeros(m)
    DNISB = zeros(m)
    print("PIS = ", PIS)
    print("NIS = ", NIS)
    for i in range(0, m):
        Dplus.append(distM(PIS, r[i,:], p))
        Dminus.append(distM(NIS, r[i,:], p))

    #Closeness coefficient:
    c=zeros(m)
    # Convert numpy array into python list to achieve mutability
    c = list(c)

    for i in range (0, m):
        # Reassign values to elements of c
        sumOfPlusMinus = (Dplus[i] + Dminus[i])
        c[i] = Dminus[i]/sumOfPlusMinus

    # Converting python lists back to numpy array
    c = array(c)
    Dplus = array(Dplus)
    Dminus = array(Dminus)

    return [c,Dplus,Dminus]


# function data_v=normalization2(data)
def normalization2(data):
    data_v= array(data)

    # Scaling data between [0,1]
    [m, n] = data_v.shape
    mins_v = min(data_v)
    Ones = ones(m, n)
    data_v = data_v + Ones * diagonal(abs(mins_v))
    maxs_v = max(data_v)

    # Converting a numpy array into python to achieve mutability
    data_v = list(data_v)
    for item in data_v:
        item = item * diagonal(maxs_v^(-1))

    data_v = array(data_v)

    return data_v

# function unorm=tconormstandardn(A,w)
# [n,m]=size(A);
# unorm=u_yager(A(1),A(2),w);
# for i=2:n
#     unorm=u_yager(A(i),unorm,w);
# end


# TODO Continue from Here
def recursivetconorm(A, w):
    A = array(A)
    [n] = A.shape
    unorm = u_yager(A[0], A[1], w)

    return unorm


# function mu=u_Yager(a,b,w)
#
# mu=min([1,(a^w+b^w)^(1/w)]);

def u_yager(a, b, w):
    mu = min([1, (a**w + b**w) ** (1/w)])
    return mu


# function [c,Dplus,Dminus,PIS,NIS,a]=topsis(data,p,w)

def topsisdistpnary(data, p, w):
    # Lists to store content of Dminus and Dplus
    Dminus = []
    Dplus = []
    x = array(data)
    [m, n] = x.shape()

    # Normalization:
    a = normalization2(x)

    # Positive and negative ideal solutions:
    PIS=zeros(n)
    NIS=zeros(n)

    # Converting a numpy array into python to achieve mutability
    PIS = list(PIS[0])
    NIS = list(NIS[0])

    w2 = 2

    for j in range(0, n):
        PIS[j] = recursivetconorm(a[:, j].transpose(), w)
        NIS[j] = recursivetnorm(a[:, j], w2)

    # Converting python lists back to numpy arrays
    PIS = array(PIS)
    NIS = array(NIS)

    # Distances to PIS and NIS
    DPISB = zeros(m)
    DNISB = zeros(m)

    for i in range(0, m):
        # Add elements to Dplus and Dminus
        Dplus.append(distM(PIS, a[i, :], p))
        Dminus.append(distM(NIS, a[i, :], p))

    # Closeness coefficient
    c = zeros(m)
    # Converting a numpy array into python to achieve mutability
    c = list(c)

    for i in range(0, m):
        c[i] = Dminus(i)/(Dplus(i)+Dminus(i))

    # Converting python list back to numpy array
    c = array(c)
    Dplus = array(Dplus)
    Dminus = array(Dminus)

    return [c,Dplus,Dminus,PIS,NIS,a]





# Main Function
def main():
    # Mainfiles purpose is to show how to use n - ary TOPSIS method
    # that uses n - ary norm operators to set preference for either positive
    # ideal solution or negative ideal solution depending on practical
    # problem.It was published in
    # P.Luukka, N—ary norm operators and TOPSIS, 2020 IEEE International
    # Conference on Fuzzy Systems (FUZZ-IEEE), Glasgow, UK, 2020, pp. 1-6,
    # doi: 10.1109/FUZZ48607.2020.9177580.
    # First lets create artificial data of ten alternatives and five criteria:

    # data=c*randn(10,5) python code
    c=10

    data = []
    data_row = []
    for row in range(0, 10):
        for column in range(0, 5):
            data_row.append(rand() * c)
        data.append(data_row)
        data_row= []



    # Define parameters p for Minkowski metric (1=Manhattan distance,2=Euclidean distance etc)
    # and parameter values for fuzzy union (w) and intersection (w2) operators
    p = 1
    w = 2
    w2 = 5

    # See more information about these from the proceedings.
    # Define whether criteria is benefit criteria or cost criteria in crit
    # vector 1=benefit, 2=cost.
    crit = array([1, 1, 1, 2, 1]) # in this example fourth would be cost criteria and others benefit

    [cc, PISB, NISB] = narytopsis(data,p,w,w2,crit)

    # For output of the function you get:
    # cc = closeness coefficient values for ten alternatives
    # PISB = distance to positive ideal solution
    # NISB = distance to negative ideal solution
    # You can get the ordering of the alternatives by sorting CC to descending order

    # TODO Sort cc in descending order
    I = cc.transpose()

    # Order of the attributes:
    Order = I.argsort()
    Order = list(Order[0])[::-1] # Reversing order

    # Display content of variables PISB, NISB, cc, and Order
    print("\nPISB = ", PISB)
    print("\nNISB = ", NISB)
    print("\nCC = ", cc)
    print("\nOrder = ", Order)


if __name__ == '__main__':
    main()
