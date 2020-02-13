def greater_than(x,y):
  if x > y:
    return x
  if x < y:
    return y
  else:
      return "These numbers are the same"

def graduation_reqs(credits):
  if credits >= 120:
    print("You have enough credits to graduate!")
    return "You have enough credits to graduate!"
  else:
    print("You do not have enough credits to graduate")
    return "You do not have enough credits to graduate!"
  
graduation_reqs(120)
