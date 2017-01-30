"""Softmax."""
""" lot of knowledge about numpy lib need to lear http://hialex.cn/2014/05/22/(%E8%AF%91)NumPy%E6%95%99%E7%A8%8B(%E4%B8%80)/
http://blog.csdn.net/sunny2038/article/details/9002531"""

scores = [3.0, 1.0, 0.2]

import numpy as np

def softmax(x):
    #"""Compute softmax values for each sets of scores in x."""
    #pass  # TODO: Compute and return softmax(x) 
	return np.exp(x) / np.sum(np.exp(x), axis=0)

print(softmax(scores))

# Plot softmax curves
import matplotlib.pyplot as plt
x = np.arange(-2.0, 6.0, 0.1)
print x
print "\n"
scores = np.vstack([x, np.ones_like(x), 0.2 * np.ones_like(x)])
print scores
print "\n"
print softmax(scores).T

plt.plot(x, softmax(scores).T, linewidth=2)
plt.show()
