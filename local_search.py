import numpy as np

# Function to calculate objective func 
def objective(s_vec):
    coeffs = np.array([8, 11, 9, 12, 14, 10, 6, 7, 13])
    return np.sum(coeffs * s_vec)

# function to check if given solution obeys the problem constraints
def constraint(s_vec):
    # Sum must be less than equal to 16
    coeffs = np.array([1,2,3,2,3,4,1,5,3])
    constrain_1 = np.sum(coeffs * s_vec) <= 16
    # Numbers must be binary
    constrain_2 = np.array_equal(s_vec, s_vec.astype(bool))
    return constrain_1 and constrain_2  

# Function to generate all possible neighbors for given solution
def neighbors(s_vec):
    n_list = [] #Initialise empty list
    for i in range(len(s_vec)): # 9 possible neighbors because 9 elements in the solution 
        copy = s_vec.copy()
        #Bit-flip the ith element
        if s_vec[i] == 0:
            copy[i] = 1
        else:
            copy[i] = 0
        if constraint(copy): # Only add valid solutions to list
            n_list.append(copy)
    return n_list

#Function to perform local search
def search(s_i):
    max_s = s_i # Set max solution to initial solution
    max_obj = objective(s_i) # get its objective function
    end = False # set end flag to false
    count = 0 # set count to zero
    while not end:
        count += 1
        neighbors_ = neighbors(max_s) # Get neighbours of max solution
        neigbor_max_obj = objective(neighbors_[0]) # get objective function of first neighbour
        neighbor_max = neighbors_[0] # set first neighbour as max solution
        for neighbor in neighbors_: # Go through all neighbours and find best neighbour
            if objective(neighbor) > neigbor_max_obj: #Check if objective function is better
                neighbor_max = neighbor # if better, set as max neighbour solution
                neigbor_max_obj = objective(neighbor)
        if neigbor_max_obj > max_obj: # check if best neighbour is better than best solution
            max_s = neighbor_max # if better, set as max solution
            max_obj = neigbor_max_obj
        else:
            end = True # if not, end the search
        for n in neighbors_:
            print(count,'Neighbour: ',n, 'Objective Function',objective(n))
    return max_obj,max_s

s_1 = np.array([0, 1, 1, 1, 0, 0, 1, 1, 1])
s_2 = np.array([0, 1, 0, 1, 0, 0, 0, 1, 0])
print(f'for s1 = {s_1}')
print('Best Objective Function and Solution',search(s_1))
print(f'for s2 = {s_2}')
print('Best Objective Function and Solution',search(s_2))



