arr=[1,2,3,[2,3,4,5]]
arr3=arr[3:]# slicing #list
print(arr3[0][2])# nested list
arr3[0][2]=10
print(arr)
print(arr3)


