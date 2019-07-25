import sys
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

print('Parsing and plotting for data from Gaussian16 output files.')
print('Written by Damon Hinz, 2019')
print('')

if len(sys.argv) <=1:
    print('Input path to Gaussian output file:')
    name = input()
else:
    name = sys.argv[1]

def scf():

    substr = 'SCF Done'
    scfEnergy = []  #List for SCF energies
    
    with open (name, 'r') as text_file:
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
    
    with open(name, 'r') as text_file:
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

def pes():

    pes = []
    substr = 'SCF Done'
    save_point = 'Stationary point found'
    last_scf_line = ''
    with open(name, 'r') as text_file:
        for line in text_file:
            if substr in line:
                last_scf_line = line # store for later
            if save_point in line:
                pes.append(last_scf_line[25:38])

    pes = [float(i) for i in pes]
    df = pd.DataFrame({'Energy': pes})

    plt.xlabel('Step')
    plt.ylabel('Energy (hartrees)')
    plt.xticks(np.arange(0, len(pes), 1))
    plt.plot(df)
    plt.show()

choice = None
while choice != 'quit':
    choice = input('What would you like to plot? [SCF, Force, PES, quit]')
    if choice == 'SCF':
        scf()
    elif choice == 'Force':
        maxForce()
    elif choice == 'PES':
        pes()
    elif choice == 'quit':
        pass
    else:
        print('Please try again.')
