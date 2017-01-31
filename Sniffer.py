

class Sniffer(object):
    """
    This module provides multiple sniffing and filtering options
    """

    def __init__(self, interface):
        self.interface = interface
        print interface
        exit('ciao')

    def listDevice(self, macAddresses):
        s = manuf.MacParser()
        for item in macAddresses:
            res = s.get_all(item)
            print res
