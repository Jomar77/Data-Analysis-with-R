import random
import math

def main():
    print("Welcome to the Lottery numbers generator")
    num_entries = int(input("How many entries would you like? "))
    print()
    
    for i in range(num_entries):
        print("Entry", i+1, end=": ")
        
        skewness = input("Enter 'left' for left skewness or 'right' for right skewness: ")
        std_dev = 10
        meanLeft =[12,16]
        meanRight =[20,24]
        
        if skewness.lower() == 'left':
            mean = random.choice(meanLeft)
        elif skewness.lower() == 'right':
            mean = random.choice(meanRight)
        else:
            print("Invalid input")
            return
        
        
        numarr = []
        for j in range(6):
            #num should not be repeated
            num = math.ceil(random.gauss(mean, std_dev))
    
            #check if num is already in the array, then append it
            
            while num < 1 or num > 40 or check(num, numarr):
                num = math.ceil(random.gauss(mean, std_dev))
                
            numarr.append(num)
            print(numarr[j], end=" ")
        

        num = math.ceil(random.gauss(5, 3))
        
        while num < 1 or num > 10 or check(num, numarr):
            num = math.ceil(random.gauss(5, 2))
        
        print("Bonus:", num)

        print(numarr)
        if checkFile(str(numarr)):
            print("This entry already exists")
            break

    print()

#recursive function that checks if the number is already in the array
def check(num, numarr):
    return num in numarr

def checkNumbersInFile(numbers, file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    cleaned_lines = [line.strip() for line in lines]
    
    for num in numbers:
        if num in cleaned_lines:
            return True

    return False

numbers_to_check = tuple(['6', '23', '25', '27', '28', '32'])  # List of numbers you want to check
file_path = 'lotto.txt'  # Path to the text file

result = checkNumbersInFile(numbers_to_check, file_path)
print(numbers_to_check)
print(result)
