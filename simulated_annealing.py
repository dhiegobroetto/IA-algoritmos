# ----- Dhiego Santos Broetto ----- #
# ---------- 2016204404 ----------- #

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

def simulated_annealing(VT, max_size, t, alpha, state) :
    # best_value = 0
    # best_state = [0] * len(VT)
    # while(True) :
    #     find_best = False
    #     defineNeighborhood(VT, best_state, states_list)
    #     shuffle(states_list)
    #     while(states_list != []) :
    #         state = states_list.pop()
    #         if(max_size >= getSizeState(VT, state)):
    #             if(best_value < getValueState(VT, state)) :
    #                 best_value = getValueState(VT, state)
    #                 best_state = state
    #                 find_best = True
    #                 states_list.clear()
    #     if(not find_best) :
    #         break
    return state

# Max size
max_size = 19 
# Object array
VT = [(1, 3), (4, 6), (5, 7)]

# Trivial solution
# states = [0] * len(VT)
# best_state_trivial = hillClimbing(VT, states, max_size)

# Simulated Annealing
states_list = []
best_state_simple = simulated_annealing(VT, max_size, best_state_trivial, states_list)

# Results
total_value_trivial = getValueState(VT, best_state_trivial)
total_size_trivial = getSizeState(VT, best_state_trivial)

total_value_simple = getValueState(VT, best_state_simple)
total_size_simple = getSizeState(VT, best_state_simple)

print("Trivial Solution")
print ("[Total Value => ", total_value_trivial, ", Total Size => ", total_size_trivial, ", Best State => ", best_state_trivial)

print("Simple Descent")
print ("[Total Value => ", total_value_simple, ", Total Size => ", total_size_simple, ", Best State => ", best_state_simple)