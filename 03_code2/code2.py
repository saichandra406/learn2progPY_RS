def printTriangle(size):
    #start with starCount being 0
    starCount = 0

    #count from 0 (inclusive) to size (exclusive), for each number i that you count
    for i in range(size):
        #count from 0 (inclusive) to i (inclusive), for each number j that you count
        for j in range(i+1):
            #print a "*"
            print('*', end='')
            #increment starCount
            starCount += 1
        #when you finish counting on j, 
        #print a newline ("\n")
        print()
    #when you finish counting on i, 
    #your answer is starCount
    return starCount

if __name__ == "__main__":
    print("Here is a triangle with height 4")
    numStars = printTriangle(4)
    print("That triangle had {} total stars".format(numStars))
    #now print "Here is a triangle with height 7\n"
    print("Here is a triangle with height 7")
    #then call printTriangle, passing in 7, and assign the result to numStars
    numStars = printTriangle(7)
    #finally, print "That triangle had %d total stars\n", such that the %d 
    #prints the value of numStars
    print(f"That triangle had {numStars} total stars")
