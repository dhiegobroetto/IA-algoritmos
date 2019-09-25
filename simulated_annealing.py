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

# ------------------------ Simulated Annealing ------------------------ #

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

def probabilityState(worst_case,state,t) :
    p = 1/math.exp(1)**((worst_case-state)/t)
    r = random.uniform(0,1)
    return r < p

def simulated_annealing(VT, max_size, t, alpha, states_list) :
    best_value = 0
    best_state = [0] * len(VT)
    while(t >= 1) :
        find_best = False
        defineNeighborhood(VT, best_state, states_list)
        shuffle(states_list)
        while(states_list != []) :
            state = states_list.pop()
            if(max_size >= getSizeState(VT, state)):
                if(best_value < getValueState(VT, state)) :
                    best_value = getValueState(VT, state)
                    best_state = state
                    find_best = True
                    states_list.clear()
                else :
                    if(probabilityState(getValueState(VT, state),getValueState(VT,best_state),t)) :
                        best_value = getValueState(VT, state)
                        best_state = state
                        find_best = True
                        break
        if(not find_best) :
            break
        t *= alpha
    return state

# Max size
max_size = 19 
# Object array
VT = [(1, 3), (4, 6), (5, 7)]
t = 100
alpha = 0.5

# Trivial solution
# states = [0] * len(VT)
# best_state_trivial = hillClimbing(VT, states, max_size)

# Simulated Annealing
states_list = []
best_simulated_annealing = simulated_annealing(VT, max_size, t, alpha, states_list)

# Results
# total_value_trivial = getValueState(VT, best_state_trivial)
# total_size_trivial = getSizeState(VT, best_state_trivial)

total_value_simple = getValueState(VT, best_simulated_annealing)
total_size_simple = getSizeState(VT, best_simulated_annealing)

print("Simple Descent")
print ("[Total Value => ", total_value_simple, ", Total Size => ", total_size_simple, ", Best State => ", best_simulated_annealing)