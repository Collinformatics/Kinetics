import os
import math
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sys


# Set options
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)
pd.set_option('display.float_format', '{:,.3f}'.format)


def pressKey(event):
    if event.key == 'escape':
        plt.close()
    elif event.key == 'e':
        sys.exit()
    elif event.key == 'r':
        python = sys.executable
        os.execl(python, python, *sys.argv)


class Functions:
    def __init__(self, duration, timeStep):
        self.time = np.arange(0, duration+timeStep, timeStep)
        self.printN = 10

        # Params: Figures
        self.figSize = (9.5, 8) # (width, height)
        self.figSizeWide = (9.5, 5)
        self.labelSizeTitle = 20 # Set fontsize
        self.labelSizeAxis = 16 # Set fontsize
        self.labelSizeTicks = 12 # Set fontsize
        self.lineThickness = 1.5
        self.tickLength = 4
        self.figureResolution = 600


    def complexFormation(self, concE, concS, concES, rateF, rateR):
        data = {'E': [concE], 'S': [concS], 'ES': [concES]}
        for i in range(0, len(self.time)-1, 1):
            e, s, es = data['E'][-1], data['S'][-1], data['ES'][-1]
            t1, t2 = self.time[i], self.time[i+1]
            dt = t2 - t1

            # Evaluate componets
            dES = (rateF*e*s - rateR*es) * dt
            data['ES'].append(es + dES)
            x = dES + rateR*es
            data['E'].append(x / (rateF * s))
            data['S'].append(x / (rateF * e))
        data = pd.DataFrame(data, index=self.time)
        print(f'Concentrations:\n{data}')
        return data


    def plotLines(self, data, labelX, labelY, title, colors):
        fig, ax = plt.subplots(figsize=self.figSize)
        for i in range(data.columns.size):
            ax.plot(data.index, data.iloc[:,i], color=colors[i],
                    label=data.columns[i], linewidth=self.lineThickness)

        ax.legend(fontsize=self.labelSizeTicks, loc='best', framealpha=0.8)

        # Styling
        ax.set_title(title, fontsize=self.labelSizeTitle, fontweight='bold')
        ax.set_xlabel(labelX, fontsize=self.labelSizeAxis)
        ax.set_ylabel(labelY, fontsize=self.labelSizeAxis, labelpad=20, rotation=90)
        ax.tick_params(labelsize=12)

        # Grid
        ax.grid(True, linewidth=0.25, color='black')
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)

        for _, spine in ax.spines.items():
            spine.set_visible(True)

        plt.tight_layout()
        fig.canvas.mpl_connect('key_press_event', pressKey)
        plt.show()
