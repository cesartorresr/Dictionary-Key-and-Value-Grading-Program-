student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades ={}

#TODO-2: Write your code below to add the grades to student_grades.👇

# Diccionarios tienen llaves y valores. Si quieres cambiar el valor es student_scores[key] Si quieres cambiar los key es solo student_scores
for key in student_scores:
  score = student_scores[key]
  if score > 90:
    student_grades[key] = "Oustanding"
  elif score > 80 and score < 91:
    student_grades[key] = "Exceeds Expectations"
  elif score > 70 and score < 80:
    student_grades[key] = "Acceptable"
  else:
    score = "Fail"     

    

# 🚨 Don't change the code below 👇
print(student_grades)





