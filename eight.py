import string 
def check_pangram(str1): 
alphabet = "abcdefghijklmnopqrstuvwxyz"
for char in alphabet: 
if char not in str1.lower(): 
return False
return True
# Driver code 
str1 = 'the quick brown fox jumps over the lazy dog'
if(check_pangram(str1) == True): 
print("The String is a Pangram String.") 
else: 
print("The String is not a Pangram String.") 
