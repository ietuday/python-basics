fhandle = open('abc.txt', 'w')
line1 = 'My Name is Slim Shady\n'
fhandle.write(line1)
line2 = 'My Name is UDAYADITYA SINGH\n'
fhandle.write(line2)
name = 'Test'
age = 27
CGPA = 7.85
fhandle.write(name+ '\n')
fhandle.write(str(age) + '\n')
fhandle.write(str(CGPA) + '\n')

fhandle.close()

fhandle = open('abc.txt', 'r')
data = fhandle.read()
print(len(data))
