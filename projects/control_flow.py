#gpa must be 3.0 or above.
#ps_core = Personal Statement score, must be 90 or above.
#ec_count = Extracurricular Activites, must be 3 or higher but if gpa and ps_score are met, recommend in-person interview.
 
  
def applicant_selector(gpa, ps_score, ec_count):
  if gpa >= 3.0 and ps_score >= 90 and ec_count >= 3:
    return "This applicant should be accepted."
  if gpa >= 3.0 and ps_score >= 90 and ec_count <= 3:
    return "This applicant should be given an in-person interview."
  else:
    return "This applicant should be rejected."
  

print(applicant_selector(3.0,90,2))
