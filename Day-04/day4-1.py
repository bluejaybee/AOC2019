def parse_input(filename):
	with open(filename) as file:
		print('hello!!!!')
		string_input = file.read()
		print(string_input)
	list_input =  string_input.split('-')
	print(list_input)
	return list_input
	
def has_matching_adjacent_digits(password):
	password = str(password)
	for i in range(0,len(password)-1):
		if password[i] == password[i+1]:
			return True
	return False

def has_increasing_digits(password):
	password = str(password)
	for i in range(0, len(password)-1):
		if password[i+1]<password[i]:
			return False
	return True
	
def main(range_one, range_two):
	count = 0
	range_one = int(range_one)
	range_two = int(range_two)
	for i in range(range_one, range_two):
		if has_matching_adjacent_digits(i) and has_increasing_digits(i):	
			count +=1
	print(count)
	
if __name__ == '__main__':
	puzzle_input = parse_input('input.txt')
	main(puzzle_input[0], puzzle_input[1])
	
		