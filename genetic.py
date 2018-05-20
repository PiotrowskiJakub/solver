from random import shuffle, randrange, sample, random


def makespan(perm, times):
    job_count = len(perm)
    machine_count = len(times[0])

    makespan = [[0] * (machine_count + 1) for _ in range(0, job_count + 1)]
    for i, job in enumerate(perm):
        for machine in range(0, machine_count):
            makespan[i + 1][machine + 1] = max(makespan[i][machine + 1], makespan[i + 1][machine]) + times[job - 1][
                machine]

    return makespan[job_count][machine_count]


def genetic(times):
    population_size = 100
    num_of_epochs = 100
    job_count = len(times)
    population = [list(range(1, job_count + 1)) for _ in range(0, population_size)]
    for individual in population:
        shuffle(individual)

    population_with_fitness = evaluate_fitness(population, times)
    for _ in range(0, num_of_epochs):
        parents = choose_parents(population_with_fitness)
        children = breed(parents)
        mutate(children)
        population_with_fitness = merge(population_with_fitness, evaluate_fitness(children, times))
    return choose_best(population_with_fitness)[0]


def evaluate_fitness(population, times):
    return [(individual, makespan(individual, times)) for individual in population]


def choose_parents(population):
    parents = []
    for _ in range(0, len(population)):
        tournament = sample(population, 5)
        parents.append(choose_best(tournament))

    return parents


def breed(parents):
    shuffle(parents)
    children = []
    for i in range(1, len(parents), 2):
        children += pmx(parents[i - 1][0], parents[i][0])
    return children


def mutate(children):
    for child in children:
        if random() > 0.6:
            left = randrange(0, len(child))
            right = randrange(left, len(child))

            tmp = child[left]
            child[left] = child[right]
            child[right] = tmp


def merge(parents, children):
    both = parents + children
    both.sort(key=lambda x: x[1])
    return both[:len(parents)]


def choose_best(population):
    return min(population, key=lambda x: x[1])


def translate(x, d):
    while x in d and x != d[x]:
        x = d[x]
    return x


def pmx(a, b):
    length = len(a)
    left = randrange(0, length + 1)
    right = randrange(left, length + 1)

    a2 = a[left:right]
    b2 = b[left:right]
    d = dict(zip(a2, b2))
    d_inv = dict(zip(b2, a2))

    child1 = list(map(lambda x: translate(x, d_inv), a[0:left])) + b2 + list(map(lambda x: translate(x, d_inv),
                                                                                 a[right:length + 1]))
    child2 = list(map(lambda x: translate(x, d), b[0:left])) + a2 + list(
        map(lambda x: translate(x, d), b[right:length + 1]))

    return [child1, child2]
