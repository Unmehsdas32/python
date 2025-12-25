##statement
'''
while condition:
  statement(s)
'''

##[1]
'''
i=1
while i<=5:
  print(i)
  i+=1
'''

##[2]
'''
num=int(input("Enter Your Number: "))
while num>0:
  print(num)
  num-=1
'''

##[3]while loop with break
'''
i=1
while i<=10:
  if i==5:
    break
  print(i)
  i+=1
'''

##[4]
'''
i=0
while i<10:
  i+=1
  if i==5:
    continue
  print(i)
'''

##[5]nested while
'''
n = 5
i = 1
while i <= n:
    j = 1
    while j <= i:
        print("*", end="")
        j += 1
    print()
    i += 1
'''



