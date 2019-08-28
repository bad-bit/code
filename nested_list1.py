def main():

	n = int(input().strip())

	dictionary = dict(input().split() for _ in range(n))
	print(dictionary)

	print(sorted(dictionary))

if __name__ == '__main__':
	main()