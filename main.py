import heapq

wires = [4, 3, 2, 6]

heapq.heapify(wires)

print('Initial wires', wires)

cost = 0

while len(wires) > 1:
    print('=======================')
    smallest = heapq.heappop(wires)
    second_smallest = heapq.heappop(wires)

    new_wire = smallest + second_smallest

    cost += new_wire

    print(f'New wire: {smallest} + {second_smallest} = {new_wire}')

    heapq.heappush(wires, new_wire)

    print('Wire state:', wires)
    print('Current cost:', cost)

print('Calculation complete:')
print(f'Cost: {cost}')

