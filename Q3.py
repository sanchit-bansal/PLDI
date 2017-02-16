#using python to read an input file 
#and print the largest of them


TextFile = open("int-list-in.txt", "r+")


with open("int-list-in.txt", "r+") as TextFile:
    content = TextFile.readlines()
    content = [x.strip() for x in content] 
    unique=set(content)
    print (unique)
fo = open("unique-out.txt", "rw+")
fo.write("%s\n" % unique)



