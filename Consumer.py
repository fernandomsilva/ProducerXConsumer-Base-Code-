from global_functions import *
from config import *
import sys
import time

id = int(sys.argv[1])
current_iteration = 1

current_directory = "data/generation-" + str(current_iteration) + "/"

input_file = "test.txt"
output_file_prefix = "ind-"
output_file_sufix = ".txt"
#output_file = "output_" + str(id) + ".txt"

#log_file = "log.txt"

def functionToRun(param):
	return param ** 2

while True:
	try:
		file_pointer = openFile(current_directory + input_file)
		file_data = readFromFile(file_pointer)
		closeFile(file_pointer)
		temp = int(file_data[0])
	except:
		print ("Failed to open ", current_directory + input_file)
		time.sleep(0.1)
		continue

	length_of_data = 0
	try:
		offset = (id % 2) - 2
		test_pointer = openFile(current_directory + "ind-" + str(number_of_individuals + offset) + ".txt")
		test_data = readLineFromFile(test_pointer)
		length_of_data = len(test_data)
	except:
		pass

	print ("Data len: ", length_of_data)
	if length_of_data < number_of_simulations:
		population = [int(file_data[i]) for i in range(1, len(file_data))]
		
		evaluated_pop = [int(file_data[i+1]) for i in range(0, len(file_data)-1) if (i % 2) == (id % 2)]

		result = list(map(functionToRun, evaluated_pop))

		i = id % 2
		index = 0
		while i < (len(result) * 2):
			addToFile(current_directory + output_file_prefix + str(i) + output_file_sufix, str(result[index]) + ";")
			i += 2
			index += 1
			#addToFile(log_file, "DONE")
		
		time.sleep(5)
		#current_iteration += 1
	else:
		current_iteration += 1
		print ("Start gen ", current_iteration)
		current_directory = "data/generation-" + str(current_iteration) + "/"
		time.sleep(SLEEP_TIME_CONSUMER)
	
	if current_iteration >= number_of_generations+1:
		break
