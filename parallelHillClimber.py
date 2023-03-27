from solution import SOLUTION
import constants as c
import copy
import os

class PARALLEL_HILLCLIMBER:

    def __init__(self):
        os.system("del brain*.nndf")
        os.system("del tmp*.txt")
        os.system("del fitness*.txt")

        self.parents = {}
        self.nextAvailableID = 0

        for i in range(c.populationSize):
            self.parents[i] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1

    def Evolve(self):
        self.Evaluate(self.parents)
        for currentGeneration in range(c.numberOfGenerations):
             self.Evolve_For_One_Generation()

    def Show_Best(self):
        #self.parent.Evaluate("GUI")
        pass

    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children)
        self.Print()
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

    def Evaluate(self, solutions):
        for individual in solutions.values():
            individual.Start_Simulation("DIRECT")

        for individual in solutions.values():
            individual.Wait_For_Simulation_To_End()

    def Select(self):
        for key in self.parents.keys():
            if (self.children[key].fitness < self.parents[key].fitness):
                self.parents[key] = self.children[key]

    def Print(self):
        print("\n")
        for key in self.parents.keys():
            print("Parent Fitness: ", self.parents[key].fitness, "\tChild Fitness: ", self.children[key].fitness)
        print("\n")