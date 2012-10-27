#!/usr/bin/env python

#Python implementation of SIR model
#From "A Gentle Introduction to Mathematical Modeling: Lessons from the Living Dead
#By Eric Lofgren
#Eric.Lofgren@unc.edu

import numpy as np
from pylab import *
import scipy.integrate as spi

#Parameter Values
S0 = 0.99999
I0 = 0.00001
R0 = 0.0
PopIn= (S0, I0, R0)
beta= 0.50      
gamma=1/10.  
t_end = 100     
t_start = 1
t_step = .02
t_interval = np.arange(t_start, t_end, t_step)

#Solving the differential equation. Solves over t for initial conditions PopIn

def eq_system(PopIn,t):
    '''Defining SIR System of Equations'''
    #Creating an array of equations
    Eqs= np.zeros((3))
    Eqs[0]= -beta * PopIn[0]*PopIn[1]
    Eqs[1]= beta * PopIn[0]*PopIn[1] - gamma*PopIn[1]
    Eqs[2]= gamma*PopIn[1]
    return Eqs

SIR = spi.odeint(eq_system, PopIn, t_interval)

#Splitting out the curves for S, I and R from each other, in case they need
#to be used seperately
S=(SIR[:,0])
I=(SIR[:,1])
R=(SIR[:,2])

#Create a new array of the same length to be used as the x-axis for a plot
x=arange(len(SIR),dtype=float)

#Scale x-axis array by the step size
for i in x:
    x[i]=(x[i]*t_step)

#Stack S, I and R with the x-axis
SIR_plot= vstack([S,I,R,x])

#Graph!
fig= figure()
ax = fig.add_subplot(111)
plot(SIR_plot[3],SIR_plot[0],'g--',SIR_plot[3],SIR_plot[1],'r-',SIR_plot[3],SIR_plot[2],'-.b',linewidth=3) 
xlabel("Time (days)")
ylabel("Percent of Population")
title("Zombie SIR Epidemic")
grid(True)
legend(("Survivors", "Zombies", "Dead"), shadow=True, fancybox=True)
show()
