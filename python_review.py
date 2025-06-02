import random


file_name = "test.txt"
letters = ['a','b','c']


randomLetter = random.randint(1,3)

with open(file_name,'w') as file: 
    i=0
    while i<100: 
        randomNumber = random.randint(1, 9)
        randomLetter = random.randint(1,3)
        file.write(f'{letters[randomLetter-1]}, {randomNumber}\n')
        i+=1

a = 0
a_counter = 0
b = 0
b_counter = 0
c= 0
c_counter =0

with open(file_name,'r') as file: 
    for lines in file: 
        for character in lines: 
            first_letter = None
            if character.isalpha():
                first_letter = character
            if first_letter == 'a':  
                a+= int(lines[3])
                a_counter +=1
            elif first_letter == 'b':
                b+= int(lines[3])
                b_counter+=1
            elif first_letter == 'c':
                c+= int(lines[3])
                c_counter+=1


print(f"A average: {a/a_counter} \t B average: {b/b_counter} \t C average: {c/c_counter}")