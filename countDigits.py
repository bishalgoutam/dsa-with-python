## Program to find the number of digits

def countDigits(n):
    count = 0
    while(n>0):
        n=n//10
        count+=1
    return count

if __name__ == "__main__":
    input_number = 789965
    count = countDigits(input_number)
    print(f'Count of digits in {input_number} is {count}.')