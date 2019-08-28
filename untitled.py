def main():

    n = int(input("").strip())
    d = {}
    sum = 0
    avg = 0
    ans = 0

    for _ in range(n):

        name, p, c, m = input().split(" ")
        d[name] = p, c, m

    target = str(input().strip())

    for name in d:
        if target == name:
            marks = d.get(target)

            for i in marks:
                floated = float(i)
                sum = sum + floated
            
            avg = float(sum / 3)
            final = str(avg)

            length = len(final)

            if length > 5:
            	print('%.5s' % final)
            elif length == 4:
            	print(final+"0")
            elif length == 3:
            	print(final+"0")

    
if __name__ == '__main__':
    main()