size=int(input('Enter the size of an array: '))
print('Enter elements :')
arr=[]
for i in range(size):
    ele=int(input('Enter element {}: '.format(i+1)))
    arr.append(ele)

for i in range(size-1):
    for j in range(i+1,size):
        if arr[j]<arr[i]:
            print("step {},{} : {}".format(i+1,j+1,arr))
            arr[j],arr[i]=arr[i],arr[j]
            

print("\nSorted array by selection sort method: ",arr)