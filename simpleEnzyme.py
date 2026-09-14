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
k1 = 5
k1r = 2 # k₋₁

# Input: Reaction Params
duration = 6 # min
step = 1 # min
time = [t for t in range(0, duration+step, step)]
k = 0.4 # Rate cst (1/s)
vol = 1 # Volume (L)



# ========================================================================================
# Initalize class
fn = Functions(duration=duration, timeStep=step)

# Run reactions
data = fn.complexFormation(
    concE=E, concS=S, concES=ES, rateF=k1, rateR=k1r
)
concE = data['E']
concS = data['S']
concES = data['ES']

# Plot data
fn.plotLines(
    data=data, labelX='Time', labelY='Concentration (mol/L)',
    title='Reaction Kinetics', colors=['black', '#20BB20', '#7700AA']
)

