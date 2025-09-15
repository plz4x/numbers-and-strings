print("Prime Checker -- check if a number is prime!")
while True:
    num = input("Enter a whole number: ")
    num = int(num)
    if num < 1:
        print("Sorry, invalid number.")
    elif num == 1:
        print("Scientists are still debating whether 1 is a prime number or not!")
    elif num == 2:
        print("2 is prime!")
    else:
        checkNum = 2
        while checkNum < num:
            if num % checkNum == 0:
                print(f"{num} is not prime.")
                break
            else:
                checkNum = checkNum + 1
                print(f"{checkNum - 2} of {num - 2} calculations complete.")
        if num == checkNum:
            print("Calculations complete!")
            print(f"{num} is prime!")
