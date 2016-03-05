#!
import os

file = open('env.props', 'w')
for key in os.environ.keys():
    file.write(str(key) + '=' + str(os.environ[key]) + '\n')
file.close()
print('done creating file')