fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    line = line.rstrip() #removes the whitespaces after each line
    line=line.split() #split the line into a list of words using the split() method
    for word in line: #if the word already exists ignore
        if word not in lst: #if the word does not already in the list
            
            lst.append(word) #include the word
            
lst.sort() #sorting the list in ascending order

print(lst)