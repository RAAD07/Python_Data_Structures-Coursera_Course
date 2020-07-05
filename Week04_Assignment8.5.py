fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0

for line in fh:
    line=line.rstrip() #removes whitespaces at the end of each line
    if not line.startswith('From '):continue #if line does not start with "From" then ignore
    count=count+1 #counts the lines in the file with From as the first word 
    line=line.split() #otherwise split the words where it finds whitespace
    print(line[1]) #take the 2nd part (index1) which contains the mail id

print("There were", count, "lines in the file with From as the first word")
