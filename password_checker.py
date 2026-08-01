password = input("Enter password:")
score=0

#Condition
if len(password) >= 8:
  score += 1

if any(char.isupper() for char in password):
  score += 1

if any(char.islower() for char in password):
  score += 1

if any(char.isdidgit() for char in password):
  score += 1

if any(char in "!@#$%^&*"  for char in password):
  score += 1

# Result
if score == 5:
    print("Strong Password")
elif score >= 3:
    print("Moderate Password")
else:
    print("Weak Password")
