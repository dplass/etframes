import etframes
from pylab import *


ys = [1,1.5,2,3,6,7,2.5,5,6,9,12,13,15,1,7,9,22,5,5,6,8,19,22,22,3,7,9,10,10,11,14]
xs = [1,1,1,1,1,1,2,2,2,2,2,2,2,3,3,3,3,4,4,4,4,4,4,4,5,5,5,5,5,5,5]

scatter(xs,ys, c='black', marker='o', s=20, alpha=0.4, edgecolors='none')

def minmax(data):
    return min(data), max(data)

etframes.add_range_frame(gca(),
                         xbounds=minmax(xs),
                         ybounds=minmax(ys))

# TODO don't show the -1d and +1d axis ticks + labels?

plt.gray()
plt.savefig("demo_scatter_transparent.png", dpi=300, transparent=True, orientation='landscape')
# show()




