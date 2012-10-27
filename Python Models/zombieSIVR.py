#!/usr/bin/env python

#Python implementation of continuous SIR model with non-R immune class
#From "A Gentle Introduction to Mathematical Modeling: Lessons from the Living Dead
#By Eric Lofgren
#Eric.Lofgren@unc.edu

#Import Necessary Modules
import numpy as np
from pylab import *
import scipy.integrate as spi

#Parameter Values
S0 = 0.99999
I0 = 0.00001
V0 = 0.00
R0 = 0.0

PopIn= (S0, I0, R0, V0)
beta= 0.50      
gamma= 1/10.    
sigma= 0.01
t_end = 100     
t_start = 1
t_step = .02
t_interval = np.arange(t_start, t_end, t_step)

#Solving the differential equation. Solves over t for initial conditions PopIn

def eq_system(PopIn,t):
    '''Defining SIR System of Equations'''
    #Creating an array of equations
    Eqs= np.zeros((4))
    Eqs[0]= -beta*PopIn[0]*PopIn[1] - sigma*PopIn[0]
    Eqs[1]= beta*PopIn[0]*PopIn[1] - gamma*PopIn[1]
    Eqs[2]= gamma*PopIn[1]
    Eqs[3]= sigma*PopIn[0]
    return Eqs

SIVR = spi.odeint(eq_system, PopIn, t_interval)

#Splitting out the curves for S, I and R from each other, in case they need
#to be used seperately
S=(SIVR[:,0])
I=(SIVR[:,1])
R=(SIVR[:,2])
V=(SIVR[:,3])

#Create a new array of the same length to be used as the x-axis for a plot
x=arange(len(SIVR),dtype=float)

#Scale x-axis array by the step size
for i in x:
    x[i]=(x[i]*t_step)

#Stack S, I and R with the x-axis
#Slightly less efficient than just gluing SIR and x together
#Allows for clearer manipulation of individual curves - imo
SIVR_plot= vstack([S,I,R,V,x])

#Graph!
fig= figure()
ax = fig.add_subplot(111)
plot(SIVR_plot[4],SIVR_plot[0],'g--',SIVR_plot[4],SIVR_plot[1],'r-',SIVR_plot[4],SIVR_plot[2],'-.b',SIVR_plot[4],SIVR_plot[3],'m:',linewidth=3) 
xlabel("Time (days)")
ylabel("Percent of Population")
title("Zombie SIR Epidemic with Vaccination")
grid(True)
legend(("Survivors", "Zombies", "Dead", "Vaccinated"), shadow=True, fancybox=True)
show()
