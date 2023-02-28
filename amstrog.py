num = int(input("Please Enter a Number:"))

sum = 0
temp = num

while temp > 0:
    digit = temp % 10
    print(digit)
    sum += digit * digit * digit
    temp = temp//10
 
if sum==num:
    print('It is an Armstrong number')
else:
    print('It is not an Armstrong number')
