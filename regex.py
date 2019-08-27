import re

def main():

	
	card_list = []
	n = int(input())

	for i in range(0, n):
		target = input().strip()
		card_list.append(target)

	for x in card_list:
		status_start = bool(re.match(r"^[4, 5, 6]\d\d\d\-\d\d\d\d\-\d\d\d\d\-\d\d\d\d", x))


		if status_start == True:# and len(x) == 16:
			print("Valid")
		else:
			print("Invalid")


if __name__ == '__main__':
	main()

	#^[4, 5, 6]\d\d\d\-{0,1}\d\d\d\d\-{0,1}\d\d\d\d\-{0,1}\d\d\d\d