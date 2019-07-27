print("Enter numbers ! Enter 0 to stop")
num = []
c=0
while True:
  num.append(int(input())
  if num[c]==0:
    break
  else:
    c+=1
sum  = 0

if num[0] == 0:
  print("invalid")
else:
  for i in range(len(num)-1):
    sum += num[i]
  print("Average is ",float(sum/count))
