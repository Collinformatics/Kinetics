from functions import Functions
import numpy as np
import sys


"""
    Consider a simple reversable reactions, where an enzyme (E) binds to a substrate (S) 
    to from a complex (ES), and then isomerizes into a new state (EX).
    
        E + S ⇌ ES ⇌ EX
    
    
    For the first step, ES formation is time dependant:
    
        ∆[ES] / ∆t = k₁[E][S] - k₋₁[ES]
    
        where k₁ and k₂ are the respective forward and reverse rate constants.
    
"""
"""
    k₂
"""


## ***** Inputs *****

# Input: Initital Concentrations
E = 4 # ConcA (mol/L)
S = 5
ES = 0

# Input: Rate Constants
k1 = 4**-1
k1r = 3**-3 # k₋₁

# Input: Reaction Params
duration = 15 # min
step = 0.05 # min


# ========================================================================================
# Initalize class
fn = Functions(duration=duration, timeStep=step)

# Run reactions
data = fn.complexFormation(
    concE=E, concS=S, concES=ES, rateF=k1, rateR=k1r
)

# Plot data
fn.plotLines(
    data=data, labelX='Time', labelY='Concentration (mol/L)',
    title=f'Reaction Kinetics\nE + S ⇌ ES\nk₁ = {round(k1, 2)}, k₋₁ = {round(k1r, 2)}',
    colors=['black', '#7700AA', '#20BB20']
)
