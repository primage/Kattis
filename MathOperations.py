def main():

	case = int(input())
	sets = [input() for _ in range(case)]

	for s in sets:
		counter = 0

		# split to indiv number
		abc_str = s.split()
		
		# convert str to int
		abc = list(map(int, abc_str))

		# sort the list from min to max
		abc.sort()

		# check if at least one of the operations is possible
		if (abc[0] + abc[1] == abc[2]):
			print('Possible')
			continue
		elif (abc[2] - abc[1] == abc[0]):
			print('Possible')
			continue
		elif (abc[0] * abc[1] == abc[2]):
			print('Possible')
			continue
		elif (abc[2] / abc[1] == abc[0]):
			print('Possible')
			continue
		else: print('Impossible')		
			
if __name__ == "__main__":
	main()
