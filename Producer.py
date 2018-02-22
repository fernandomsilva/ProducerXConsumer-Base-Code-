from global_functions import *
import sys
import random

number_of_consumers = int(sys.argv[1])
current_iteration = 1
last_iteration = 0
number_of_generations = 10

input_filename_prefix = "output_"
input_filename_sufix = ".txt"

log_filename = "log.txt"
eraseFile(log_filename)

output_filename = "test.txt"

results_filename = "gen-output.txt"

total = 0.0

def produce():
	product = random.sample(range(10000), number_of_consumers)
	data_buffer = str(current_iteration) + "\n"
	for i in product:
		data_buffer += str(i) + "\n"
	
	output_file = createFile(output_filename)
	writeToFile(output_file, data_buffer)
	closeFile(output_file)

def compileData():
	result = []
	
	for i in range(number_of_consumers):
		input_file = openFile(input_filename_prefix + str(i) + input_filename_sufix)
		input_data = readFromFile(input_file)
		closeFile(input_file)
		
		result.append(float(input_data[0]))
	
	return result
### MAIN

while True:
	if current_iteration == 1:
		produce()
		last_iteration = current_iteration

	log_file = openFile(log_filename)
	log_data = readFromFile(log_file)
	closeFile(log_file)
	if len(log_data) >= number_of_consumers:
		data = compileData()
		total += sum(data)
		eraseFile(log_filename)

		addToFile(results_filename, str(current_iteration) + "; " + str(total))
		current_iteration += 1
	
	if current_iteration > last_iteration:
		produce()
		last_iteration = current_iteration
	
	if current_iteration >= number_of_generations:
		print total
		break
	#CODE TO SLEEP <---
