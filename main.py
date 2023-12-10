from greedy import pcmax_greedy
from genetic import pcmax_genetic

# open the instance from file
filename = "instances/" + input("Enter filename: ")

file = open(filename, "r")
content = file.read().split()
numbers = [int(i) for i in content]

# first value is the number of processors
processors = numbers[0]
# processes length start from 2nd index
processes = numbers[2:]

greedy_result = pcmax_greedy(processes, processors)
genetic_result = pcmax_genetic(processors, processes)

print(f"Greedy algorithm time: {greedy_result}\nGenetic algorithm time: {genetic_result}")