def main():
	input_lines = []
	nbox = []
	npea = []
	list_box_list = []
	list_pea_list = []
	box = True
	temp = []
	while True:
		a = input()
		if len(a) == 1:
			if box:
				if a == '0':
					list_pea_list.append(temp)
					break
				else:
					box = False
					list_pea_list.append(temp)
					temp = []	
					nbox.append(a)
					input_lines.append(a)		
			else: 
				box = True
				list_box_list.append(temp)
				temp = []
				npea.append(a)
				input_lines.append(a)
		else:
			data = a.split()
			data_dict = {}
			print(len(data))
			if len(data) == 5:
				data_dict = {'x1': float(data[0]), 'y1': float(data[1]), 'x2': float(data[2]), 'y2': float(data[3]), 'size': data[4]}
			else:
				data_dict = {'x': float(data[0]), 'y': float(data[1]), 'size': data[2]}
				
			temp.append(data_dict)
			input_lines.append(a)
	print(list_box_list)
	list_pea_list = list_pea_list[1:]
	
	for box_list, pea_list in zip(list_box_list, list_pea_list):
		for p in pea_list:
			in_box = False
			for b in box_list:
				if ( p['x']>=b['x1'] and p['x']<=b['x2'] and p['y']>=b['y1'] and p['y']<=b['y2'] ): 
					in_box = True
					if p['size'] == b['size'] :
						print(p['size'], 'correct')
						break
					else: 
						print(p['size'], b['size'])
						break
			if not in_box: 
				print(p['size'], 'floor')
		print('')
	
	
if __name__ == "__main__":
	main()
