a=int(input("Enter a number : "))
def check(a):# Function for checking whether number is a happy number
  sum=0
  happy=False
  for i in range (101):
    while a>0:
      r=a%10
      sum=sum+(r**2)
      a=a//10
    if sum==1:
      happy=True
      break
    else:
      a=sum
      sum=0
  return happy
if check(a)==True:
  print("The number is a Happy number")
else:
  print("The number is a Sad number")
   


def range_print(): # Function for printing happy numbers in the range 
  l=int(input("Enter the first range : "))
  u=int(input("Enter the final range : "))
  for i in range(l,u+1):
    if check(i)==True:
      print(i)
print("")
range_print()


def first_n_print(): # Function for printing first n happy numbers
  n=int(input("Enter the number of happy numbers needed : "))
  count=0
  i=0
  while count<n:
    i=i+1
    if check(i)==True:
      print(i)
      count=count+1
print("")
first_n_print()