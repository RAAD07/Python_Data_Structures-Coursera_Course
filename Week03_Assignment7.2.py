# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
total=0.0
count=0
for line in fh:
    #this if condition will ignore those lines that do not start with the word "From"
    if not line.startswith("X-DSPAM-Confidence:") : continue 
    
    line1=line.find('0') #this method will find the index where O exists
    line2=line[line1:] #take that part which starts from 0 and continue to the last indext
    line2=float(line2) #converting to floats
    total=float(total+line2) #counting total/sum
    count=count+1 #total number of element is counted
average=total/count
print('Average spam confidence:',average)