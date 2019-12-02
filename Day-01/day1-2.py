def main(filename):
	# main method to solve the puzzle
	# get input
	input = read_input(filename)
	# initialise final value
	total_fuel = 0
	for value in input:
		module_fuel= module_mass(value)
		while module_fuel > 0:
			total_fuel += module_fuel
			module_fuel = module_mass(module_fuel) if module_mass(module_fuel) >=0 else 0
	return str(total_fuel)
	
def module_mass(data):
	fuel = int(data)//3 - 2
	return fuel
	
def read_input(filename):
	# method to read in the input from the text file
	with open(filename) as file:
		input = file.read()
	split_input = input.split('\n')
	return split_input[:-1]
	
if __name__ == '__main__':
    print(main("input"))