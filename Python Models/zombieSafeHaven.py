#!/usr/bin/env python

#Python implementation of "Safe Haven" model
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
H0 = 0.0
E0 = 0.0
K0 = 0.0
R0 = 0.0
PopIn = (S0, E0, I0, H0, K0, R0)
beta_F = 0.50
beta_H = beta_F/2
alpha = 1/2.
kappa = 0.00
lamda = 1/14. #needs to be mispelled, lambda is a Python-specific function
gamma =1/10.    
t_end = 200       
t_start = 1
t_step = .02
t_interval = np.arange(t_start, t_end, t_step)

#Solving the differential equation. Solves over t for initial conditions PopIn

def eq_system(PopIn,t):
    '''Defining SIR System of Equations'''
    #Creating an array of equations
    Eqs= np.zeros((6))
    Eqs[0] = -beta_F*PopIn[0]*PopIn[2] - lamda*PopIn[0]
    Eqs[1] = beta_F*PopIn[0]*PopIn[2] + beta_H*PopIn[3]*PopIn[2] - alpha*PopIn[1]
    Eqs[2] = alpha*PopIn[1] - gamma*PopIn[2] - kappa*PopIn[2]*PopIn[3]
    Eqs[3] = lamda*PopIn[0] - beta_H*PopIn[3]*PopIn[2]
    Eqs[4] = kappa*PopIn[2]*PopIn[3]
    Eqs[5] = gamma*PopIn[2]
    return Eqs

SIR = spi.odeint(eq_system, PopIn, t_interval)

#Splitting out the curves for S, I and R from each other, in case they need
#to be used seperately
S=(SIR[:,0])
E=(SIR[:,1])
I=(SIR[:,2])
H=(SIR[:,3])
K=(SIR[:,4])
R=(SIR[:,5])

#Create a new array of the same length to be used as the x-axis for a plot
x=arange(len(SIR),dtype=float)

#Scale x-axis array by the step size
for i in x:
    x[i]=(x[i]*t_step)

#Stack S, I and R with the x-axis
SIR_plot= vstack([S,E,I,H,K,R,x])

#Graph!
fig= figure()
ax = fig.add_subplot(211)
plot(SIR_plot[6],SIR_plot[0],'g--',SIR_plot[6],SIR_plot[1],'m:',SIR_plot[6],SIR_plot[2],'r-',SIR_plot[6],SIR_plot[3],'-.b',linewidth=3) 
xlabel("Time (days)")
ylabel("Percent of Population")
title("Safe Haven Results - Low Kappa")
grid(True)
legend(("Wandering Survivors", "Latent", "Infected", "Safe Survivors"), shadow=True, fancybox=True)

ax = fig.add_subplot(212)
plot(SIR_plot[6],SIR_plot[4],'k--',SIR_plot[6],SIR_plot[5],linewidth=3) 
xlabel("Time (days)")
ylabel("Percent of Population")
grid(True)
legend(("Culled", "Dead"), shadow=True, fancybox=True)

show()
