def printer(msg):
    print(msg)
printer('Uday')

x = printer

x('Rohan')

def indirect(func,msg):
    func(msg)
indirect(printer,'test')

y = x
y("test2")
print(y.__name__)

#lamda 

#normal Function
def func(x, y, z): return x + y + z
print(func(1,2,3))

#lamda function
var = lambda x,y,z: x+y+z
print(var(1,2,3))

def f1(x): return x**2
def f2(x): return x**3
def f3(x): return x**4

l = [f1, f2, f3]

for i in l:
    print(i(2))

l = [lambda x: x**2,
     lambda x: x**3,
     lambda x: x**4
    ]
for i in l:
    print(i(3))

dictFunction = {
                'add': lambda x,y: x+y,
                'sub': lambda x,y: x-y,
                'mul': lambda x,y: x*y,
                'div': lambda x,y: x/y
}

print(dictFunction['mul'](2,7))