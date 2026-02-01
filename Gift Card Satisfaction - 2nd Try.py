# https://datalemur.com/questions/python-gift-card-satisfaction

def max_satisfaction(expectations, cards):
  expectations.sort()
  cards.sort()
  
  exp_no = 0
  sat = 0
  for i in cards:
    if expectations[exp_no] <= i:
      sat += 1
      exp_no += 1
    if exp_no == len(expectations):
      break
  return sat
