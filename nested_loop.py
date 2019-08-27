def main():

	n = int(input().strip())

	scorecard = []
	ank = []

	for _ in range(n):
		name = input()
		score = float(input())

		scorecard = scorecard + [[name, score]]
		ank = ank + [score]

	b = sorted(list(set(ank)))[1]

	for a,c in sorted(scorecard):
		if c == b:
			print(a)


if __name__ == '__main__':
	main()



