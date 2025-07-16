"""
Calculate the average waiting time given a list of positions.
The function simulates the movement between positions and calculates the
total waiting time, then returns the average waiting time.
Parameters:
positions (list of int): A list of integer positions.
Returns:
float: The average waiting time.
"""


def average_waiting_time(positions):
    current_pos = 0
    total_time = 0
    relative_time = 0

    for next_pos in positions:
        travel_time = abs(current_pos - next_pos)
        relative_time += travel_time
        total_time += relative_time
        current_pos = next_pos

    return total_time / len(positions)


"""
Calculate and compare the average waiting times for different orderings of positions.
This function takes a list of positions and computes the average waiting time for three different orderings:
1. Sorted positions.
2. Positions sorted by their distance to zero (nearest neighbor).
3. The original order of positions.
Args:
    positions (list): A list of numerical positions.
Returns:
    dict: A dictionary containing the average waiting times for the three orderings with keys:
        - "sorted_waiting_time": Average waiting time for sorted positions.
        - "nearest_neighbor_waiting_time": Average waiting time for positions sorted by nearest neighbor.
        - "optimal_proposed_waiting_time": Average waiting time for the original order of positions.
"""


def ex2func(positions):
    sorted_positions = sorted(positions)
    sorted_waiting_time = average_waiting_time(sorted_positions)

    nearest_neighbor_positions = sorted(positions, key=lambda x: abs(x))
    nearest_neighbor_waiting_time = average_waiting_time(nearest_neighbor_positions)

    optimal_proposed_waiting_time = average_waiting_time(positions)

    return {
        "sorted_waiting_time": sorted_waiting_time,
        "nearest_neighbor_waiting_time": nearest_neighbor_waiting_time,
        "optimal_proposed_waiting_time": optimal_proposed_waiting_time,
    }


"""
Given a list of house positions, this function sorts the positions and
returns a cleaning order. The cleaning order is such that all negative
positions (representing houses to the left of the starting point) are
visited in reverse order first, followed by all non-negative positions
(representing houses to the right of the starting point) in ascending order.
Parameters:
house_positions (list of int): A list of integers representing the positions
                                of houses along a street.
Returns:
list of int: A list of integers representing the order in which the houses
                should be cleaned.
"""


def parcours(house_positions):
    sorted_positions = sorted(house_positions)

    negatives = [pos for pos in sorted_positions if pos < 0]
    positives = [pos for pos in sorted_positions if pos >= 0]

    cleaning_order = negatives[::-1] + positives

    return cleaning_order


"""
Sorts a list of integers based on a custom traversal algorithm.
The function takes a list of integers, sorts it, and then traverses the sorted list
to create a new list based on the following rules:
- Start with the smallest absolute value in the list.
- At each step, choose the next closest integer (either the previous or next in the sorted list)
    based on the absolute difference from the current integer.
- Continue until all elements have been traversed and added to the final list.
Args:
    gL (list of int): The input list of integers to be sorted and traversed.
Returns:
    list of int: The final list of integers after traversal.
"""


def parcoursOnSQR(gL):
    l = sorted(gL.copy())
    currentIndex = l.index(min(l, key=lambda x: (abs(x), -x)))
    currentVar = l[currentIndex]
    finalList = [currentVar]
    nextVar = 2147483647
    precedVar = -2147483648

    while len(l) > 1:
        if currentIndex + 1 < len(l):
            nextVar = l[currentIndex + 1]
            if currentIndex > 0:
                precedVar = l[currentIndex - 1]
                if abs(precedVar - currentVar) < abs(nextVar - currentVar):
                    currentVar = precedVar
                    l.pop(currentIndex)
                    currentIndex = currentIndex - 1
                else:
                    currentVar = nextVar
                    l.pop(currentIndex)
                    currentIndex = currentIndex
            else:
                currentVar = nextVar
                l.pop(currentIndex)
                currentIndex = currentIndex
        else:
            currentVar = precedVar
            l.pop(currentIndex)
            currentIndex = currentIndex - 1
        finalList.append(l[currentIndex])
    return finalList
