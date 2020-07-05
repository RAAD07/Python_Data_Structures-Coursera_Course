name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
dic=dict()
for line in handle:
    #line=line.rstrip() #this line can be used or omitted; no harm on that
    if not line.startswith('From'):continue
    words=line.split()
    if words[0]=='From':
        neededword=words[5] #index 5 contains the time
        neededpart=neededword.split(':') #then split that time based on colon sign
        part1=neededpart[0] #take the hours part only
        
        for w in part1.split():    #here split method is necessary, 
                                   #it will create a list of strings with only part1 variable
                                   #Otherwise the loop will travese on each letter/number of part1 variable
                                   #but we need the whole hours part not a particular letter/number
            dic[w]=dic.get(w,0)+1  #make histogram based on the hours part

for k,v in sorted(dic.items()): #sorting the hours based on key not value
                                #cz key is the hour and value is the number of times it appears
    print(k,v)
