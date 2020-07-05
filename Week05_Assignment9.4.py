name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

d = dict()

for line in handle:
    
    if not line.startswith('From'):continue
    
    line = line.split()
    
    if line[0] == 'From':
        
        line1 =  line[1]
        #print(line1)
        #print(type(line1))
        #print(line1.split())
        for word in line1.split(): #here split method is necessary, 
                                   #it will create a string of list with only line1 variable
                                   #Otherwise the loop will travese on each letter of line1 variable
                                   #but we need the whole mail id not a particular letter
            
            d[word]=d.get(word,0)+1 #make histogram of mail id in the dictionary

#this part wil determine which is the highest/largest in the dictionary
name=None
largeNum=None
for key,value in d.items():
    if largeNum is None or value>largeNum:
        largeNum=value
        name=key
print(name,largeNum)
