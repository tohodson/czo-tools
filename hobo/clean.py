#! /usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np

import numpy.random as rand
from matplotlib.widgets import import  RectangleSelector

def onselect(eclick, erelease):
    'eclick and erelease are matplotlib events at press and release'
    print(' startposition : (%f, %f)' % (eclick.xdata, eclick.ydata))
    print(' endposition   : (%f, %f)' % (erelease.xdata, erelease.ydata))
    print(' used button   : ', eclick.button)


def line_picker(line, mouseevent):
    """
    find the points within a certain distance from the mouseclick in
    data coords and attach some extra attributes, pickx and picky
    which are the data points that were picked
    """
    if mouseevent.xdata is None:
        return False, dict()
    xdata = line.get_xdata()
    ydata = line.get_ydata()
    maxd = 0.05
    d = np.sqrt((xdata - mouseevent.xdata)**2. + (ydata - mouseevent.ydata)**2.)

    ind = np.nonzero(np.less_equal(d, maxd))
    if len(ind):
        pickx = np.take(xdata, ind)
        picky = np.take(ydata, ind)
        props = dict(ind=ind, pickx=pickx, picky=picky)
        return True, props
    else:
        return False, dict()

def onpick2(event):
    x = []
    y = []
    print('onpick2 line:', event.pickx, event.picky)
    ax = plt.gca()
    print(ax)
    ax.plot(event.pickx, event.picky, 'o', color='red')
    plt.show()

fig, ax = plt.subplots()
ax.set_title('custom picker for line data')
line, = ax.plot(rand(100), rand(100), 'o', picker=line_picker)
fig.canvas.mpl_connect('pick_event', onpick2)


