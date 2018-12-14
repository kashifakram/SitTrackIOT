import serial
import struct
import urllib2


if __name__ == '__main__':
    s = serial.Serial('/dev/ttyACM0')
    while True:
        res = s.read()
        urllib2.urlopen("http://192.168.43.109:8080/{}/{}".format(res, s.read()))
        print(int(res))
