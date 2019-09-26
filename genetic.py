# ----- Dhiego Santos Broetto ----- #
# ---------- 2016204404 ----------- #

from random import shuffle
import math
import random

def getValueState(VT, states) :
    total_value = 0
    for i in range(0, len(states)) :
        total_value += VT[i][0] * states[i]
    return total_value

def getSizeState(VT, states) :
    total_size = 0
    for i in range(0, len(states)) :
        total_size += VT[i][1] * states[i]
    return total_size

# ------------------------ Genetic ------------------------ #

def getPositiveNeighbor(state, states_list) :
    for i in range(0, len(state)):
        state_aux = state.copy()
        state_aux[i] += 1
        states_list.append(state_aux)

def getNegativeNeighbor(state, states_list) :
    for i in range(0, len(state)):
        if state[i] > 0:
            state_aux = state.copy()
            state_aux[i] -= 1
            states_list.append(state_aux)


def defineNeighborhood(VT, state, states_list) :
    getPositiveNeighbor(state, states_list)
    getNegativeNeighbor(state, states_list)   

def genetic(VT, max_size, population_size):
    population = []
    best_solution = [0] * len(VT)
    best_value = getValueState(VT, best_solution)
    for _ in range(population_size):
        state = generateRandomState(VT, max_size)
        population.append(state)
    
    while(True) :
        find_best = False
        sortList(population)
        while(population != []) :
            state = population.pop()
            if(T >= getSizeState(VT, state)):
                if(best_value < getValueState(VT, state)) :
                    best_value = getValueState(VT, state)
                    best_state = state
            population = select_best(population,n,values)
                    
        if(not find_best) :
            break
    

def generateRandomState(VT, T) :
    state = []
    while(True) :
        state = [random.randint(0, 3) for i in range(3)]
        if(getSizeState(VT, state) <= T) :
            return state

def sortList(population) :
    population.sort(key = lambda pos: pos[1], reverse = False)

# Max size
max_size = 19 
# Object array
VT = [(1, 3), (4, 6), (5, 7)]
population_size = 5

crossover_ratio = 0.5
mutation_ratio = 0.1
n = 3



# Genetic
states_list = []
best_genetic = genetic(VT, max_size, t, alpha, states_list)

# Results
total_value_simple = getValueState(VT, best_genetic)
total_size_simple = getSizeState(VT, best_genetic)

print("Simple Descent")
print ("[Total Value => ", total_value_simple, ", Total Size => ", total_size_simple, ", Best State => ", best_genetic)