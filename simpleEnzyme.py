from functions import Functions
import numpy as np
import sys


"""
    Consider a simple reversable reactions, where an enzyme (E) binds to a substrate (S) 
    to from a complex (ES), and then isomerizes into a new state (EX).
    
        E + S ⇌ ES ⇌ EX
        
    Or modifies the S to produce a product (P):

        E + S ⇌ ES ⇌ E + P
    
    
    For the first step, ES formation is time dependant:
    
        ∆[ES] / ∆t = k₁[E][S] - k₋₁[ES]
    
        where k₁ and k₂ are the respective forward and reverse rate constants.
    
    
    Therefor a timestep t, the new ES concentration ([ES]ₜ) is the sum of the [ES] at
    the previous timestep ([ES]ₜ₋₁) and the change in [ES[
    
        [ES]ₜ = [ES]ₜ₋₁ + ∆[ES] / ∆t


"""
"""
    k₂
"""


## ***** Inputs *****

# Input: Initital Concentrations
E = 4 # [M: mol/L]
S = 5
ES = 0

# Input: Rate Constants
k1 = 4*10**-3 # [M/s]
k1r = 3*10**-4 # k₋₁

# Input: Reaction Params
duration = 200 # s
step = 0.05 # s


# ========================================================================================
# Initalize class
fn = Functions(duration=duration, timestep=step)

# Run reactions
data = fn.complexFormation(
    concE=E, concS=S, concES=ES, rateF=k1, rateR=k1r
)

# Plot data
fn.plotLines(
    data=data, labelX='Time (s)', labelY='Concentration (mol/L)',
    title=f'Reaction Kinetics\nE + S ⇌ ES\nk₁ = {k1:.1e} M/s\nk₋₁ = {k1r:.1e} M/s',
    colors=['black', '#7700AA', '#20BB20']
)
