def all_substring(): # Printing substrings of the strings
  a=str(input("Enter a string : "))
  l=len(a)
  for i in range (0,l+1):
    for j in range (i+1,l+1):
      sub=a[i:j]
      print(sub)


def substrings_of_k(): # Printing substrings of  length k
  k=int(input("Enter the length of substrings needed : "))
  a=str(input("Enter a string : "))
  l=len(a)
  for i in range (0,l+1):
    for j in range (i+1,l+1):
      sub=a[i:j]
      if len(sub)==k :
        print(sub)


def distinct(): # Printing substrings of  length k and n distinct characters
  a=str(input("Enter a string : "))
  k=int(input("Enter the length of substrings needed : "))
  n=int(input("Enter the number of distinct characters needed in the string : "))
  l=len(a)
  for i in range (0,l+1):
    for j in range (i+1,l+1):
      sub=a[i:j]
      s=set(sub)
      if len(s)==n and len(sub)==k:
        print(sub)



def distinct_and_max(): # Print substrings of length maximum length with N distinct characters
  a=str(input("Enter a string : "))
  n=int(input("Enter the number of distinct characters needed in the string : "))
  list1=[]
  l=len(a)
  for i in range (0,l+1):
    for j in range (i+1,l+1):
      sub=a[i:j]
      if len(set(sub))==n:
        list1.append(sub)
  m=len(max(list1,key=len))
  for i in range(len(list1)):
    if(len(list1[i])==m):
      print(list1[i])


def palindrome():   # Print substrings which are palindromes
  a=str(input("Enter a string : "))
  for i in range(0,len(a)+1):
    for j in range(i+1,len(a)+1):
      s=a[i:j]
      reverse=s[::-1]
      if(s==reverse):
        print(s)

# Using the functions
print("* Gives substrings")
all_substring()
print("* Gives substrings of a specific length")
substrings_of_k()
print("* Gives substrings of given number of distinct characters and given length")
distinct()
print("* Gives substrings of given number of distinct characters and maximum length")
distinct_and_max()
print("* Gives palindrome substrings")
palindrome()