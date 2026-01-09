n = int(input("enter the number of terms : "))
a = 0
b = 1
print("fibonacci series is : ")
for i in range (1,n+1) :
    print(a,end=" ")
    a,b=b,a+b
