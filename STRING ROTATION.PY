def checkRotation(s1, s2): 
    temp = '' 
  
    # Check if lengths of two strings are equal or not 
    if len(s1) != len(s2): 
        return False
  
    # storing concatenated string 
    temp = s1 + s1 
  
    
    if s2 in temp: 
        return True 
    else: 
        return False
   
string1 = "HELLO"
string2 = "LOHEL"
  
if checkRotation(string1, string2): 
    print("Given Strings are rotations of each other.")
else: 
    print("Given Strings are not rotations of each other.")