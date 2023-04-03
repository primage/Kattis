def main():
	first_line = input()
	clearings = int(first_line.split()[0])
	paths = int(first_line.split()[1])
	path_dict = {}
	
	# store clearings and paths to path_dict in the following structure
	# path_dict = {0: [1, 2], 1: [0, 2], 2: [1, 0]}
	for i in range(paths):
		line = input()
		clear1 = int(line.split()[0])
		clear2 = int(line.split()[1])
		if clear1 not in path_dict:
			path_dict[clear1] = [clear2]
		else:
			path_dict[clear1].append(clear2)
		if clear2 not in path_dict:
			path_dict[clear2] = [clear1]
		else:
			path_dict[clear2].append(clear1)
	
	# probability distriution = what is the probability of being in the clearing at step i
	prob_dist = [0]*clearings 
	
	# the starting probability distribution
	prob_dist[0] = 1
	
	N = 10000 # number of steps 
	E = 0	  # expected propability
	
	for i in range(N):
		next_prob_dist = [0]*clearings
		for j in range(clearings):
			for k in path_dict[j]:
				next_prob_dist[k] = next_prob_dist[k] + prob_dist[j]/len(path_dict[j])	
		E = E + next_prob_dist[-1]*(i+1)
		next_prob_dist[-1] = 0 # reset the prob of the exit
		prob_dist = next_prob_dist
	print(E)
	
if __name__ == "__main__":
	main()
