

from generic import *
from datetime import date
from datetime import datetime
from ascent_logging import custom_logger as cl
import logging
import pytest
import os
import sched



today = str(date.today())
print (today)
datetimeobject = datetime.strptime(today,'%Y-%m-%d')
new = datetimeobject.strftime('%m-%d-%Y')
print(new)

time = datetime.now()
print(time)



file_path = ".\\Ascent_MDM\\today"
    #directory = os.path.dirname(file_path)
try:
    print(os.getcwd())
    if not os.path.exists(file_path):
        os.chdir("C:\\Users\\Hasher\\PycharmProjects\\Ascent_MDM")
        print("pass")
        os.mkdir(str(today))
        print(os.getcwd())
    else:
        print("path is already created")

except OSError:
    print('Error: Creating directory. ' + file_path)


try:
    #print(os.getcwd())
    source = "C:\\Users\\Hasher\\PycharmProjects\\Ascent_MDM"
    destination = 'C:\\Users\\Hasher\\PycharmProjects\\Ascent_MDM\\'
    url = destination.__add__(today)
    print(url)
    if os.path.exists(url):
        print('pass1')
        for data in os.walk(destination):
            for info in data:
                print(info)
                if info.find('.html'):
                    print(info)
                    print("Created: %s" % time.ctime(os.path.getctime(info)))

    #for file in source
    #if file.endswith)
    else:
        print('fail')



except OSError:
    print('done')

