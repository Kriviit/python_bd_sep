arr1=[1,2,3,4]
arr2=[5,6,7,8]

# +
arr3=arr1+arr2 # list -concat[1,2,3,4,5,6,7,8]
print(arr3)
print(arr1)
print(arr2)

# repeating *
# we are mul a list with int
arr4=arr1*2
arr5=[-1]*10
print(arr4)
print(arr5)

#indexing
a=[1,2.3,"hello",True,[2,3,4]]
print(a)
print(a[0])
print(a[-5])

#slicing
arr6=[1,2,3,4,5,6,7,8,9,10,22,1,1,2,2,3,3]
sub=arr6[0:6:2]# new object
print(arr6[5])
sub[0]=10
print(sub)
print(arr6)

