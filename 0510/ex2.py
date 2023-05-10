i=1
sum=0
while (i<=100):
  sum+=i
  if(i%10==0):
    print("1-{}:{}".format(i,sum))
  i=i+1