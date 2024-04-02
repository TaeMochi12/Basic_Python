mylist=[4,8,12,48,56,88,100]
target=int(input('Enter the element to search in the list:'))
start=0
end=len(mylist)-1
flag=0
while start<=end:
    mid=int((start+end)/2)
    if mylist[mid]==target:
        print("Target found at index",mid)
        flag=1
        break
    elif mylist[mid]<target:
        start=mid+1
    else: 
        end=mid-1

if flag==0:
    print("Element not found")