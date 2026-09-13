import os
import matplotlib as mpl
import matplotlib.pyplot as plt
import sys


def pressKey(event):
    if event.key == 'escape':
        plt.close()
    elif event.key == 'e':
        sys.exit()
    elif event.key == 'r':
        python = sys.executable
        os.execl(python, python, *sys.argv)


class ODE:
    def __init__(self):
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


    def plotLines(self, data, labelX, labelY, title, lineSets):
        t1, y1, label = data

        fig, ax = plt.subplots(figsize=self.figSize)
        ax.plot(t1, y1, color='#101010', linewidth=self.lineThickness, label=label)
        for t2, y2, label2, color, linestyle, marker in lineSets:
            ax.plot(t2, y2, color=color, linewidth=self.lineThickness,
                    linestyle=linestyle, label=label2)
            ax.scatter(t2, y2, marker=marker, s=20, color=color, zorder=5)
        ax.legend(fontsize=self.labelSizeTicks, loc='best', framealpha=0.8)

        # Styling
        ax.set_title(title, fontsize=self.labelSizeTitle, fontweight='bold')
        ax.set_xlabel(labelX, fontsize=self.labelSizeAxis)
        ax.set_ylabel(labelY, fontsize=self.labelSizeAxis, rotation=0, labelpad=20)
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
