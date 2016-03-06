#!
file = open('env.props', 'w')
file.write('TEST=hi, its me!\n')
file.write('SSH_HOSTNAME=45.55.142.115\n')
file.close()
print('done creating file')