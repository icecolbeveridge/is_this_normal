# NOTE: This is hacked-together code mainly for my own benefit. Play with it as much as you like, but I make no promises about
# whether it will work or whether I will fix it if it doesn't.

import random
import math
import numpy as np
import matplotlib.pyplot as plt

# remove the {to_remove} lowest-performing workers
def cull( workforce, to_remove = 100 ):
    workforce.sort()
    return workforce[to_remove:]

# pick the {to_hire} best applicants out of {to_pick_from} normally-distributed people
def hire( to_hire = 100, to_pick_from = 1000):
    r = [random.normalvariate(100, 10) for i in range (to_pick_from)]
    r.sort()
    return r[-to_hire:]

def mean(x):
    return sum(x) / len(x)

means = []
workforce = [random.normalvariate(100,10) for i in range(1000)]
for i in range(100):
    workforce = cull(workforce)
    means.append(mean(workforce)) # taking the mean after the cull is much less noisy (and more reasonable)
    new_hires = hire()
    workforce.extend( new_hires )

workforce.sort()

# Plot the CDF
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
y = np.linspace(1, 1/900., 900) # Need the worker labels to go backwards

m, b = np.polyfit(workforce[100:], np.log(y),1) # Fit a line to the curve (on log axes)
poly1d_fn = np.poly1d((m,b))
ax.plot(workforce[100:], np.exp(poly1d_fn(workforce[100:])), '--k') # plot the fit

ax.scatter(x=workforce[100:], y= y ) # plot the employees

ax.plot([workforce[100],workforce[-1]], [1/5., 1/5.]) # plot the horizontal 20% line

p20 = workforce[100] + (workforce[-1] - workforce[100]) * 0.2 
ax.plot([p20, p20], [1/900, 1]) # plot the vertical 80% line

# fix the axes
ax.set_yscale('log') 
plt.xlabel("Performance")
plt.ylabel("Cumulative frequency")
plt.show()

# Then plot the means

plt.plot(means)
plt.xlabel("Time (years)")
plt.ylabel("Performance")

plt.show()
