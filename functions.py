import os
import math
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sys


def pressKey(event):
    if event.key == 'escape':
        plt.close()
    elif event.key == 'e':
        sys.exit()
    elif event.key == 'r':
        python = sys.executable
        os.execl(python, python, *sys.argv)


class Functions:
    def __init__(self, duration, timestep):
        self.time = 0
        self.getTime(duration, timestep)
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


    def getTime(self, duration, timeStep):
        time = [t for t in range(0, duration+timeStep, timeStep)]
        if len(time) % 2 != 0:
            time = time[0:len(time)-1]
        self.time = time


    def complexFormation(self, concE, concS, concES, rateF, rateR):
        data = {'E': [concE], 'S': [concS], 'ES': [concES]}
        print(f'Time: {self.time}')
        for i in range(0, len(self.time), 2):
            e, s, es = data['E'][-1], data['S'][-1], data['ES'][-1]
            t1, t2 = self.time[i], self.time[i+1]
            dt = t2 - t1
            print(f'dt = {t2}-{t1} = {dt}')

            # Evaluate componets
            dES = (rateF*e*s - rateR*s) * dt
            data['ES'].append(es + dES)
            x = dES + rateR*es
            data['E'].append(x / (rateF * s))
            data['S'].append(x / (rateF * e))

        data = pd.DataFrame(data)
        print(f'\nConcentrations:\n{data}')
        print(f'{data.columns.size}')
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
