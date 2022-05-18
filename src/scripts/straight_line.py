import matplotlib.pyplot as plt
import numpy as np
import paths

fig = plt.figure()
plt.plot(np.linspace(1, 10, 10), np.linspace(1, 10, 10))
fig.savefig(paths.figures/"cool_fig.pdf")
