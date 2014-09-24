import socket
import fcntl
import struct

class INet:

    def __init__(self):
        pass
    @staticmethod
    def get_ip(ifname):
        s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        return socket.inet_ntoa(fcntl.ioctl(
            s.fileno(),
            0x8915,
            struct.pack('256s', ifname[:15])
        )[20:24])

    @staticmethod
    def get_eth0_ip():
        ip = INet.get_ip("eth0")
        return ip
