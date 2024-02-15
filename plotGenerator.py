# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 15:16:14 2024

@author: JGarner
"""

import matplotlib.pyplot as plt
import numpy as np

def generatePlot(x, y, title, fileName, _xlim, _ylim, _color):
    fig = plt.figure(figsize=(5.99, 3.06))
    plt.title(title)
    plt.ylim(0, _ylim)
    plt.xlim(0, _xlim)
    plt.scatter(x, y, s = 2, color = _color)
    plt.grid(True);
    plt.savefig(fileName)
    return
    
def generateMultiPlot():
    return