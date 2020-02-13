statement_one = (2 - 1 > 3) or (-5 * 2 == -10)

statement_two = (9 + 5 <= 15) or (7 != 4 + 3)

def graduation_mailer(gpa, credits):
  if (gpa >= 2.0) or (credits >= 120):
    print("GPA: " + str(gpa))
    print("Credits: " + str(credits))
    print("Will send mailer")
    return True
  else:
    print("GPA: " + str(gpa))
    print("Credits: " + str(credits))
    print("Will not send mailer")
    return False
  
graduation_mailer(1.9,110)
