def parse_input(filename):
	with open(filename) as file:
		string_input = file.read()
	list_input =  string_input.split('-')
	return list_input
	
def has_matching_adjacent_digits(password):
	password = str(password)
	length = len(password)
	count = 1
	list = []
	for i in range(0,len(password)-1):
		if password[i] == password[i+1]:
			count += 1
			if i == len(password)-2:
				list.append(count)
		else:
			list.append(count)
			count = 1
	if 2 in list:
		return True
	else:
		return False
	
def has_increasing_digits(password):
	password = str(password)
	for i in range(0, len(password)-1):
		if password[i+1]< password[i]:
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
	
		