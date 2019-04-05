# -*- coding: utf-8 -*-
"""A Genetic Algorithm (GA) Test

Decsription of GA:
--------------------
SETUP
    step 1: Initialize: Create a population of N elements, each with randomly generated DNA.
DRAW
    step 2: Selection: Evaluate the fitness of each element of the population and build a mating pool.
    step 3: Reproduction: Repeat N times:
        a. Pick two (or whatever number you like) parents with probability according to relative fitness.
        b. Crossover - create a "child" by combining the DNA of these two parents.
        c. Mutation - mutate the child's DNA based on a given probability.
        d. Add the new child to a new population.
    step 4. Leave the poor parents and generate new population, replace the old population with the new population and return to step 2.

Scenario of this test:
---------------------
Here is the sentence (string): "To be or not to be, that is a question."
Using GA to generate this sentence.
"""
import numpy as np
import matplotlib.pyplot as plt
import string, time

class DNA(object):
    """docstring for DNA."""
    def __init__(self, length):
        super(DNA, self).__init__()
        self.length = length
        self.pool = list(string.ascii_letters[:] + ',. ')
        self.dna = self.generate()

    def generate(self):
        return ''.join(np.random.choice(self.pool, self.length))

    def crossover(self, anoDNA):
        crossover_point = np.random.randint(self.length)
        babyDNA = DNA(self.length)
        babyDNA.dna = self.dna[:crossover_point] + anoDNA.dna[crossover_point:]
        return babyDNA

    def mutate(self, mutation_rate):
        dna_array = list(self.dna)
        for i, c in enumerate(dna_array):
            if np.random.uniform() <= mutation_rate:
                dna_array[i] = np.random.choice(self.pool)
        self.dna = ''.join(dna_array)


class Population(object):
    """docstring for Population."""
    def __init__(self, target, mutation_rate, pop_size):
        super(Population, self).__init__()
        self.target = target
        self.elem_length = len(self.target)
        self.mutation_rate = mutation_rate
        self.pop_size = pop_size
        self.population = [DNA(self.elem_length) for i in range(self.pop_size)]

    def calc_fitness(self):
        self.fitness_list = list(map(self.fitness_between, self.population))

    def fitness_between(self, elem):
        score = 0
        for i, c in enumerate(elem.dna):
            if c == self.target[i]:
                score += 1
        return 2**(score-self.elem_length)

    def generate_next_generation(self):
        next_Generation = Population(self.target, self.mutation_rate, self.pop_size)
        next_Generation.population = []
        for i in range(self.pop_size):
            # Pick parents
            prob = self.fitness_list / np.sum(self.fitness_list)
            parent1, parent2 = np.random.choice(self.population, 2, p=prob)
            # Crossover
            baby = parent1.crossover(parent2)
            # Mutation
            baby.mutate(self.mutation_rate)
            # Add the baby to new generation
            next_Generation.population.append(baby)
        next_Generation.calc_fitness()
        return next_Generation

def GA(target, mutation_rate, pop_size):
    p = Population(target, mutation_rate, pop_size)
    p.calc_fitness()
    t1 = time.time()
    num_generations = 0
    max_fitness_list = []
    while target not in [elem.dna for elem in p.population]:
        p = p.generate_next_generation()
        num_generations += 1
        print('\rnum. of gen: %3d, max_fitness: %.2f, best: %s'
                %(num_generations,
                  max(p.fitness_list),
                  p.population[np.argsort(p.fitness_list)[-1]].dna),
              end='')
        max_fitness_list.append(max(p.fitness_list))
    print("\nCosts %.4f sec." %(time.time() - t1))
    steps = np.arange(0, num_generations)

    fig = plt.figure(figsize=(7, 5))
    plt.plot(steps, max_fitness_list, lw=1, c='k', alpha=0.5, label='path')
    plt.xlabel('steps')
    plt.ylabel('max fitness of each generation')
    plt.legend()
    plt.show()


if __name__=="__main__":
    target = 'To be or not to be.'
    mutation_rate = 0.01
    pop_size = 200
    GA(target, mutation_rate, pop_size)
