num = []
c=0
while True:
  num.append(int(input()))
  if num[c]==0:
    break
  else:
    c+=1

num = num[:-1]
print(sorted(num,reverse = False))
