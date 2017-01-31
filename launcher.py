import os
import sys
import Sniffer, FakeAccessPoint, sniff

# Console colors
W = '\033[0m'  # white (normal)
R = '\033[31m' # red
G = '\033[32m' # green
O = '\033[33m' # orange
B = '\033[34m' # blue
P = '\033[35m' # purple
C = '\033[36m' # cyan
T = '\033[93m' # tan
ast = '['+B+'*'+W+'] '
min = '['+R+'-'+W+'] '
plu = '['+G+'+'+W+'] '

def main():
    if not os.geteuid() == 0:
        sys.exit(R+'WirelessPrism must be run as root... Exiting'+W)

    print('Welcome in WirelessPrism, please choose one of the following activities:')
    print('[1] Passive Sniffing')
    print('[2] Fake Access Point')

    while True:
        input = raw_input()
        if input == '1':
            print G+'Chiamo il modulo sniffing'+W
            a = ['D0:65:CA:2A:9E:F2','A0:8D:16:61:A7:EA', '10:1C:0C:6A:75:AE', 'DC:3E:F8:A2:21:6C', '34:8A:7B:AE:FC:66',
                 'CC:FA:00:B5:77:4F']
            s = Sniffer.Sniffer()
            print s.listDevice(a)
            sniff.pktPrint()
            exit()

        elif input == '2':
            print 'Chiamo il modulo FAP'
            f = FakeAccessPoint.FakeAccessPoint()
            exit()

        else:
            print('please choose one of the options and enter the corrispective number: ')

if __name__ == '__main__':
    main()