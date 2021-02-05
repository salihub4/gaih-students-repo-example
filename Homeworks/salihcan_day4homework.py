lowervalue = 0 
topvalue = 100

for number in range(lowervalue,topvalue + 1):
    if number > 0:
        for i in range(2,number):
            if (number % i) == 0:
                break
        else:
            print(number)