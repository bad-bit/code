def main():

	data = []
	n = int(input().strip())

	for i in range(n):
		x = input().split(" ")
		cmd = x[0]

		if cmd == "append":
			data.append(int(x[1]))
		if cmd == "print":
			print(data)
		if cmd == "insert":
			data.insert(int(x[1]), int(x[2]))
		if cmd == "reverse":
			data = data[::-1]
		if cmd == "pop":
			data = data.pop()
		if cmd == "sort":
			data = sorted(data)
		if cmd == "remove":
			data.remove(int(x[1]))



if __name__ == '__main__':
	main()