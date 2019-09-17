# ----- Dhiego Santos Broetto ----- #
# ---------- 2016204404 ----------- #

import random
from random import shuffle

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

def stateExpand(VT, states, T) :
    best_index = findBestState(VT, states, T)
    if(best_index >= 0) :
        states[best_index] += 1
        return True
    else :
        return False

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

# ------------------------ Simple Descent ------------------------ #

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

def simple_descent(VT, T, state, states_list) :
    best_value = getValueState(VT, state)
    best_state = state.copy()
    while(True) :
        find_best = False
        defineNeighborhood(VT, best_state, states_list)
        shuffle(states_list)
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

# ------------------------ Deepest Descent ------------------------ #

def generateRandomState(VT, T) :
    state = []
    while(True) :
        state = [random.randint(0, 3) for i in range(3)]
        if(getSizeState(VT, state) <= T) :
            return state

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

def deepest_descent(VT, T, state, states_list) :
    best_state = state.copy()
    best_value = getValueState(VT, best_state)
    while(True) :
        find_best = False
        defineNeighborhood(VT, best_state, states_list)
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

# ------------------------ Multistart Descent ------------------------ #

def multistart_descent(VT, T, states_list, states_number, deepest) :
    best_state_global = generateRandomState(VT, T)
    best_value = getValueState(VT, best_state_global)
    for _ in range(states_number) :
        state = generateRandomState(VT, T)
        if(deepest) :
            best_state = deepest_descent(VT, T, state, states_list)
        else :
            best_state = simple_descent(VT, T, state, states_list)
        if(getValueState(VT, best_state) > best_value) :
            best_value = getValueState(VT, best_state)
            best_state_global = best_state
    return best_state_global

# Max size
T = 19 
# Object array
VT = [(1, 3), (4, 6), (5, 7)]
# Number of states to multistart
states_number = 10

# Trivial solution
states = [0] * len(VT)
best_state_trivial = hillClimbing(VT, states, T)

# Multistart descent
states_list = []

# Simple descent
best_state_simple = multistart_descent(VT, T, states_list, states_number, False)

# Deepest descent
best_state_deepest = multistart_descent(VT, T, states_list, states_number, True)

# Results
total_value_trivial = getValueState(VT, best_state_trivial)
total_size_trivial = getSizeState(VT, best_state_trivial)

total_value_simple = getValueState(VT, best_state_simple)
total_size_simple = getSizeState(VT, best_state_simple)

total_value_deepest = getValueState(VT, best_state_deepest)
total_size_deepest = getSizeState(VT, best_state_deepest)

print("Trivial Solution")
print ("[Total Value => ", total_value_trivial, ", Total Size => ", total_size_trivial, ", Best State => ", best_state_trivial)

print("Simple Descent")
print ("[Total Value => ", total_value_simple, ", Total Size => ", total_size_simple, ", Best State => ", best_state_simple)

print("Deepest Descent")
print ("[Total Value => ", total_value_deepest, ", Total Size => ", total_size_deepest, ", Best State => ", best_state_deepest)