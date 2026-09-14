from functions import Functions
import math
import numpy as np
import sys

"""
    Reaction rates: the speed of a rxn

    Average rate:
        ∆molB = molB at time_f - molB at time_i

    * For: A -> B
        avg rate = - ∆molA / ∆t


    Irreversible reaction:
        aA + bB -> cC

        rate = (-∆[A] / ∆t) = (-∆[B] / ∆t) = (∆[C] / ∆t)

        rate = k[A][B]

    * k: rate constant


    Reaction order:
        rate = k * [A]^m * [B]^n

    * m, n: reaction orders


    First-Order Reactions:
        rate = -∆[A] / ∆t = - k[A]

        -kt = ln([A]_t / [A]_0) = ln([A]_t) - ln([A]_0)
        
        [A]_t = e^(ln([A]_0) + -kt)


    Second-Order Reactions:
        rate = k[A]^2

        (1 / [A]_t) = kt + (1 / [A]_0)

        -kt = ln([A]_t / [A]_0) = ln([A]_t) - ln([A]_0)

    * Half life:
        halflife = t_1/2 = 1 / k[A]_0
"""

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
ode = ODE()


def firstOrderRxn(conc, times, rateCst, numProd=1):
    l = len(conc)
    data = []
    for i, c in enumerate(conc):
        conc_0 = conc[i]
        x = []
        sign = -1
        if i >= l-numProd:
            concA_0 = conc[0]
            for t in times:
                conc_t = concA_0 * (1 - math.exp(-rateCst*t))
                x.append(conc_t)
        else:
            for t in times:
                conc_t = math.exp(np.log(conc_0) + (-rateCst*t))
                x.append(conc_t)
        data.append(x)
    return data


# Run reactions
concA, concB, concC = firstOrderRxn([A, B, C], times=time, rateCst=k)
print(concC)


ode.plotLines(
    data=(time, concC, 'Product C'), labelX='Time', labelY='y(t)',
    title='Reaction Kinetics', lineSets=[(time, concA, 'Reactant A', '#20BB20', '-', ''),
                                         (time, concB, 'Reactant B', '#7700AA', '-', '')]
)
