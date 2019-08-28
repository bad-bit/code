import decimal

def main():

    n = int(input("").strip())
    d = {}
    #d2 = {}
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
            #print(marks)
            for i in marks:
                floated = float(i)
                sum = sum + floated
            
            avg = float(sum / 3)
            final = str(avg)

            length = len(final)
            #print(final)

            if length > 5:
            	print('%.5s' % final)
            elif length == 4:
            	print(final+"0")
            elif length == 3:
            	print(final+"0")

            #if final.endswith(".0"):
             #   print(final+"0")
            #else:
                #ans = float(round(avg, 3))
             #   print(final+"0")


            #

            #if final.endswith(".0"):
            #    print(final+"0")
            #else:
            #    print(final)


        #    print(ans)
    #            print(floated)
    #            avg = floated / 3
    #            print(floated)
        


    #print(d)'''
    
if __name__ == '__main__':
    main()