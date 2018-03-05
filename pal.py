def palindrome(s):
  length=len(s) 
  print(s)
  if(length<=1):
    return True
  #elif(length==2):
  elif(s[0]==s[-1]):
      return True
  elif(s[0]==s[1]):
    #print(s)
   palindrome(s[1:-1])
  else:
    return False
print(palindrome('sssasss'))