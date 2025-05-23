n=int(input("Enter a number: "))
rev=0
num=n
while n>=0:
    r=n%10
    rev=(rev*10)+r
    n=n//10
print('Reverse of ',num,' is ',rev)

if num==rev:
    print("Palindrome")
else:
    print("Not Palindrome")
