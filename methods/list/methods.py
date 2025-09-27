# # to know abt methods
# # dir()
# # print(dir([]))
# # arr=[1,2,3]
# # arr2=[1,2,3,4]
# # print(dir(arr))
# # result=arr.append(10)#VOID None
# # print(arr)
# # print(result)
# # result=arr2.clear()#VOID None
# # print(arr2)
# # result=arr.insert(1,10)#VOID None
# # print(arr)
# # print(result)

# a=[1,2,3,5]
# b=[1,2,3,5]
# result=a.append(10)#updating the object or list  --> void
# a.clear() # no return type

# print(result)
# print(b)

# c=a.copy()# return

# d=[1,1,1,2,1,2,3,34,1,2,23,3,4,1]
# result=d.count(1)
# arr=[1,2,3,4]
# arr2=[5,6,7,8]
# [1,2,3,4,5,6,7,8]
# #arr+arr2
# arr.extend(arr2)
# print(arr)
# idx=arr.index(4)
# print(idx)
arr=[1,2,3,4,5,-1,-2] #element
# arr.remove(3)#void
# popped_item=arr.pop(0)#idx
result=arr.sort(reverse=True)
print(result)
# print(popped_item)
print(arr)