#statement_one = not (4 + 5 <= 9)

#statement_two = not (8 * 2) != 20 - 4

def graduation_reqs(gpa, credits):
  if (gpa >= 2.0) and (credits >= 120):
    return "You meet the requirements to graduate!"
  elif not (credits >=120) and (gpa >= 2.0):
    return "You do not have enough credits to graduate."
  elif not (gpa >= 2.0) and (credits >= 120):
    return "Your GPA is not high enough to graduate."
  else:
    return "You do not meet either requirement to graduate!"
  
print((graduation_reqs(1.1,110)))
