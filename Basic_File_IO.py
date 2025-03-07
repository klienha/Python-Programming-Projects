#PA8solution
def read_grades_file(filename, project=False):
	rv = dict()
	with open(filename) as f:
		lines = f.readlines()
		multi_items = (('pa',9), ('lab',11), ('zy',15))
		rv['name'] = lines[0].split(',')[1].strip()		
		for i in range(len(multi_items)):
			rv[multi_items[i][0]] = lines[i+1].split(',')[1:]
		rv['mid1'] = float(lines[-3].split(',')[1].strip())
		rv['mid2'] = float(lines[-2].split(',')[1].strip())
		rv['final'] = float(lines[-1].split(',')[1].strip())
		for k,num in multi_items:
			old_list = rv[k]
			new_list = list()
			for v in old_list:
				new_list.append(float(v))
			if project and len(new_list)<num:
				avg = sum(new_list)/len(new_list)
				for i in range(num-len(new_list)):
					new_list.append(avg)
			rv[k] = new_list
	return rv

def write_grades_file(filename, gbook):
	with open(filename,'w') as f:
		f.write('name, '+gbook['name']+'\n')
		multi_items = ('pa', 'lab', 'zy')
		for v in multi_items:
			f.write(v)
			for vv in gbook[v]:
				f.write(', '+str(vv))
			f.write('\n')
		f.write(f'mid1, {gbook["mid1"]}\n')
		f.write(f'mid2, {gbook["mid2"]}\n')
		f.write(f'final, {gbook["final"]}')