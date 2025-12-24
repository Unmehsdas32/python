1st =[1,2,3]
2nd =[4,5,6]
print(1st+2nd)
sarch=["Nepal","Bhutan","Bangladesh","China"] 
country=input("Enter a country Name: ")
if country in sarch:  
  print(country,"is the member of sarch")
else:
  print(country,"is not the member of sarch")
marks=int(input("enter your number in maths:"))
if marks>=90 and marks<=100:
  print("A+")
elif marks>=80 and marks<90:
  print("A")  
elif marks>=70 and marks<80:
  print("B+") 
elif marks>=60 and marks<70:
  print("B")
elif marks>=50 and marks<60:
  print("C")
elif marks>=40 and marks<50:
  print("D")
elif marks>=0 and marks<40:
  print("F")
else:
  print("invalid marks")
    