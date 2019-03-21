
num = 100
def changer():
   global num
   num = 90
   print(num)
changer()
print(num) 


def data(a, *b):
    print(b)
data(1,2,3,4,5,4,4,3,3,3,3)

def dictData(**d):
    print(d)

dictData(name='rohan', age=90)

def f1(a, c, *b, **d):
    print('a is ',a)
    print('b is ',b)
    print('c is ',c)
    print('d is ',d)
f1(1,2, [1,2,3,4], name="jerin", age=78)


def setUserData(firstName, lastName, age, address):
      print("first Name is ", firstName)
      print("last Name is ", lastName)
      print("age is ", age)
      print("address is ", address)

data = ['jarin', 'alen']
dataDict = {'age': 45, 'address': 'Delhi'}

setUserData(*data, **dataDict)