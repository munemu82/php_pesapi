import re
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
