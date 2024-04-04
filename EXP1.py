import array as a


b= a.array('i',[5,4,3,2,1])
 #print(b)

for i in range(0,5):
    print(b[i],end=" ")
    
def insertionSort(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        j=i-1
        while j>=0 and key<arr[j]:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
        



 
def selectionsort(arr) :
    for i in range(len(arr)):
        min_idx=i
        for j in range(i+1,len(arr)):
            if arr[min_idx]>arr[j]:
                min_idx=j
        arr[i],arr[min_idx]=arr[min_idx],arr[i]
    

        
            
arr=[12,11,13,5,6]
selectionsort(arr)
print("sorted array is:")
for i in range(len(arr)):
    print("%d"%arr[i])
