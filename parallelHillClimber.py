from solution import SOLUTION
import constants as c
import copy
import os
import numpy as np

class PARALLEL_HILLCLIMBER:

    def __init__(self, waveType, freq):
        #os.system("del brain*.nndf")
        os.system("del tmp*.txt")
        os.system("del fitness*.txt")

        self.waveType = waveType
        self.freq = freq

        self.parents = {}
        self.nextAvailableID = 0
        self.fitnessVals = np.empty((c.populationSize, c.numberOfGenerations))

        for i in range(c.populationSize):
            self.parents[i] = SOLUTION(self.nextAvailableID, self.waveType, self.freq)
            self.nextAvailableID += 1

    def Evolve(self):
        self.Evaluate(self.parents, 0)
        for currentGeneration in range(1, c.numberOfGenerations):
             self.Evolve_For_One_Generation(currentGeneration)
        filename = "data/fitnessVals_" + str(self.waveType) + "_" + str(self.freq) + ".npy"
        np.save(filename, self.fitnessVals)

    def Save_Best(self):
        minFitness = 10000
        for key in self.parents.keys():
            if self.parents[key].fitness < minFitness:
                minFitness = self.parents[key].fitness
                bestParent = self.parents[key]
        filename = "bestSolution_" + str(self.waveType) + "_" + str(freq)
        np.save(filename, bestParent.weights)
        
        #
        pass

    def Evolve_For_One_Generation(self, currGen):
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children, currGen)
        self.Print(currGen)
        self.Select()

    def Spawn(self):
        self.children = {}

        for i in self.parents.keys():
            self.children[i] = copy.deepcopy(self.parents[i])
            self.children[i].Set_ID(self.nextAvailableID)
            self.nextAvailableID += 1

    def Mutate(self):
        for child in self.children.values():
            child.Mutate()

    def Evaluate(self, solutions, currGen):
        for individual in solutions.values():
            individual.Start_Simulation("DIRECT")

        for individual in solutions.values():
            individual.Wait_For_Simulation_To_End()
            genID = individual.myID - c.populationSize*currGen
            self.fitnessVals[genID][currGen] = round(individual.fitness, 4)

    def Select(self):
        mostFitness = 1000
        for key in self.parents.keys():
            if self.parents[key].fitness < mostFitness:
                mostFitness = self.parents[key].fitness
                mostFit = self.parents[key]
            if self.children[key].fitness < mostFitness:
                mostFitness = self.children[key].fitness
                mostFit = self.children[key]
        for key in self.parents.keys():   
                self.parents[key] = mostFit

    def Print(self, currGen):
        print("\n")
        print(currGen+1, "/", c.numberOfGenerations, " Generations")
        print("\n")