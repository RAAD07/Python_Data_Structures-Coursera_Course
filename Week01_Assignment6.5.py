text = "X-DSPAM-Confidence:    0.8475"
indexNum=text.find('0') #this method will find the index where O exists
newStr=float(text[indexNum:]) #converting to floating number
print(newStr)