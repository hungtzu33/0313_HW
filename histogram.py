#
#Template for Python program
#Name
#
import matplotlib.pyplot as plt
import numpy as np

# 1.input
x =np.random.normal(90,10,100)

# 2.process

# 3.output
plt.title("Histogram")
plt.xlabel("Distribution")
plt.ylabel("Score")
plt.xlim([0.100])
plt.hist(x)
plt.show()