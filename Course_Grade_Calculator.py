# PA5solution.py

def increment_attendance(seating, locations):
	for row,col in locations:
		seating[row][col] += 1

def drop_lowest(scores, drop_num):
	for i in range(len(scores)):
		for j in range(drop_num[i]):
			min_idx = None
			for k in range(len(scores[i])):
				if min_idx is None or scores[i][k] < scores[i][min_idx]:
					min_idx = k
			del scores[i][min_idx]

def organize_grades(grades, assignment_types,max_possible):
	# zy, lab, PA, mid, final
	gbook = {"zy":list(), "lab":list(), "pa":list(), "mid1":list(), "mid2":list(), "final":list()}
	for i in range(len(grades)):
		gbook[assignment_types[i]].append(grades[i]/max_possible[i])
	return gbook

def gbook_averages(gbook):
	rv = dict()
	for assignment_type,grade_list in gbook.items():
		avg = 0.0
		for grade in grade_list:
			avg += grade
		if len(grade_list) > 0:
			avg = avg/len(grade_list)
		rv[assignment_type] = avg
	return rv

def course_grade(gbook, weights, replace):
	#first replace if higher
	for rep_with, rep_from in replace.items():
		if gbook[rep_from] < gbook[rep_with]:
			gbook[rep_from] = gbook[rep_with]
	avg = 0.0
	for k in weights.keys():
		avg += gbook[k]*weights[k]
	return avg