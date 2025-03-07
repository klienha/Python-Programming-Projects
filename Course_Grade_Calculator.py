#Background
#Given a 2-D list seating, and a sequence of locations, increment the value at each location by one, and modify the seating matrix in-place
def increment_attendance(seating, locations):
	for row,col in locations:
		seating[row][col] += 1
#Given a 2-D list of scores, and a list containing the number of low scores to drop (drop_number), remove the corresponding lowest scores from each row
def drop_lowest(scores, drop_num):
	for i in range(len(scores)):
		for j in range(drop_num[i]):
			min_idx = None
			for k in range(len(scores[i])):
				if min_idx is None or scores[i][k] < scores[i][min_idx]:
					min_idx = k
			del scores[i][min_idx]
#Create and return a dictionary where each key is one of the assignment types, and each value is a list of the percentage grades in that assignment type
def organize_grades(grades, assignment_types,max_possible):
	# zy, lab, PA, mid, final
	gbook = {"zy":list(), "lab":list(), "pa":list(), "mid1":list(), "mid2":list(), "final":list()}
	for i in range(len(grades)):
		gbook[assignment_types[i]].append(grades[i]/max_possible[i])
	return gbook
#Given a dictionary gbook containing assignment types (strings) as keys, and lists of grades (numbers) as values, return a new dictionary with the same keys, and with the average of each list of grades for the given key.
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
#Given a dictionary gbook containing assignment types (strings) as keys with the average grade for that assignment type as the value, a dictionary weights with assignment types as keys and the course grade weights for each assignment type, and a dictionary replace where both keys and values are assignment types and represents
#whether a given assignment type (key) should replace an assignment type with a lower
#value (value), return a floating point number representing the final course grade,
#computed by combining the assignment averages with their corresponding weights, and
#replacing grades where appropriate.
def course_grade(gbook, weights, replace):
	#first replace if higher
	for rep_with, rep_from in replace.items():
		if gbook[rep_from] < gbook[rep_with]:
			gbook[rep_from] = gbook[rep_with]
	avg = 0.0
	for k in weights.keys():
		avg += gbook[k]*weights[k]
	return avg
