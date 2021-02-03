#1
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]

list1, list2 = list2, list1

print("list1 value :", list1)
print("list2 value :", list2)


#2
s = input("Can you enter a single digit integer?")

try:
    if int(s)>=0:
        print("Even Numbers :")
        for i in range(int(s)):
            if i % 2 == 0:
                print(i)
except:
        print("Llease enter number.")
