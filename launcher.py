import os
import subprocess
import sys
import Sniffer
import FakeAccessPoint
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
    print(O + '[1]' + W + ' Wi-Fi SSID Sniffer')
    print(O + '[2]' + W + ' Sensible Data Sniffer')
    print(O + '[3]' + W + ' FTP Credential Sniffer')
    print(O + '[4]' + W + ' Mail Sniffer')
    print(O + '[5]' + W + ' Airodump')
    print(O + '[6]' + W + ' Fake Access Point')


def selectMON_interface():
    print B+'[INFO]'+W+' Looking for a monitor-mode interface'
    cmd = "ifconfig -a | grep mon | cut -d ':' -f1"
    try: # cerca interfacce in monitor mode
        mon_interfaces = subprocess.check_output(cmd, shell=True)
        print mon_interfaces

    except:
        print R+'[ERROR]'+W+' No monitor-mode interfaces found'
        mon_interfaces = False

    # cerca interfacce wireless wlanX
    if not mon_interfaces:
        cmd = "ifconfig -a | grep wlan | cut -d ':' -f1"
        print B+'[INFO]'+W+' Looking for a Wlan interface'

        try:
            wlan_interfaces = subprocess.check_output(cmd, shell=True)
            print G + '[INFO]' + W + ' Wlan found'
        except:
            # non ci sono nemmeno interfacce wireless
            print R+'[ERROR]'+W+' No Wlan interfaces found... Exiting'
            return False

        # ci sono interfacce ma esci e metti in monitor
        if wlan_interfaces:
            print B+'[INFO]'+W+' Please put in monitor mode ("$ airmon-ng start wlanX") one of these interfaces:\n'+wlan_interfaces
            return False
    else:
        interface = raw_input('Enter a Monitor interface: ')
    return interface


def selectWLAN_interface():
    print B+'[INFO]'+W+' Looking for a Wlan interface'
    cmd = "ifconfig -a | grep wlan"

    try: #cerca wlan
        wlan_interfaces = subprocess.check_output(cmd, shell=True)
        print G + '[INFO]' + W + ' Wlan found'
        print wlan_interfaces

    except:
        # non ci sono interfacce wireless
        print R+'[ERROR]'+W+' No Wlan interfaces found... Exiting'
        return False

    # ci sono interfacce!
    interface = raw_input('Enter a Wlan interface: ')
    return interface


def select_filename():
    filename = raw_input('Enter a Filename: ')
    return filename


def main():
    check_root()
    cmd = 'cat images/logo.txt'
    os.system(cmd)
    while True:
        #loop forever looking for an option
        try:
            print_menu()
            input = raw_input()

            # options list
            if input == '1':
                interface = selectMON_interface()
                if interface:
                    print G + '[INFO] Starting Wi-Fi SSID Sniffer' + W
                    print G + '[INFO] Waiting for something interesting...' + W
                    try:
                        sniff(iface=interface, prn=Sniffer.ssidSniffer)
                    except(KeyboardInterrupt, SystemExit):
                        pass
                else:
                    print R +'[INFO]'+ W+' Exiting'
                    exit(1)

            elif input == '2':
                interface = selectMON_interface()
                if interface:
                    print G + '[INFO] Starting Sensible Data Sniffer' + W
                    print G + '[INFO] Waiting for something interesting...' + W
                    try:
                        sniff(filter='tcp', iface=interface, prn=Sniffer.sendibleDataSniff, store=0)
                    except(KeyboardInterrupt, SystemExit):
                        pass
                else:
                    print R +'[INFO]'+ W+' Exiting'
                    exit(1)

            elif input == '3':
                interface = selectWLAN_interface()
                if interface:
                    print G + '[INFO] Starting FTP Credential Sniffer' + W
                    print G + '[INFO] Waiting for something interesting...' + W
                    try:
                        sniff(filter='tcp port 21', iface=interface, prn=Sniffer.ftpSniff, store=0)
                    except(KeyboardInterrupt, SystemExit):
                        pass
                else:
                    print R +'[INFO]'+ W+' Exiting'
                    exit(1)

            elif input == '4':
                interface = selectWLAN_interface()
                if interface:
                    print G + '[INFO] Starting Mail Sniffer' + W
                    print G + '[INFO] Waiting for something interesting...' + W
                    try:
                        sniff(filter="tcp port 110 or tcp port 25 or tcp port 143", prn=Sniffer.mailSniff, store=0)
                    except(KeyboardInterrupt, SystemExit):
                        pass
                else:
                    print R +'[INFO]'+ W+' Exiting'
                    exit(1)

            elif input == '5':
                interface = selectMON_interface()
                if interface:
                    print G + '[INFO] Starting AirDump' + W
                    filename = select_filename()
                    try:
                        Sniffer.Airdump(interface, filename)
                    except(KeyboardInterrupt, SystemExit):
                        pass
                else:
                    print R +'[INFO]'+ W+' Exiting'
                    exit(1)
                time.sleep(1)

            elif input == '6':
                print G + '[INFO] Starting Fake Access Point' + W
                try:
                    fap = FakeAccessPoint.FakeAccessPoint()
                    fap.setConf()
                    fap.run()
                except(KeyboardInterrupt, SystemExit):
                    print R + '[INFO]' + W + ' Exiting'
                    exit(1)


        #exiting with ctrlC
        except KeyboardInterrupt:
            print R +'[INFO]'+ W+' Exiting'
            exit(0)


if __name__ == '__main__':
    main()
