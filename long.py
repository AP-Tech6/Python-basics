#to find longest subarray  such that their sum would be less than 10
#2 1 6 2 1 2 4 7 8 1 2 tracing output

li=list(map(int,input().split()))
k=int(input())
r=0  #checks sum <=10
l=0  #checks sum>10
m=0   #for maximum
s=0     #sum
while(r<len(li)):
    s+=li[r]
    while s>k:
        s=s-li[l]
        l+=1
    length=r-l+1
    m=max(m,length)
    r+=1
print(m)        


"""
Dry Run

Input:
2 1 6 2 1 2 4 7 8 1 2
10

Step-by-step

Window
[2]

sum = 2
length = 1
m = 1

Window
[2,1]

sum = 3
length = 2
m = 2

Window
[2,1,6]

sum = 9
length = 3
m = 3

Add 2

[2,1,6,2]

sum = 11

Now sum > 10

Remove from left:

remove 2

sum = 9

Window:
[1,6,2]

length = 3

Continue

Longest valid window becomes:

[2,1,2,4]

sum = 9
length = 4

So:
m = 4

Output:
4
"""