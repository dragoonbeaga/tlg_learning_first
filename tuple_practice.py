

tuple_record = ('etho', 'AA:BB:CC:DD:11:22', '192.168.0.1', '5060', 'UDP')



print(tuple_record)
print(tuple_record * 2)


records = ['etho', 'AA:BB:CC:DD:11:22', '192.168.0.1', '5060', 'UDP']


import time
local_time = time.localtime(time.time())
print(local_time)
print(type(local_time))
print('The year is {}'.format(local_time[0]))    #year
print(f'The month is: {local_time[1]}')    #month
print(f'The day is {local_time[2]}')    #day
print('The hour is {}' .format(local_time[3]))    #hour
print('The minutes is', local_time[4])    #minutes

print('{}/{}/{}'.format(local_time[0], local_time[1], local_time[2]))