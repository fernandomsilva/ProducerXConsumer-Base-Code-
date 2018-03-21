from global_functions import *
from config import *
import sys
import os
import random
import time
import uuid

#number_of_consumers = int(sys.argv[1])
current_iteration = 1
last_iteration = 0

current_directory = "data/generation-0/"

input_filename_prefix = "ind-"
input_filename_sufix = ".txt"

#log_filename = "log.txt"
#eraseFile(log_filename)

output_filename = "test.txt"

results_filename = "data/gen-output-" + str(uuid.uuid4()) + ".txt"
temp_file = createFile(results_filename)
closeFile(temp_file)

total = 0.0

start = time.time()

def produce():
	product = random.sample(range(10000), number_of_individuals)
	data_buffer = str(current_iteration) + "\n"
	for i in range(0, len(product)):
		data_buffer += str(product[i])
		if i < len(product) - 1:
			data_buffer += "\n"
	
	output_file = createFile(current_directory + output_filename)
	writeToFile(output_file, data_buffer)
	closeFile(output_file)

def compileData():
	result = []
	
	for i in range(number_of_individuals):
		input_file = openFile(current_directory + input_filename_prefix + str(i) + input_filename_sufix)
		input_data = readLineFromFile(input_file)
		closeFile(input_file)
		
		temp_data = [float(x) for x in input_data]
		average = sum(temp_data) / float(len(temp_data))
		
		result.append(float(average))
	
	return result
### MAIN

if current_iteration == 1:
	current_directory = "data/generation-" + str(current_iteration) + "/"
	if not os.path.exists(current_directory):
		os.makedirs(current_directory)
	produce()
	last_iteration = current_iteration

while True:	
	length_of_data_1 = 0
	length_of_data_2 = 0
	try:
		test_pointer = openFile(current_directory + "ind-" + str(number_of_individuals-1) + ".txt")
		test_data = readLineFromFile(test_pointer)
		closeFile(test_pointer)
		length_of_data_1 = len(test_data)

		test_pointer = openFile(current_directory + "ind-" + str(number_of_individuals-2) + ".txt")
		test_data = readLineFromFile(test_pointer)
		closeFile(test_pointer)
		length_of_data_2 = len(test_data)
	except:
		print ("File", current_directory + "ind-" + str(number_of_individuals-1) + ".txt", " doesn't exist")
		time.sleep(SLEEP_TIME_PRODUCER)
		continue
	
	#if len(log_data) >= number_of_consumers:
	print ("Data len: ", float(length_of_data_1 + length_of_data_2) / 2.0)
	if length_of_data_1 >= number_of_simulations and length_of_data_2 >= number_of_simulations:
		data = compileData()
		total += sum(data)
		#eraseFile(log_filename)

		print("Compiling generation ", current_iteration)
		addToFileWithBreakline(results_filename, str(current_iteration) + "; " + str(total) + "; " + str(time.time() - start) + ";")
		start = time.time()
		current_iteration += 1
	
	if current_iteration >= number_of_generations+1:
		break
	
	if current_iteration > last_iteration:
		print("Making new generation ", current_iteration)
		current_directory = "data/generation-" + str(current_iteration) + "/"
		if not os.path.exists(current_directory):
			os.makedirs(current_directory)
		produce()
		last_iteration = current_iteration
	
	time.sleep(SLEEP_TIME_PRODUCER)
