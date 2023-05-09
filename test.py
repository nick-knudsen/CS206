from matplotlib.pyplot import imshow, subplot, subplots, show
import numpy as np

#fig, axs = subplots(3,2, sharex = True, sharey = True)
subplot_row = 0
subplot_index = 1
waveTypes = ['Sine','Square','Sawtooth']
sensorNames = ('BackLowerLeg','FrontLowerLeg','LeftLowerLeg','RightLowerLeg')
for waveType in range(1,4):
    subplot_col = 0
    for freq in [0.1, 0.2]:
        filename = "data/sensorValues_" + str(waveType) + "_" + str(freq) + ".npy"

        data = np.load(filename)
        formatted = np.zeros((8, 1000))
        for i in range(4):
            formatted[2*i] = data[i]

        for row in range(8):
            for col in range(1000):
                if formatted[row][col] == -1:
                    formatted[row][col] = 0

        truncated = formatted[:,:500]
        ax = subplot(3,2,subplot_index)
        title_str = waveTypes[waveType-1] + " w/ frequency " + str(freq)
        ax.set_title(title_str)
        ax.set_yticks([0,2,4,6], labels=sensorNames)
        #axs[subplot_row, subplot_col] = imshow(truncated, cmap="Greys", interpolation="nearest", aspect=20)
        imshow(truncated, cmap="Greys", interpolation="nearest", aspect=20)
        subplot_index += 1
        subplot_col += 1
    subplot_row += 1
show()