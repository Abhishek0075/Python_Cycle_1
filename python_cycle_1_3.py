def details():# Takes values
  name=str(input("Enter the name of the employee : "))
  code=int(input("Enter the code of the employee : "))
  bp=float(input("Enter the basic pay of the employee : "))
  return name,code,bp
def gross_salary(bp):# Fuction for gross salary calculation
  if bp<10000:                    
    gs=bp+bp*(5/100)+bp*(2.5/100 )+500
  elif bp>10000 and bp<30000:
    gs=bp+bp*(7.5/100)+bp*(5/100)+2500
  elif bp>30000 and bp<50000:
    gs=bp+bp*(11/100)+bp*(7.5/100)+5000
  else:
    gs=bp+bp*(25/100)+bp*(11/100)+7000
  return gs
def deduction(bp):# Function for calculation of deduction
  if bp<10000:
    d=20+bp*(8/100)
  elif bp>10000 and bp<30000:
    d=60+bp*(8/100)
  elif bp>30000 and bp<50000:
    d=60+bp*(11/100)+bp*(11/100)
  else:
    d=80+bp*(12/100)+bp*(20/100)
  return d
def netsalary(bp):# Function for calculation of netsalary
  gs=gross_salary(bp)
  d=deduction(bp)
  return (gs-d)
name1,code1,bpay=details()
print("")
print("=========Payment Slip=========")# PAYMENT SLIP MODELLING
print("Name         : ",name1)
print("Code         : ",code1)
print("Gross salary : ",gross_salary(bpay))
print("Deduction    : ",deduction(bpay))
print("Net salary   : ",netsalary(bpay))
print("==============================")
