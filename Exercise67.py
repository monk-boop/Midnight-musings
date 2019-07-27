age = []
c = 0
while True:
  print("Enter age")
  age.append(int(input()))
  if age[c] == 0:
    break
  else:
    c+=1
cost  =0  
for i in range(len(age) - 1):
  if age[i]>3 and age[i]<30:
    cost = cost+12
  elif age[i]>29 and age[i]<80:
    cost = cost+15
  else:
    continue
print("Total cost is ", cost)






