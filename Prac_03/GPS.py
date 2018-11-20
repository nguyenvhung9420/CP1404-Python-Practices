import random

def main():
    pop = 1000

    for i in range(10):
        deaths = generateDeath(0.05, 0.25, pop)
        births = generateBirth(0.1, 0.2, pop)
        print("Year {}: {} were/was born. {} were/was dead.".format((i+1),births, deaths))
        pop += births
        pop -= deaths
        print("Population is {} people.".format(pop))


def generateDeath(lower, upper, population):
    deathPercent = random.uniform(lower, upper)
    deathNumber = int(population * deathPercent)
    return deathNumber

def generateBirth(lower, upper, population):
    birthPercent = random.uniform(lower, upper)
    birthNumber = int(population * birthPercent)
    return birthNumber

main()