import re

def main():

	card_list = []

	n = int(input())

	for i in range(0, n):
		target = input().strip()
		card_list.append(target)


	for x in card_list:
		#status = bool(re.findall(r"^a", x))
		
		if status == True and len(x) == 16:
			print("Valid")
		else:
			print("Invalid")

if __name__ == '__main__':
	main()