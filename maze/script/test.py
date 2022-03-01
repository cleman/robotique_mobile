#!/usr/bin/env python
def read():
    file = open("/home/prof/lebhou_ws/src/maze/script/integer","r")
    data = file.readlines()
    file.close()
    return data[0]

while 1:
    print(read())