import os, subprocess, sys
import Sniffer
from scapy.all import *

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

def check_root():
    if not os.geteuid() == 0:
        sys.exit(R+'WirelessPrism must be run as root... Exiting'+W)

def print_menu():
    print('\n'+G + 'Welcome in Wireless Mayhem Framework, please choose one of the following activities:' + W)
    print(R + '[1]' + W + ' Wi-Fi SSID Sniffer')
    print(R + '[2]' + W + ' Sensible Data Sniffer')
    print(R + '[3]' + W + ' FTP Credential Sniffer')
    print(R + '[4]' + W + ' Mail Sniffer')
    print(R + '[5]' + W + ' Airodump')

def select_interface():
    print B+'[INFO]'+W+' Looking for a monitor-mode interface'

    # cerca interfacce in monitor mode
    cmd = "ifconfig -a | grep mon"
    try:
        mon_interfaces = subprocess.check_output(cmd, shell=True)
        print mon_interfaces

    except:
        print R+'[INFO]'+W+' No monitor-mode interfaces found'
        mon_interfaces = False

    # cerca interfacce wireless
    if not mon_interfaces:
        cmd = "ifconfig -a | grep wlan"
        print B+'[INFO]'+W+' Looking for a Wlan interface'

        try:
            wlan_interfaces = subprocess.check_output(cmd, shell=True)

        except:
            # non ci sono nemmeno interfacce wireless
            print R+'[INFO]'+W+' No Wlan interfaces found... Exiting'
            return False

        # ci sono interfacce ma esci e metti in monitor
        if wlan_interfaces:
            print G+'[INFO]'+W+' Wlan found'
            print B+'[INFO]'+W+' Please put in monitor mode ("$ airmon-ng start wlanX") one of these interfaces:\n'+wlan_interfaces
            return False
    else:
        interface = raw_input('Enter a Monitor interface: ')

    return interface

def select_filename():
    filename = raw_input('Enter a Filename: ')
    return filename

def main():
    check_root()
    while True:
        try:
            print_menu()
            input = raw_input()

            if input == '1':
                print G+'[INFO] Starting Wi-Fi SSID Sniffer'+ W
                interface = select_interface()
                if interface:
                    try:
                        sniff(iface=interface, prn=Sniffer.ssidSniffer)
                    except(KeyboardInterrupt, SystemExit):
                        pass
                else:
                    exit(1)

            elif input == '2':
                print G+'[INFO] Starting Sensible Data Sniffer'+ W
                interface = select_interface()
                if interface:
                    try:
                        sniff(filter='tcp', iface=interface, prn=Sniffer.sendibleDataSniff, store=0)
                    except(KeyboardInterrupt, SystemExit):
                        pass
                else:
                    exit(1)

            elif input == '3':
                print G+'[INFO] Starting FTP Credential Sniffer'+ W
                interface = select_interface()
                if interface:
                    try:
                        sniff(filter='tcp port 21', iface=interface, prn=Sniffer.ftpSniff, store=0)
                    except(KeyboardInterrupt, SystemExit):
                        pass
                else:
                    exit(1)

            elif input == '4':
                print G+'[INFO] Starting Mail Sniffer'+ W
                interface = select_interface()
                if interface:
                    try:
                        sniff(filter="tcp port 110 or tcp port 25 or tcp port 143", prn=Sniffer.mailSniff, store=0)
                    except(KeyboardInterrupt, SystemExit):
                        pass
                else:
                    exit(1)

            elif input == '5':
                print G+'[INFO] Starting AirDump'+ W
                interface = select_interface()
                if interface:
                    filename = select_filename()
                    try:
                        Sniffer.Airdump(interface, filename)
                    except(KeyboardInterrupt, SystemExit):
                        pass
                else:
                    exit(1)
                time.sleep(1)


        except KeyboardInterrupt:
            exit('\nBye, Bye\n')

if __name__ == '__main__':
    main()