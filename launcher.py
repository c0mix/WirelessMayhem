import os, subprocess
import sys
import Sniffer

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
            print '[INFO] Looking for a monitor-mode interface'

            cmd = "ifconfig -a | grep mon"
            try:
                mon_interfaces = subprocess.check_output(cmd, shell=True)
                print mon_interfaces
            except:
                print('[INFO] No monitor-mode interfaces found')
                mon_interfaces = False
            if not mon_interfaces:
                print '[INFO] Looking for a Wlan interface'
                cmd = "ifconfig -a | grep wlan"
                try:
                    wlan_interfaces = subprocess.check_output(cmd, shell=True)
                except:
                    print('[INFO] No Wlan interfaces found... Exiting')
                    exit(1)

                if wlan_interfaces:
                    print '[INFO] Wlan found'
                    print('[INFO] Please put in monitor mode ("$ airmon-ng start wlanX") one of these interfaces:\n' + wlan_interfaces)
                    exit(1)
            else:
                interface = raw_input('Enter a Monitor interface: ')
                print'calling sniffer'

            exit()

        elif input == '2':
            print 'Chiamo il modulo FAP'
            #f = FakeAccessPoint.FakeAccessPoint()
            exit()

        else:
            print('please choose one of the options and enter the corrispective number: ')

if __name__ == '__main__':
    main()