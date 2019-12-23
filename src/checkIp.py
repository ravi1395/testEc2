import socket as s
class ip:
    def __init__(self):
        self.sock = s.socket(s.AF_INET, s.SOCK_DGRAM)

    def close(self):
        self.sock.close()

    def getIp(self):
        self.sock.connect(('8.8.8.8', 80))
        ip = self.sock.getsockname()[0]
        self.close()
        return ip
