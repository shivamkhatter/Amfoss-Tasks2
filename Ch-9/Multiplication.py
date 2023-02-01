import random
import time




numOfQuestions = 10
correct = 0

for i in range (numOfQuestions+1):
    num1 = random.randint(0,9)
    num2 = random.randint(0,9)
    print(str(num1),"*",str(num2))
    answer = (input("Give your answer "))
    tries=0
    while True:
        while answer == "":
            print("Give an integer as your answer")
            answer = (input("Give your answer "))
        answer=int(answer)
        if answer != str(num1*num2) and tries<2:
            answer = int(input("Try again"))
            tries += 1
        elif tries==2:
            print('Tries over ')
            break
        elif answer == (num1*num2):
            print('your answer ',answer,' is correct')
            correct +=1
            break
print("your score is ", (correct),"/%s"%i)
