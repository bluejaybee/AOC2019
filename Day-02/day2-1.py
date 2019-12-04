def parse_input(filename):
	with open(filename) as file:
		string_input = file.read()
	list_input = string_input.split(',')
	return list_input
	
def main(puzzle_input):
	puzzle_input[1] = 12
	puzzle_input[2] = 2
	starting_index = 0
	opcode_1 = int(puzzle_input[0])
	while opcode_1 != 99:
		first_index = int(puzzle_input[starting_index+1])
		second_index = int(puzzle_input[starting_index+2])
		if opcode_1 == 1:
			answer = int(puzzle_input[first_index]) + int(puzzle_input[second_index])
		elif opcode_1 == 2:
			answer = int(puzzle_input[first_index]) * int(puzzle_input[second_index])
		third_index = int(puzzle_input[starting_index+3])
		puzzle_input[third_index] = answer
		starting_index += 4
		opcode_1 = int(puzzle_input[starting_index])
	print(puzzle_input)
	print(puzzle_input[0])
	

if __name__ == '__main__':
	input = parse_input('input.txt')
	main(input)
			
			
		