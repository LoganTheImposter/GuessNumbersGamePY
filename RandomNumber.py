import random

target = random.randint (0, 9)
count = 0
life = 3

while True:    
    if count < 3:
        print('Choose number between 0-9 you have %a Times' % life)
        num = int(input())
        if num > target:
            print('The number is lower Try agian!')
            print('---------------------')
            count +=1
            life -=1
        elif num < target:
            print('The number is higher Try agian!')
            print('---------------------')
            count +=1
            life -=1
        else:
            print()
            print('--You won!!!')
            break
           
    else:
        print('You failed the number is %x' % target)
        print('----------********----------')
        break