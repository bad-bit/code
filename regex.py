import re

def main():

	
	card_list = []
	n = int(input())

	for i in range(0, n):
		target = input().strip()
		card_list.append(target)

	for x in card_list:
		status_start = bool(re.match(r"^[4, 5, 6]\d{3}\-{0,1}\d{4}\-{0,1}\d{4}\-{0,1}\d{4}$", x) and not re.search(r"([\d])\1\1\1", x.replace("-", "")))
		#more readable version of the regex:
		#	^[4, 5, 6]\d\d\d\-{0,1}\d\d\d\d\-{0,1}\d\d\d\d\-{0,1}\d\d\d\d

		if status_start == True:
			print("Valid")
		else:
			print("Invalid")

if __name__ == '__main__':
	main()

	

	#fail
	#^[4, 5, 6]\d\d\d\-\d\d\d\d\-\d\d\d\d\-\d\d\d\d
