s=input("enter a string")
n=len(s)
flag=0
if n%2:
    mid=n//2+1
else:
    mid=n//2
start=0
end=mid
while(start<mid and end<n):
    if (s[start]==s[end]):
        start=start+1
        end=end+1
    else:
        flag=1
        break
if flag==0:
    print("string is symmetrical ")
else:
    print("string is not symmetrical")
