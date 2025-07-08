#Conversion of number to binary
#using function bin()
num = bin(5)
print("It prints with prefix '0b':",num)
#output: 0b101
print("to avoid prefix ",num[2:])


#using division
num = 5
stringNum=""
while num > 0 :
    stringNum += str(num % 2)
    num //= 2

print(stringNum)

#Most optimal Approach

num = 5
stringNum=""
while num > 0:
    stringNum += str(num & 1)
    num >>= 1

print(stringNum)