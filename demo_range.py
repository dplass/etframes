import etframes
from pylab import *


ys = [1,1.5,2,2.5,5]
xs = range(len(ys))


scatter(xs,ys, color='black', marker='o', s=20)

def minmax(data):
    return min(data), max(data)

etframes.add_range_frame(gca(),
                         xbounds=minmax(xs),
                         ybounds=minmax(ys))

# perhaps don't show the -1 and +1 axis ticks + labels?

plt.gray()
plt.savefig("demo_range.png", dpi=300, transparent=True, orientation='landscape')
# show()




