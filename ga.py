import random
import numpy as np

def create_chromosome(size): #creamos un cromosoma aleatorio 
    return [ random.randint(1, size) for _ in range(size) ]

def fitness(chromosome,maxfitness):
    clashes = 0;
    # calculate row and column clashes
    # just subtract the unique length of array from total length of array
    # [1,1,1,2,2,2] - [1,2] => 4 clashes
    row_col_clashes = abs(len(chromosome) - len(np.unique(chromosome)))
    clashes += row_col_clashes 

    # calculate diagonal clashes
    for i in range(len(chromosome)):
        for j in range(len(chromosome)):
            if ( i != j):
                dx = abs(i-j)
                dy = abs(chromosome[i] - chromosome[j])
                if(dx == dy):
                    clashes += 1
    
    return maxfitness - clashes

def probability(chromosome,maxfitness,size):
    return fitness(chromosome,maxfitness) / size

def sortPopulation(population,maxfitness,size):
    probabilities = [probability(individual,maxfitness,size) for individual in population]
    population_probabilities = list(zip(population,probabilities))
    sorted_population = sorted(population_probabilities, key = lambda x: x[1], reverse=True)
    return sorted_population

def crossover(best_individual,individual):
    n = len(best_individual)
    child = []
    for i in range(n):
        if best_individual[i] == individual[i]:
            child.append(best_individual[i])
        else:
            child.append(random.randint(1, n))
    return child

def mutate(individual):  #randomly changing the value of a random index of a chromosome
    n = len(individual)
    gen = random.randint(0, n - 1)
    newgen = random.randint(1, n)
    individual[gen] = newgen
    return individual

