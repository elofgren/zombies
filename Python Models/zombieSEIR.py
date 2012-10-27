#!/usr/bin/env python

#Python implementation of SEIR model
#From "A Gentle Introduction to Mathematical Modeling: Lessons from the Living Dead
#By Eric Lofgren
#Eric.Lofgren@unc.edu

#Import Necessary Modules
import numpy as np
from pylab import *
import scipy.integrate as spi

#Parameter Values
S0 = 0.99999
E0 = 0.0
I0 = 0.00001
R0 = 0.0
PopIn= (S0,E0, I0, R0)
beta= 0.50        
alpha= 1/2.
gamma=1/10.    
t_end = 100
t_start = 1
t_step = .02
t_interval = np.arange(t_start, t_end, t_step)

#Solving the differential equation. Solves over t for initial conditions PopIn

def eq_system(PopIn,t):
    '''Defining SEIR System of Equations'''
    #Creating an array of equations
    Eqs= np.zeros((4))
    Eqs[0]= -beta * PopIn[0]*PopIn[2]
    Eqs[1]= beta * PopIn[0]*PopIn[2] - alpha*PopIn[1]
    Eqs[2]= alpha*PopIn[1] - gamma*PopIn[2]
    Eqs[3]= gamma*PopIn[2]
    return Eqs

SEIR = spi.odeint(eq_system, PopIn, t_interval)

#Splitting out the curves for S, I and R from each other, in case they need
#to be used seperately
S=(SEIR[:,0])
E=(SEIR[:,1])
I=(SEIR[:,2])
R=(SEIR[:,3])

#Create a new array of the same length to be used as the x-axis for a plot
x=arange(len(SEIR),dtype=float)

#Scale x-axis array by the step size
for i in x:
    x[i]=(x[i]*t_step)

#Stack S, I and R with the x-axis
SEIR_plot= vstack([S,E,I,R,x])

#Graph!
fig= figure()
ax = fig.add_subplot(111)
plot(SEIR_plot[4],SEIR_plot[0],'g--',SEIR_plot[4],SEIR_plot[1],'m:',SEIR_plot[4],SEIR_plot[2],'r-',SEIR_plot[4],SEIR_plot[3],'-.b',linewidth=3) 
xlabel("Time (days)")
ylabel("Percent of Population")
title("Zombie SEIR Epidemic")
grid(True)
legend(("Survivors","Latent", "Zombies", "Dead"), shadow=True, fancybox=True)
show()
