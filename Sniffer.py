from scapy.all import *
import manuf


class Sniffer(object):
    """
    This module provides multiple sniffing and filtering options
    """

    monitor_interface = ''

    def listDevice(self, macAddresses):
        s = manuf.MacParser()
        for item in macAddresses:
            res = s.get_all(item)
            print res
