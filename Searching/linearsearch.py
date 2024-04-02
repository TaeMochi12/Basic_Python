mylist=[4,8,12,48,56,88,100]
target=int(input('Enter the element to search in the list:'))
flag=0
for i in mylist:
    if(target==i):
        print("Target found at index",mylist.index(i))
        flag=1
        break

if flag==0:
    print("Element not found")