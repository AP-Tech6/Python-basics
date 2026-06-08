l=list(map(int,input().split()))
k=int(input())
for i in l:
    if i==k:
        print("yes found")
        break
else:
    print("not found")

#here time complexity :O(N)
# binary search based on divide and conquer method
# linear search does not require array to be sorted but binary search works on sorted array    



