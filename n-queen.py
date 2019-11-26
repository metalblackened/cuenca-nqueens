import random
import time
import numpy as np
from base import Session, engine, Base
from models import SolutionModel
from querys import get_or_create_solution
from ga import create_chromosome,fitness,sortPopulation,crossover,mutate

def number_solutions(n):
    solutions = [1,0,0,2,10,4,40,92,352,724,2680,14200,73712,
                 365596,2279184,14772512,95815104,666090624,
                 4968057848,39029188884,314666222712,2691008701644,
                 24233937684440,227514171973736,2207893435808352,
                 22317699616364044,234907967154122528]
 
    return solutions[n-1]

def print_chromosome(chrom):
    print("Chromosome = {},  Fitness = {}"
        .format(str(chrom), fitness(chrom,total_clashes)))

def getSolutions(n_queens):
    session = Session()
    return session.query(SolutionModel).filter(SolutionModel.n_queens == n_queens).all()


def generate(population, fitness):
    mutation = 0.1
    new_population = []
    sort_population = sortPopulation(population,total_clashes,n_queens)
    new_population = [x[0] for x in sort_population[:5000]]
    for i in range(len(new_population)):
        child = crossover(random.choice(new_population[:5000]),random.choice(new_population[:5000]))
        if random.random() < mutation:
            child = mutate(child)
        new_population.append(child)
        if fitness(child,total_clashes) == total_clashes: 
            break
    new_population = sortPopulation(new_population,total_clashes,n_queens)
    return [x[0] for x in new_population]
    
def findSolution():
    population = [create_chromosome(n_queens) for _ in range(1000)]
    generation = 0

    while not total_clashes in [fitness(individual,total_clashes) for individual in population]:
        print("-------Generacion {} -----Mejor solucion----{}---Soluciones totales encontradas = {}".format(generation,population[0],solutionsFounded))
        population = generate(population, fitness)
        #print("Maximum Fitness = {}".format(max([fitness(n) for n in population])))
        generation += 1
    
    solution = []
    for chromosome in population:
        if fitness(chromosome,total_clashes) == total_clashes:
            solution = chromosome
            print_chromosome(solution)
            break
    return solution

if __name__ == "__main__":
    start_time = time.time()
    Base.metadata.create_all(engine)
    menu_opcion = int(input("Menu: \n 1.- Encontrar soluciones \n 2.- Ver soluciones\n"))
    n_queens = int(input("Ingresa el numero de reinas:  \n"))
    total_clashes = (n_queens*(n_queens-1))/2
    
    if menu_opcion == 2:
        for row in getSolutions(n_queens):
            recordObject = {'n_queens': row.n_queens,
                        'solution': row.solution}
            print(recordObject)
    else:
        print("El numero de choques posibles son:" + str(total_clashes))
        print("El numero de soluciones posibles es:" + str(number_solutions(n_queens)))
 
        solutions = []
        solutionsFounded = 0
        while True:
            sol = findSolution()
            if sol not in solutions:
                solutionsFounded = solutionsFounded +1
                print("############################################")
                print("Soluciones totales encontradas = {}".format(str(solutionsFounded)))
                print("############################################")
                get_or_create_solution(n_queens,sol)
                solutions.append(sol)
            if(len(solutions) == number_solutions(n_queens)):
                break

