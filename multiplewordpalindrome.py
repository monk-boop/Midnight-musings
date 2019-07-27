
strr = input("Enter the String: ").replace(" ","")

for i in range(len(strr)//2): # all args of range must be int. //returns an int value after division
  if strr[i] != strr[len(strr)-i-1]:
    print("string is not a palindrome")
    break

  else:
    print("It's a palindrome all righty!")
