print("Enter the bits")
bits  = input()
ones = bits.count('1')
if ones%2 == 0:
  print("Even parity")

else:
  print("Odd parity")
