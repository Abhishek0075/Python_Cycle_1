num=int(input("Enter a 4 digit number : "))
#Initializing different variables for processes
sum=0
reverse=0
odddiff=1
evendiff=1
r=num%10
# Reversing and doing product of odd and even postion digits
reverse=(reverse*10)+r
sum=sum+r
evendiff=evendiff*r
num=num//10
r=num%10
reverse=(reverse*10)+r
sum=sum+r
odddiff=odddiff*r
num=num//10
r=num%10
reverse=(reverse*10)+r
sum=sum+r
evendiff=evendiff*r
num=num//10
r=num%10
reverse=(reverse*10)+r
sum=sum+r
odddiff=odddiff*r
num=num//10
print("Sum =",sum)
print("Reverse =",reverse)
print("Difference =",(odddiff-evendiff))


