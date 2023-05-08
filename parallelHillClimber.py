from solution import SOLUTION
import constants as c
import copy
import os
import numpy as np

class PARALLEL_HILLCLIMBER:

    def __init__(self, waveType, freq, restart=False, gen=0):
        os.system("del tmp*.txt")
        os.system("del fitness*.txt")
        

        self.restart = restart
        self.gen = gen
        self.waveType = waveType
        self.freq = freq

        self.parents = {}
        
        if restart:
            filename = "data/fitnessVals_" + str(self.waveType) + "_" + str(self.freq) + ".npy"
            self.fitnessVals = np.load(filename)
            self.nextAvailableID = self.gen*c.populationSize
        else:
            self.fitnessVals = np.empty((c.populationSize, c.numberOfGenerations))
            self.nextAvailableID = 0

        for i in range(c.populationSize):
            if restart:
                prefix = "data/"
                filename = "gen" + str(self.gen-1) + "Parent_" + str(self.waveType) + "_" + str(self.freq)+".npy"
                weights = np.load(prefix + filename)
                self.parents[i] = SOLUTION(self.nextAvailableID, waveType, freq, False, weights)
            else:
                self.parents[i] = SOLUTION(self.nextAvailableID, self.waveType, self.freq)
            self.nextAvailableID += 1

    def Evolve(self):
        self.Evaluate(self.parents, self.gen, save=False)
        # try:
        currGen = self.gen
        for currentGeneration in range(self.gen, c.numberOfGenerations):
            self.Evolve_For_One_Generation(currGen)
            currGen += 1
            os.chdir("data")
            filename = "fitnessVals_" + str(self.waveType) + "_" + str(self.freq) + ".npy"
            os.system("del " + filename)
            np.save(filename, self.fitnessVals)  
            os.chdir("..")
            os.system("del fitness*.txt")
        # except Exception as exception:
        #     print(exception)

    def Save_Best(self, filename):
        maxFitness = 0
        for key in self.parents.keys():
            if self.parents[key].fitness > maxFitness:
                maxFitness = self.parents[key].fitness
                bestParent = self.parents[key]
        np.save(filename, bestParent.weights)


    def Evolve_For_One_Generation(self, currGen):
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children, currGen)
        self.Print(currGen)
        self.Select()
        path = "gen"
        suffix = "Parent_" + str(self.waveType) + "_" + str(self.freq) + ".npy"
        filename =  path + str(currGen) + suffix
        os.chdir("data")
        os.system("del " + path + "*" + suffix)
        os.chdir("..")
        self.Save_Best("data/" + filename)

    def Spawn(self):
        self.children = {}

        for i in self.parents.keys():
            self.children[i] = copy.deepcopy(self.parents[i])
            self.children[i].Set_ID(self.nextAvailableID)
            self.nextAvailableID += 1

    def Mutate(self):
        for child in self.children.values():
            child.Mutate()

    def Evaluate(self, solutions, currGen, save=True):
        for individual in solutions.values():
            individual.Start_Simulation("DIRECT")

        for individual in solutions.values():
            individual.Wait_For_Simulation_To_End()
            genID = individual.myID - c.populationSize*(currGen+1)
            self.fitnessVals[genID][currGen] = round(individual.fitness, 4)

    def Select(self):
        mostFitness = 0
        for key in self.parents.keys():
            if self.parents[key].fitness > mostFitness:
                mostFitness = self.parents[key].fitness
                mostFit = self.parents[key]
            if self.children[key].fitness > mostFitness:
                mostFitness = self.children[key].fitness
                mostFit = self.children[key]
        for key in self.parents.keys():   
                self.parents[key] = mostFit

    def Print(self, currGen):
        print("\n")
        print(currGen+1, "/", c.numberOfGenerations, " Generations")
        print("\n")