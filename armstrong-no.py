num = int(input("Enter a 3-digit number: "))
temp = num
sum = 0
while temp > 0:
    digit = temp % 10
    sum = sum + digit * digit * digit
    temp = temp // 10
if sum == num:
    print("Armstrong number")
else:
    print("Not an Armstrong number")
