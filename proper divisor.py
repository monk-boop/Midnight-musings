def prodiv(n):
  return {x for x in range(1,(n+1//2)) if n%x == 0 and n!= x}

num = [prodiv(48)]

print(num)
