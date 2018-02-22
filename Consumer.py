from global_functions import *
import sys

LIMIT_OF_INDIVIDUALS = 100

id = (int(sys.argv[1]) % LIMIT_OF_INDIVIDUALS)
current_iteration = 0

input_file = "test.txt"
output_file = "output_" + str(id) + ".txt"

log_file = "log.txt"

def functionToRun(param):
	return param ** 2

while True:
	file_pointer = openFile(input_file)
	file_data = readFromFile(file_pointer)
	closeFile(file_pointer)
	temp = int(file_data[0])
	print temp
	print current_iteration

	if temp > current_iteration:
		current_iteration = temp
		individual = int(file_data[id + 1])

		result = functionToRun(individual)

		file_pointer = createFile(output_file)
		writeToFile(file_pointer, str(result))
		closeFile(file_pointer)

		addToFile(log_file, "DONE")
		
		current_iteration += 1
	else:
		pass
		#CODE TO SLEEP <---