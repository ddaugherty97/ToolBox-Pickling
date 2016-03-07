""" A program that stores and updates a counter using a Python pickle file"""

import os.path
import sys
import pickle 

def update_counter(file_name, reset=False):
	""" Updates a counter stored in the file 'file_name'

		A new counter will be created and initialized to 1 if none exists or if
		the reset flag is True.

		If the counter already exists and reset is False, the counter's value will
		be incremented.

		file_name: the file that stores the counter to be incremented.  If the file
				   doesn't exist, a counter is created and initialized to 1.
		reset: True if the counter in the file should be rest.
		returns: the new counter value

	>>> update_counter('blah.txt',True)
	1
	>>> update_counter('blah.txt')
	2
	>>> update_counter('blah2.txt',True)
	1
	>>> update_counter('blah.txt')
	3
	>>> update_counter('blah2.txt')
	2
	"""

	# Checks to see if the file already exists or if it needs to be reset
	if os.path.exists(file_name) and reset == False:

		# Opens the file for editing
		f = open(file_name, 'r+')
		counter_value = pickle.load(f)

		# Adds one to the counter and stores it back into the file
		counter_value += 1
		f.seek(0,0)
		pickle.dump(counter_value, f)
		f.close()

	else: # File either needs to be reset or it does not already exist

		# Opens a new file and stores a counter with a value of 1 
		f = open(file_name, 'w')
		counter_value = 1
		pickle.dump(counter_value, f)
		f.close()

	# Reads the counter in the file
	final_count = pickle.load(open(file_name, 'r'))
	return final_count

if __name__ == '__main__':
	if len(sys.argv) < 2:
		import doctest
		doctest.testmod()
	else:
		print "new value is " + str(update_counter(sys.argv[1]))