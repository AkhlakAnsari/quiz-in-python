#for addition convert score into integer
score = 0
score = int(score)

#USER NAME
name = input("GOOD NAME PLEASE:")
print("""Hello {},
Good luck for quiz!""".format(name))
print('please use for answer is option Ex A,B,C,D capital letter')

#Question1
print("""1.where is the capital of india?
A. Bihar  
B. Bengaluru 
C. Chennai
D. New delhi""")

answer1 = "D"
response1 = input("Your answer is:")

if (response1 != answer1):
    print('''wrong answer! \n Right answer is:New delhi''')

else:
    print("Well done! " + response1 + " is correct!")
    score = score + 1

print("Your current score is " + str(score) + " out of 5")

#Question2
print("""2.national language of india?
A. Hindi 
B. Urdu 
C. English 
D. Bhojpuri""")

answer2 = "A"
response2 = input("Your answer is:")

if (response2 != answer2):
    print('''Wrong answer!\n Right answer is :Hindi ''')


else:
    print("Well done! " + response2 + " is correct!")
    score = score + 1

print("Your current score is " + str(score) + " out of 5")

#Question3
print("""3.who is the first prime minister of india?
A. Narendra Modi 
B. Amit Shah
C. Jawaharlal Nehru 
D. Rahul Ghandhi""")

answer3 = "C"
response3 = input("Your answer is:")

if (response3 != answer3):
    print('''Wrong answer!\n Right answer is :Jawaharlal Nehru''')
else:
    print("Well done! " + response3 + " is correct!")
    score = score + 1

print("Your current score is " + str(score) + " out of 5")

#Question4
print("""4.who is the father of nation of india?
A. Mahatma Ghandhi
B. Sardar vallabhbhai patel
C. Lala lajpatrai
D. Bal gangadhar tilak""")

answer4 = "A"
response4 = input("Your answer is:")

if (response4 != answer4):
    print('''Wrong answer!\n Right answer is :Mahatma Ghandhi''')
else:
    print("Well done! " + response4 + " is correct!")
    score = score + 1

print("Your current score is " + str(score) + " out of 5")

#Question5
print(""" 5.who is famous for missile man of india?
A. Guru rajapurkar
B. Dr. A. P. J. Abdul Kalam
C. Akhlak ansari
D. Omprakash yadav""")

answer5 = "B"
response5 = input("Your answer is:")

if (response5 != answer5):
    print('''Wrong answer!\n Right answer is :Dr. A. P. J. Abdul Kalam''')
else:
    print("Well done! " + response5 + " is correct!")
    score = score + 1

print("Your total score is " + str(score) + " out of 5")
print("Thank you for playing {}, goodbye!".format(name))