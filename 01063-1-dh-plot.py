import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

print('Parsing and plotting for data from Gaussian16 output files.')
print('Written by Damon Hinz, 2019')
print('')


def scf():

    substr = 'SCF Done'
    scfEnergy = []  #List for SCF energies
    
    with open ('01063-1-dh.log', 'r') as text_file:
        for line in text_file:
            if line.find(substr) != -1:
                scfEnergy.append(line[25:38])

    scfEnergy = [float(i) for i in scfEnergy]
    df = pd.DataFrame({'Energy': scfEnergy})


    plt.xlabel('Step')
    plt.ylabel('Energy (hartrees)')
    plt.xticks(np.arange(0, len(scfEnergy), 1))
    plt.plot(df)
    plt.show()

def maxForce():

    maxForce = []
    
    with open('01063-1-dh.log', 'r') as text_file:
        for line in text_file:
            if line.find('Maximum Force') != -1:
                maxForce.append(line[26:34])

    maxForce = [float(i) for i in maxForce]
    df = pd.DataFrame({'Force': maxForce})

    plt.xlabel('Step')
    plt.ylabel('Max Force (hartrees)')
    plt.xticks(np.arange(0, len(maxForce), 1))
    plt.plot(df)
    plt.show()

choice = None
while choice != 'quit':
    choice = input('What would you like to plot? [SCF, Force, quit]')
    print('')
    if choice == 'SCF':
        scf()
    elif choice == 'Force':
        maxForce()
    elif choice == 'quit':
        pass
    else:
        print('Please try again.')
