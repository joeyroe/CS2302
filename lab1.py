# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 20:20:45 2019

@author: Joey Roe
    80549550
Date: 02/08/2019
CS 2302 Data Structures
Lab1
purpose: demonstrate how to use recursion by plotting points
         form different shapes and patterns
"""

import numpy as np
import matplotlib.pyplot as plt
import math

#number one, plots the squares in the corners
def squares(ax, timesRun, points, w):
    if timesRun > 0:
        
        i1 = [0, 1, 2, 3, 4]
    
        newSq = (points + 350) * w   #gets the square top right corner
        newSq1 = (points - 350) * w  #gets the square in the lower left corner
        """
        new Sq2 got the points for the upper left corner. It required different
        adjustments from both the x-coordinates and the the y-coordinates that had
        to be made only to the x-coordinates without affecting the y-coordinates
        and vice versa
        """
        newSq2 = points
        newSq2[i1, 1] = ((points[i1, 1] + 350) * w) #Make specific adjustments to the y points
        newSq2[i1, 0] = ((points[i1, 0] - 350) * w) #Make speciic adustments to the x points
        newSq3 = newSq2* -1 #gets the points for the lower right corner
        
        ax.plot(points[:, 0], points[:, 1], color = 'b')#This plots the points
        squares(ax, timesRun - 1, newSq, w)
        squares(ax, timesRun - 1, newSq1, w)
        squares(ax, timesRun - 1, newSq2, w)
        squares(ax, timesRun - 1, newSq3, w)
        
        
#number two, plots circles      
def circle(center,rad):
    n = int(4*rad*math.pi)
    t = np.linspace(0,6.3,n)
    x = center[0]+rad*np.sin(t)
    y = center[1]+rad*np.cos(t)
    return x,y
#number 2, plots the circles inside one another towards the left
def draw_circles(ax,n,center,radius,w):
    if n>0:
        x,y = circle(center,radius) #this is what makes the circle
        ax.plot(x,y,color='r') #this plots the circle
        draw_circles(ax, n - 1, center * w , radius * w, w)

#   I multiplied the center by a smaller number to move it over to the left,
#   I made the y point 0, then I multiplied the radius by w to make 
#   it smaller


#number 4, plots the circles in a t like pattern
def draw_circles2(ax,n,center,radius):
    if n>0:

        centerL = [(center[0] -(2 * (radius / 3))), center[1]]
        centerR = [(center[0] + (2 * (radius / 3))), center[1]]
        centerT = [center[0], (center[1] + (2 * (radius / 3)))]
        centerB = [center[0], (center[1] - (2 * (radius / 3)))]
        x,y = circle(center,radius) 
        ax.plot(x,y,color='g') 
        draw_circles2(ax, n - 1, center, radius / 3)
        draw_circles2(ax, n - 1, centerL, radius / 3)
        draw_circles2(ax, n - 1, centerR, radius / 3)
        draw_circles2(ax, n - 1, centerT, radius / 3)
        draw_circles2(ax, n - 1, centerB, radius / 3)
        
#        I had to make circles for the top, bottom, left right. and each
#        circle has a radius about 1/3 the radius of the original, so I 
#        divided the radius by 3 multiplied by two, to get a diameter
#        for one of the little circles, and subtracted or added to either
#        the x or y points

#number 3, plots trees
def trees(ax, n, points, w):
    if n > 0:
        
        i1 = [0, 1, 2]
        #newPointL gives me all of the new points for the let part of the tree
        newpointL = points -800
        newpointL[i1, 0] = newpointL[i1, 0] * w #adjusts the angle of the x coords
        
        #newPointR gives me all the new points for the right part of the tree
        newpointR = points
        newpointR[i1, 0] = ((newpointR[i1, 0] + 800) * w) + 800 #adjusts the x-coord for the right
        newpointR[i1, 1] = newpointR[i1, 1] - 800 #adjusts the y-coords for the right
        ax.plot(points[:, 0], points[:, 1], color = 'c')
        trees(ax, n - 1, newpointL, w)
        trees(ax, n - 1, newpointR, w)
        
#        I split tree up into right and left in order to plot it because
#        the right x-points are positive, whereas the x-points left are
#        negative. I also had to multiply the x-points by 0.5 to change the 
#        slope of the line as it went down

        
plt.close("all")
points = np.array([[200, 200], [-200, 200], [-200, -200], [200, -200], [200, 200]])#list for squares
figSq, axSq = plt.subplots() #figuure for number one
#squares(axSq, 2, points, .5)#figure a
#squares(axSq, 3, points, .5)#figure b
squares(axSq, 4, points, .5)#figure c

axSq.set_aspect(1.0)
axSq.axis('off')


centerCir1 = np.array([100, 0])#center points for the circle in number two
figCir1, axCir1 = plt.subplots()#figure for number two
#draw_circles(axCir1, 10, centerCir1, 100, .60)#figure a
draw_circles(axCir1, 40, centerCir1, 100, .9)#figure b
#draw_circles(axCir1, 90, centerCir1, 100, .95)#figure c

axCir1.set_aspect(1.0)
axCir1.axis('off')


centerCir2 = np.array([0, 0])
figCir2, axCir2 = plt.subplots()
#draw_circles2(axCir2, 3, centerCir2, 150)#figure a
draw_circles2(axCir2, 4, centerCir2, 150)#figure b
#draw_circles2(axCir2, 5, centerCir2, 150)#fiure c

axCir2.set_aspect(1.0)
axCir2.axis('off')


pointsTree = np.array([[0, 0], [800, 800], [1600, 0]])
figTree, axTree = plt.subplots()
trees(axTree, 3, pointsTree, .5)#figure a
#trees(axTree, 4, pointsTree, .5)#figure b
#trees(axTree, 6, pointsTree, .5)#figure c

axTree.set_aspect(1.0)
axTree.axis('off')

plt.show()
figSq.savefig('square.png')
figCir1.savefig('circle1.png')
figCir2.savefig('circle2.png')
figTree.savefig('tree.png')