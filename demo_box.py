import etframes
from pylab import *
import matplotlib.mlab


ys = [1,1.5,2,2,3,3,6,24,24,2.5,5,6,9,12,13,15,1,7,9,22,5,5,6,8,19,22,22,3,7,9,10,10,11,14]
xs = [1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,3,3,3,3,4,4,4,4,4,4,4,5,5,5,5,5,5,5]
print len(ys), len(xs)

# scatter(xs,ys, c='black', marker='o', s=20, alpha=0.4, edgecolors='none')

def minmax(data):
    return min(data), max(data)

def boxpoints(d, outlier_distance=1.5):
	# implementation pretty much the same as matplotlib axes.boxplot

    # get median and quartiles
    q1, med, q3 = mlab.prctile(d,[25,50,75])
  	# min(data), max(data)

    iq = q3 - q1
    hi_val = q3 + outlier_distance*iq
    lo_val = q1 - outlier_distance*iq
 
    print iq, q1, q3, '---', hi_val, lo_val
    # print (d > hi_val)
    # print (d < lo_val)
    outliers = r_[d[d>hi_val], d[d<lo_val]]
    # print 'outliers', outliers
    inliers = list(set(data)-set(outliers))
    # print 'inliers', inliers
    min_without_outliers = min(inliers)
    max_without_outliers = max(inliers)

    return outliers, min_without_outliers, q1, med, q3, max_without_outliers

unique_xs = list(set(xs))
for xi in unique_xs:
	data = np.asarray(ys)[np.asarray(xs)==xi]
	print '===', xi, data
	o, mini, q1, med, q3, maxi = boxpoints(data)
	print 'outliers', len(o), '-', o
	print 'min, max', mini, maxi
	print 'quartiles', q1, med, q3
	if len(o) > 0:
		scatter([xi]*len(o), o, c='k',marker='x', alpha=0.5)
		# TODO test if multiple on the same spot, then shove over sideways?
	scatter([xi],[med], c='k')
	plot([xi,xi],[maxi,q3], c='k')
	plot([xi,xi],[q1,mini], c='k')

etframes.add_range_frame(gca(),
                         xbounds=minmax(xs),
                         ybounds=minmax(ys))

# TODO don't show the -1d and +1d axis ticks + labels?

plt.gray()
plt.savefig("demo_box.png", dpi=300, transparent=True, orientation='landscape')
# show()




