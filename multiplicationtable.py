for i in range(1,11):
  print('%4d' %i, end = '   ')
print(end = '\n')
for i in range(1,11):
  print('%4d' %i, end = '  ')
  for j in range(1,11):
    print('%4d' %( i*j), '  ' , end = '')
  print(end = '\n')
