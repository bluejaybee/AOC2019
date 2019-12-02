def main(filename):
	# main method to solve the puzzle
	# get input
	input = read_input(filename)
	# initialise final value
	total_fuel = 0
	for value in input:
		fuel = int(value)//3 - 2
		total_fuel += fuel
	return str(total_fuel)
	
def read_input(filename):
	# method to read in the input from the text file
	with open(filename) as file:
		input = file.read()
	split_input = input.split('\n')
	return split_input[:-1]
	
if __name__ == '__main__':
    print(main("input"))