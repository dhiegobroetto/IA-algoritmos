# ----- Dhiego Santos Broetto ----- #
# ---------- 2016204404 ----------- #

from random import shuffle
<<<<<<< HEAD
import math
import random
import timeit
=======
import random
>>>>>>> a27eec03a5e6fdc52c785bc617d74af254027c92

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

<<<<<<< HEAD
def getValidState(VT, states, max_size) :
    if(getSizeState(VT, states) <= max_size) :
=======
def stateExpand(VT, states, T) :
    best_index = findBestState(VT, states, T)
    if(best_index >= 0) :
        states[best_index] += 1
>>>>>>> a27eec03a5e6fdc52c785bc617d74af254027c92
        return True
    else :
        return False

<<<<<<< HEAD
# ------ Roulette ------ #

def roulette(VT, states, best_element) :
    total = 0
    states_aux = states.copy()

    for i in range(len(states_aux)) :
        states_aux[i] = [states_aux[i], getValueState(VT, states_aux[i])]
    states_aux.sort(key = lambda pos: pos[1], reverse = True)
    states_best = states_aux[0:best_element].copy()
    for i in range(len(states_best)) :
        states_best[i] = states_best[i][0]

    for i in range(0, len(states_best)) :
        total += getValueState(VT, states_best[i])
    
    for i in range(0, len(states_best)) :
        states_aux.append([states_best[i],(getValueState(VT, states_best[i]) / total)])
    sortList(states_aux)
    
    rand = random.uniform(0, 1)
    percent = 0
    for i in range(0, len(states_aux)) :
        if rand <= (states_aux[i][1] + percent) :
            return states_aux[i][0]
        percent += states_aux[i][1]
    return -1

def sortList(list) :
    list.sort(key = lambda pos: pos[1], reverse = False)

# ------ Neighborhood ------ #

def getValidPositiveNeighbor(VT, state, states_list, max_size) :
    for i in range(0, len(state)):
        state_aux = state.copy()
        state_aux[i] += 1
        if getSizeState(VT, state_aux) <= round(max_size/2) :
            states_list.append(state_aux)

def defineValidNeighborhood(VT, state, states_list, max_size) :
    getValidPositiveNeighbor(VT, state, states_list, max_size)
=======
def getValidState(VT, states, T) :
    if(getSizeState(VT, states) <= T) :
        return True
    else :
        return False

def findBestState(VT, states, T) :
    total_value = 0
    best_index = -1
    for i in range(0, len(states)) :
        states[i] += 1
        if(getValidState(VT, states, T)) :
            state_value = getValueState(VT, states)
            if(state_value > total_value) :
                best_index = i
                total_value = state_value
        states[i] -= 1
    return best_index

def hillClimbing(VT, states, T) :
    while(True) :
        if(not stateExpand(VT, states, T)) :
            return states

# ------------------------ GRASP ------------------------ #

def generateRandomState(VT, max_size) :
    state = []
    while(True) :
        state = [random.randint(0, 3) for i in range(3)]
        if(getSizeState(VT, state) <= max_size and getValueState(VT, state) != 0) :
            return state
>>>>>>> a27eec03a5e6fdc52c785bc617d74af254027c92

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

<<<<<<< HEAD
def defineNeighborhood(VT, state, states_list) :
    getPositiveNeighbor(state, states_list)
    getNegativeNeighbor(state, states_list)

# ------ Hill Climbing ------ #

def hill_climbing_roulette(VT, max_size, states_list, best_element, timer) :
=======

def defineNeighborhood(VT, state, states_list) :
    getPositiveNeighbor(state, states_list)
    getNegativeNeighbor(state, states_list)   

def grasp(VT, T, best_state_trivial, states_list, max_iteration) :
>>>>>>> a27eec03a5e6fdc52c785bc617d74af254027c92
    best_value = 0
    best_state = [0] * len(VT)
    while(True) :
        find_best = False
<<<<<<< HEAD
        defineValidNeighborhood(VT, best_state, states_list, max_size)
        while(len(states_list) > 0) :
            state = roulette(VT, states_list, best_element)
            states_list.remove(state)
            state_value = getValueState(VT, state)
            if state_value > best_value :
                best_value = state_value
                best_state = state
                states_list.clear()
                find_best = True
                break
            if timer != 0 and (timeit.default_timer() - timer) > 120 :
                break
        if not find_best :
            break
        if timer != 0 and (timeit.default_timer() - timer) > 120 :
            break
    return best_state

# ------ Local Search ------ #

def deepest_descent(VT, T, best_state_trivial, states_list) :
    best_state = best_state_trivial
    best_value = getValueState(VT, best_state_trivial)
    while(True) :
        find_best = False
        defineNeighborhood(VT, best_state, states_list)
=======
        defineNeighborhood(VT, best_state, states_list)
        shuffle(states_list)
>>>>>>> a27eec03a5e6fdc52c785bc617d74af254027c92
        while(states_list != []) :
            state = states_list.pop()
            if(T >= getSizeState(VT, state)):
                if(best_value < getValueState(VT, state)) :
                    best_value = getValueState(VT, state)
                    best_state = state
                    find_best = True
                    states_list.clear()
        if(not find_best) :
            break
    return best_state

<<<<<<< HEAD
# ------ GRASP ------ #

def greedy_random_construct(VT, max_size, states_list, best_element, timer) :
    return hill_climbing_roulette(VT, max_size, states_list, best_element, timer)

def grasp(VT, max_size, best_element, max_iteration, timer = 0) :
    best_value = 0
    best_state = [0] * len(VT)
    states_list = []
    for i in range(max_iteration) :
        state = greedy_random_construct(VT, max_size, states_list, best_element, timer)
        if timer != 0 and (timeit.default_timer() - timer) > 120 :
            print("GRASP exceeded time limit (120 seconds)\n")
            break
        state_local = deepest_descent(VT, max_size, state, states_list)
        state_local_value = getValueState(VT, state_local)
        if getSizeState(VT, state_local) <= max_size :
            if state_local_value > best_value :
                best_value = state_local_value
                best_state = state_local
        if timer != 0 and (timeit.default_timer() - timer) > 120 :
            print("GRASP exceeded time limit (120 seconds)\n")
            break
    return best_state

# ------ Program ------ #

# Max size
max_size = 19
# Max iteration
max_iteration = 50
best_element = 2
# Object array
VT = [(1, 3), (4, 6), (5, 7)]
VT = [(1,3),(4,6),(5,7),(3,4), (2,6), (2,3), (6,8), (1,2),(3,5),(7,10),(10,15),(13,20),(24,25),(29,37)]
max_size = 13890000
states_list = []

best_state_grasp = grasp(VT, max_size, best_element, max_iteration, timeit.default_timer())

# Results
=======
# Max size
T = 19 
# Object array
VT = [(1, 3), (4, 6), (5, 7)]
max_iteration = 100

# Trivial solution
states = [0] * len(VT)
best_state_trivial = hillClimbing(VT, states, T)

# GRASP
states_list = []
best_state_grasp = grasp(VT, T, best_state_trivial, states_list, max_iteration)

# Results
total_value_trivial = getValueState(VT, best_state_trivial)
total_size_trivial = getSizeState(VT, best_state_trivial)

>>>>>>> a27eec03a5e6fdc52c785bc617d74af254027c92
total_value_grasp = getValueState(VT, best_state_grasp)
total_size_grasp = getSizeState(VT, best_state_grasp)

print("GRASP")
<<<<<<< HEAD
print ("[Total Value => ", total_value_grasp, ", Total Size => ", total_size_grasp, ", Best State => ", best_state_grasp)
=======
print ("[Total Value => ", total_value_grasp, ", Total Size => ", total_size_grasp, ", Best State => ", best_state_grasp)
>>>>>>> a27eec03a5e6fdc52c785bc617d74af254027c92
