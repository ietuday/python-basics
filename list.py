num = [1,2,3]
emp_names = ['rahul', 'james', 'uday', 'palash']
print(emp_names)
emp_name = ['rahul', 'james', ['uday', 'palash']]
print(emp_name)

for emp in emp_names:
    print(emp)

print(len(emp_names))
print(range(4))

for i in range(len(emp_names)):
    print("at index " + str(i) + " element is " + emp_names[i])
