import numpy as np
import matplotlib.pyplot as plt

# question 4 - pattern recognition class

# Erlang distribution, using shape "k" = 2
def erlang(x):
    return 0.5**2 * x * np.exp(-x/2)

# Some random numbers
xRange = np.arange( 0, 20, .01)

# calling the Erlang distribution on each number in the array
listProb = erlang(xRange)

# normalizing the numbers
listProb = listProb / 100

# not equal to 1, so we need to find the missing number
missingProb = (1 - (np.sum(listProb)))

# adding it to the list
yList = np.append(listProb, [missingProb])

# adding a number to the list so nxList and yList are same length
xList = np.append(xRange, [20])

# randomly choosing numbers to plot
h = np.random.choice(xList, 100,p=yList)

# printing the result
print(h)

# to see the graph
plt.plot(h);





