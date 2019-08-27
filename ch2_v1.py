n = int(input().strip())

dicti = {True: "Not Weird", False: "Weird"}

print(dicti[
	n%2 == 0 and (n in range(2, 6) or n > 20)])