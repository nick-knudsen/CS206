from solution import SOLUTION
import constants as c
import copy

class PARALLEL_HILLCLIMBER:

    def __init__(self):
        self.parents = {}
        self.nextAvailableID = 0

        for i in range(c.populationSize):
            self.parents[i] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1

    def Evolve(self):
        
        for individual in self.parents.values():
            individual.Evaluate("GUI")

        # for currentGeneration in range(c.numberOfGenerations):
        #     self.Evolve_For_One_Generation()
        pass

    def Show_Best(self):
        #self.parent.Evaluate("GUI")
        pass

    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.child.Evaluate("DIRECT")
        self.Print()
        self.Select()

    def Spawn(self):
        self.child = copy.deepcopy(self.parent)
        self.child.Set_ID(self.nextAvailableID)
        self.nextAvailableID += 1

    def Mutate(self):
        self.child.Mutate()

    def Select(self):
        if (self.child.fitness < self.parent.fitness):
            self.parent = self.child

    def Print(self):
        print("\nParent Fitness: ", self.parent.fitness, "\tChild Fitness: ", self.child.fitness)