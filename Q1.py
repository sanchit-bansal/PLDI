#using python to read an input file 
#and print the largest of them


TextFile = open("int-list-in.txt", "r+")


with open("int-list-in.txt", "r+") as TextFile:
    content = TextFile.readlines()
    content = [x.strip() for x in content] 
    newcontent = map(int, content)
    n=int(newcontent[0])
    largest=newcontent[1]
    for i in range(1,n):
	    some= newcontent[i]
	    if(some>largest):
	    	largest=some
fo = open("factorial-out.txt", "rw+")
fo.write(str(largest))


