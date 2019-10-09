import re


line = "Bs 7ae 45 sm8 # than 98794 8you 757"; 
 
 
#matches only digits in a string
matchObj = re.search( r'[\d]+', 'abc123xyz')
print ('Example 11 is', matchObj.group())
 
# create an empty list
listOfString = []
 
# Select the target pattern
# Starts with a digit followed by letter
pattern = re.compile(r'[\d][A-Za-z]+')
 
matches = pattern.finditer(line)
 
# iterate through the line to extract strings
# that start with a digit followed by letters
# See example of enumeration
 
for k,mat in enumerate (matches):
 
   # Store the desired strings in a list
   listOfString.append(mat.group())
   print ('The',k, 'pattern is:', mat.group())
 
# Print the list of strings
print (listOfString)
