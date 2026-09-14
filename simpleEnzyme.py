from functions import Functions
import numpy as np
import sys


"""
    Consider a simple reversable reactions, where an enzyme (E) binds to a substrate (S) 
    to from a complex (ES), and then isomerizes into a new state (EX).
    
        E + S ⇌ ES ⇌ EX
    
    
    For the first step, ES formation is time dependant:
    
        ∆[ES] / ∆t = k₁[E][S] - k₂[ES]
    
        where k₁ and k₂ are the respective forward and reverse rate constants.
    
    
"""


## ***** Inputs *****

# Input: Initital Concentrations
A = 4 # ConcA (mol/L)
B = 5
C = 0

# Input: Reaction Params
duration = 20 # min
step = 1 # min
time = [t for t in range(0, duration+step, step)]
k = 0.4 # Rate cst (1/s)
vol = 1 # Volume (L)
a = 1
b = 1
c = 1


# ========================================================================================
# Initalize class
fn = Functions()


# Run reactions
concA, concB, concC = fn.firstOrderRxn([A, B, C], times=time, rateCst=k)
print(concC)


fn.plotLines(
    data=(time, concC, 'Product C'), labelX='Time', labelY='y(t)',
    title='Reaction Kinetics', lineSets=[(time, concA, 'Reactant A', '#20BB20', '-', ''),
                                         (time, concB, 'Reactant B', '#7700AA', '-', '')]
)

