import random
import math

def main():
    print("Welcome to the Lottery numbers generator")
    num_entries = int(input("How many entries would you like? "))
    print()
    
    for i in range(num_entries):
        print("Entry", i+1, end=": ")
        
        skewness = input("Enter 'left' for left skewness or 'right' for right skewness: ")
        mean = 20
        std_dev = 10
        meanLeft =[11,9,13,17,15]
        meanRight =[24,22,26,20]
        
        if skewness.lower() == 'left':
            mean = random.choice(meanLeft)
        elif skewness.lower() == 'right':
            mean = random.choice(meanRight)
        
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
    print()

#recursive function that checks if the number is already in the array
def check(num, numarr):
    return num in numarr


main()
