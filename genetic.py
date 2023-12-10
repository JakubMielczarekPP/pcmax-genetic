from random import randint, random

POPULATION_SIZE = 20
MUTATION_PROBABILITY = 0.1
GENERATION_NUMBER = 1000

# generate population with randomized genotypes
def generate_population(processors, processes, population_size):
    population = []

    for _ in range(population_size):
        genotype = [[] for _ in range(processors)]
        for process in processes:
            genotype[randint(0, processors - 1)].append(process)
            population.append(genotype)

    return population

# check the fitness score of genotype
def fitness(genotype):
    end_times = [sum(processor) for processor in genotype]
    max_end_time = max(end_times)

    return max_end_time

# select two fittest genotypes
def selection(population):
    sorted_by_fitness = sorted(population, key=lambda genotype: fitness(genotype))

    return (sorted_by_fitness[0], sorted_by_fitness[1])

# crossover two genotypes
def crossover(parent1, parent2):
    half_len = round(len(parent1)/2)

    child1 = parent1[:half_len] + parent2[half_len:]
    child2 = parent1[half_len:] + parent2[:half_len]

    return (child1, child2)

# mutation
def mutation(population, mutation_probability):
    for genotype in population:
        if random() < mutation_probability:
            index1 = 0
            index2 = 0

            while index1 == index2:
                index1 = randint(0, len(genotype) - 1)
                index2 = randint(0, len(genotype) - 1)

            genotype[index1], genotype[index2] = genotype[index2], genotype[index1]


def pcmax_genetic(processors, processes):

    best_time = -1
    i = 0

    while i < GENERATION_NUMBER:
        # generate initial population
        population = generate_population(processors, processes, POPULATION_SIZE)

        # select two fittest genotypes
        parent1, parent2 = selection(population)

        # crossover the fittest genotypes
        child1, child2 = crossover(parent1, parent2)

        # replace two least fit genotypes with the children
        least_fit = max(population, key=lambda genotype: fitness(genotype))
        population[population.index(least_fit)] = child1

        second_least_fit = max(population, key=lambda genotype: fitness(genotype))
        population[population.index(second_least_fit)] = child2

        # try to mutate all genotypes
        mutation(population, MUTATION_PROBABILITY)

        new_best = fitness(parent1)
        if new_best < best_time or best_time < 0:
            best_time = new_best

        i += 1

    return best_time

