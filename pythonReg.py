import re

example = 'Trans. ID: 313821006060 You have sent 20GHS to 233261234567.  Your available balance is 250.67GHS.'
print re.split(r'\s*','Here are some words') # split words by spaces
print re.split(r'[a-fA-F]', ';dsfgjdsklgjdskgf;lWKDFJ',re.I|re.M)
#checking if certain characters are next to each other in the range e.g. a to f
print re.split(r'[a-f][a0f]', ';ahkjhkjshfa;lWKDFJdffd,ffdfdfa',re.I|re.M)
#search for specific address containing number and street e.g. st
#1 find only numbers
print re.findall(r'\d', 'here is the address324 main st.advnice')  # this prints  a list ['3','2','4']
#2 find only numbers in a specific range
print re.findall(r'\d{1,5}', 'here is the address324 main st.advnice')  # this for the range of 1 to 5 digits
#3 find words after a number 
print re.findall(r'\d{1,5}\s\w+', 'here is the address324 main st.advnice') #this prints ['324 main']
#3 find words after a number then a space followed by street name(or some words) which normally ends with period (.) 
print re.findall(r'\d{1,5}\s\w+\s\w+\.', 'here is the address324 main st.advnice') #this prints ['324 main']
print re.findall("\d+\.\d+", example)  # This matches the money type with decimal places for GHS
print re.findall("\d+\.\d+[A-Z]{3}", example)  # This matches the money type with decimal places for GHS
print re.findall("\d+", example)		#this matches only integers
print re.findall("\s\d+[A-Z]{3}", example)		#this matches money that do not have decimal places for GHS
print re.findall("[A-z]{5}\.\s[A-Z]{2}\:\s\d+", example)  #match Ghana transaction number
print re.findall("[A-z]{2}\s\d{12}\.", example)  #match Ghana sent to customer number

print re.findall("\d+\.\d+[A-Z]{3}|\d+[A-Z]{3}", example, re.I)
print re.findall("[a-z]{2}\s\d{12}\.", example)  #match Ghana reciever account number
#function to extract transaction number only
def extractTransactionNo(str):
	transactionNo = re.findall("[A-z]{5}\.\s[A-Z]{2}\:\s\d+",str)
	transactionNo = re.findall("\d{12}",transactionNo[0])
	transactionNo = transactionNo[0]
	print transactionNo
    return
#function to extract amount sent
def extractAmountSent(str):
	allMoneyInString = re.findall("\d+\.\d+[A-Z]{3}|\d+[A-Z]{3}", example, re.I)
	actualSentAmount = allMoneyInString[0]
	print actualSentAmount
    return

#function to extract account number
def extractRecieverAccount(str):
	stringExact = re.findall("[a-z]{2}\s\d{12}\.", str)
	accountNo = transactionNo = re.findall("\d{12}",stringExact[0])
	accountNo = accountNo[0]
	print accountNo
    return
#Function to exact available balance#function to extract account number
def extractAvailableBal(str):
	allMoneys = re.findall("\d+\.\d+[A-Z]{3}|\d+[A-Z]{3}", str, re.I)= 
	currentBal = transactionNo = re.findall("\d{12}",allMoneys[0])
	currentBal = currentBal[1]
	print currentBal
    return
#call my function
extractTransactionNo(example)
extractAmountSent(example)
extractRecieverAccount(example)
extractAvailableBal(example)

