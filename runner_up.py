def main():
	
	n = int(input("").strip())
	#if n >= 10 or n <=2:
	#	exit()
	
	arr = list(map(int,input().split()))

	sorted_list = []

	for i in arr:
		if i not in sorted_list:
			sorted_list.append(i)

	sorted_list.sort()
	n = len(sorted_list)
	runner_up = sorted_list[n-2]

	print(runner_up)
	

if __name__ == '__main__':
	main()