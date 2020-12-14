import random

answer = ''  
a_count=0 
b_count=0 

items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
random.shuffle(items)

for i in range(4):
    answer+=str(items[i])

while(True):
    number=input('Enter the number: ')
    if not number.isdigit() or len(number) != 4:  
        print('Please enter four digits')
    else:
        if number==answer:
            print('excellent you guess the correct number')
            break
        for i in range(4):
            for j in range(4):
                if i==j and number[i]==answer[j]:
                    a_count+=1
                elif number[i]==answer[j]:
                    b_count+=1
        print('{0}A{1}B'.format(a_count,b_count))
        a_count=0
        b_count=0
