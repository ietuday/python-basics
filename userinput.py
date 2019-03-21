# fhandle = open('userdata.txt', 'a')
# name = input('Enter your Name:')
# age = input('Enter your age')
# phone = input('Enter your mob number')
# address = input('Enter your address')
# fhandle.write('User Name is %s \n'%name)
# fhandle.write("%s's age is %d \n"%(name,age))
# fhandle.write("%s's phone is %d \n"%(name,phone))
# fhandle.write("%s's address is %s \n"%(name,address))
# fhandle.close()

import os

# path = os.getcwd()
# print(path)

# absolutePath = os.path.abspath('userdata.txt')
# print(absolutePath)
# print(os.path.exists('home/uday'))
# print(os.path.isdir(absolutePath))

# fhandle = open('systemdata.txt', 'w')
# def findir(dirname):
#     for name in os.listdir(dirname):
#         path = str(os.path.join(dirname, name))
#         if os.path.isdir(path):
#             findir(path)
#         else: 
#             print(path)
#             fhandle.write(path + '\n')
        
# path = '/home/geeky-uday/Downloads/python'
# findir(path)

cmd = 'google-chrome'
fp =   os.popen(cmd)
data = fp.read()
fp.close()