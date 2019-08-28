def main():

	converted = []
	n = int(input())

	target = input().split(" ")

	for i in target:
		converted.append(int(i))
		#print(type(converted))
		#converted.append(to_hash)
	final = tuple(converted)
	hashed = hash(final)

	print(hashed)







if __name__ == '__main__':
	main()