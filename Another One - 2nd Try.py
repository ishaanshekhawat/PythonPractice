def another_one(digits):
  num = 0
  
  ct = 0
  
  for i in digits[::-1]:
    num += i*10**ct 
    ct += 1
  
  print(num)
  
  num += 1
  res = []
  while num / 10 != 0:
    res.append(num%10)
    num //= 10
    
  return res[::-1]
