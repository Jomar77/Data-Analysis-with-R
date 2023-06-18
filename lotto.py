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
        meanLeft =[11,12,13,14,15,16]
        meanRight =[24,25,26,27,28,29]
        
        if skewness.lower() == 'left':
            mean = random.choice(meanLeft)
        elif skewness.lower() == 'right':
            mean = random.choice(meanRight)
        
        numarr = []
        for j in range(6):
            #num should not be repeated
            num = math.ceil(random.gauss(mean, std_dev))
    
            #check if num is already in the array, then append it
            
            while num < 1 or num > 40:
                num = math.ceil(random.gauss(mean, std_dev))
                if check(num, numarr):
                    break
                numarr.append(num)
                
        print(len(numarr))
        
        for j in range(6):
            print(numarr[j], end=" ")

        num = math.ceil(random.gauss(5, 2))
        
        while num < 1 or num > 10:
            num = math.ceil(random.gauss(5, 2))
        
        print("Bonus:", num)
    print()

#function that checks if the number is already in the array
def check(num, numarr):
    for i in range(len(numarr)):
        if num == numarr[i]:
            return True
    return False

main()
