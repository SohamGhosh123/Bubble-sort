print("Bubble sort")
def Bubblesort(arr):
    n=len(arr)
    for i in range(n-1):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
arr=[4,5,3,7,2,8,0]
Bubblesort(arr)
print("sorted arrey is :")
for i in range(len(arr)):
    print(arr[i])