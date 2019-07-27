n = int(input("Enter the number to check"))
fac = 2

while fac<=n:
  if n%fac == 0:
    print(fac)
    n = n/fac
  else:
    fac+=1

    
