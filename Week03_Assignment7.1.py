# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    line1=line.rstrip() #removes the whitespaces after each line
    line2=line1.upper() #we need to turn the alphabets into upper cases
    print(line2)