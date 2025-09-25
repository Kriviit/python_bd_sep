#function-> these are block of code which are design or implemented to perform some action
#print()-> to get the o/p in clg
#type()--> return datatype(class name)

#void
#return type

a=10+5

#syntax
#  def <function name>():
#     statements1
#     statements1
#     statements1
#     statements1

def add(a,b):# implementation or declaration
    print(a+b)

def sub(num1,num2):
    print(num1-num2)

#call the function
# print("this is the first line")
# add(10,20)#30 a=10 b=20
# sub(20,20)#0 a=20 b=20
# print("this is the last line")

# accessing func address
c=add
c(10,20)
c(50,20)