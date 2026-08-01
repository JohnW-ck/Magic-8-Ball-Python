
import random

name = input("Please enter a name:" )
first_question = input("And please enter a question: ")

answer2 = "I'd love to tell your fortune!"

if name and first_question:
  print(name, "asks", first_question)
  print(answer2)

random_number = random.randint(1, 9)

if random_number == 1:
  answer = ("Yes - definitely")
elif random_number == 2:
  answer = ("It is decidedly so")
elif random_number == 3:
  answer = ("Without a doubt")
elif random_number == 4: 
  answer = ("Reply hazy, try again")
elif random_number == 5: 
  answer = ("Ask again later")
elif random_number == 6:
  answer = ("Better not tell you now")
elif random_number == 7:
  answer = ("My sources say no")
elif random_number == 8:
  answer = ("Outlook not so good")
elif random_number == 9:
  answer = ("Very doubtful")
else:
   answer = ("Error")

if name and first_question:
  print("Magic 8-Ball's Answer:" , answer)

  


