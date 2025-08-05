tup=[]
a=int(input("Enter limit:"))
for i in range(a):
      n=tuple(map(int,input("Enter tuples:").split()))
      tup.append(n)
print(tup)

for i in tup:
      sum=0
      for j in i:
            sum+=j
      print(f"sum of {i} is {sum}")
      
