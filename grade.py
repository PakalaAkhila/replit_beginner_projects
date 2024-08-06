print("Grade Generator ;)")
print()
test = input("What is the name of the test? ")
max = int(input("What is the maximum score? "))
if max < 0:
  print("You can't have a negative maximum score!")
  exit()
elif max >=90 and max <=100:
  print("You got an A+ \u001b[32m🤩\u001b[0m")
elif max >=80 and max <=89:
  print("You got an A \u001b[33m  😁 \u001b[0m")
elif max >=70 and max <=79:
  print("You got a B \u001b[32m🥳\u001b[0m")
elif max >=60 and max <=69:
  print("You got a C \u001b[32m 😁\u001b[0m")
elif max >=50 and max <=59:
  print("You got a D \u001b[32m😎\u001b[0m")
elif max >=0 and max <=49:
  print("You got a U \u001b[32m🙂\u001b[0m")
