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

import csv
#checks if the entry already exists in the csv file
import csv

def is_list_in_csv(check_list, csv_file_path):
    with open(csv_file_path, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            row_as_integers = [int(item) for item in row]  # Convert row items to integers
            if set(check_list) <= set(row_as_integers):
                return True
    return False

# Example usage
my_list = [6,23,25,27,28,3]
csv_file_path = 'output.csv'

my_list_str = ','.join(map(str, my_list))

print(is_list_in_csv(my_list, csv_file_path))