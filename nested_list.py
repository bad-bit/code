def main():
	n = int(input().strip())

	name = []
	grades = []

	for i in range(n):
		names = str(input().strip())
		name.append(names)

		marks = int(input().strip())
		grades.append(marks)


	name.sort()
	
	'''#runner up code

	sorted_grades = []

	for i in grades:
		if i not in sorted_grades:
			sorted_grades.append(i)


	sorted_grades.sort(reverse=True)
	runner_up = sorted_grades[1]



	#output
	'''

	print(name)
	print(grades)



if __name__ == '__main__':
	main()