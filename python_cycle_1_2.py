def get_side():# Taking the sides of two triangles
  print("Give sides of first triangle")
  a=int(input("Enter side 1 : "))
  b=int(input("Enter side 2 : "))
  c=int(input("Enter side 3 : "))
  print("Give sides of second triangle")
  d=int(input("Enter side 1 : "))
  e=int(input("Enter side 2 : "))
  f=int(input("Enter side 3 : "))
  return a,b,c,d,e,f
def area(a,b,c):# Triangle's area
  s=(a+b+c/2)
  area=((s*(s-a)*(s-b)*(s-c))**0.5)
  return area
a,b,c,d,e,f=get_side()
area1=area(a,b,c)
area2=area(d,e,f)
print("Areas are :")
print("Area 1 =",area1)
print("Area 2 =",area2)
print("Area 1 + Area 2 = ",area1+area2)
print("The contributions are :")
print("Contribution of 1st triangle is",(area1*100)/(area1+area2),"%")
print("Contribution of 2nd triangle is",(area2*100)/(area1+area2),"%")
