import numpy as np

positions_list = [
    [-1.5, 1.2, 2.3, 5.0],
    [5, -1.5, 2.3, 1.2],
    [-15, 7, -6, -13],
    [-13, -15, -6, 7],
]

positions_list_b = [[-3, 9.5, -6.2, 2], [9.5, -3, 2, -6.2]]

positions_example = [1, -2, -5, 4, 6]


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


def parcours(house_positions):
    sorted_positions = sorted(house_positions)

    negatives = [pos for pos in sorted_positions if pos < 0]
    positives = [pos for pos in sorted_positions if pos >= 0]

    cleaning_order = negatives[::-1] + positives

    return cleaning_order


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


print("Exercise 1a:")

for positions in positions_list:
    print(
        f"Positions: {positions}, Average waiting time: {average_waiting_time(positions)} seconds"
    )

print("\nExercise 1b:")
for positions in positions_list_b:
    print(
        f"Positions: {positions}, Average waiting time: {average_waiting_time(positions)} seconds"
    )

print("\nExercise 2:")
results = ex2func(positions_example)
print(f"Temps d'attente moyen (Ordre Trié): {results['sorted_waiting_time']} secondes")
print(
    f"Temps d'attente moyen (Ordre Voisin le Plus Proche): {results['nearest_neighbor_waiting_time']} secondes"
)
print(
    f"Temps d'attente moyen (Ordre Optimal Proposé): {results['optimal_proposed_waiting_time']} secondes"
)

print("\nExercise 3:")
meanArrayParcours = []
meanArrayParcoursOnSQR = []

for _ in range(1000):
    generatedArray = np.random.randint(-1000, 1000, 1000)
    meanArrayParcours.append(average_waiting_time(parcours(generatedArray)))
    meanArrayParcoursOnSQR.append(average_waiting_time(parcoursOnSQR(generatedArray)))

print(f"Cleaning order: {np.mean(meanArrayParcours)}")
print(f"Cleaning order: {np.mean(meanArrayParcoursOnSQR)}")
