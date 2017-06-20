import os, time
import subprocess
from multiprocessing import Process

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

# definire file di configurazione: parti da un template
def execCommand(command):
    os.system(command)
    time.sleep(2)

class FakeAccessPoint():

    def __init__(self):
        #self.interface = wlan
        conf = '/home/lcomi/school/wireless/WirelessMayhem/hostap_def.conf'
        hostapd = '/home/lcomi/work/software/hostapd-2.2/hostapd/hostapd'
        logfile = '/usr/local/var/log/radius/freeradius-server-wpe.log'

    def setConf(self):
        print G + '[INFO]' + W +' Please edit the configuration file e.g. "/home/lcomi/school/wireless/WirelessMayhem/DEF_hostapd.conf" when you are done, press CTL+C'
        b=True
        while b==True:
            try:
                time.sleep(3)
            except(KeyboardInterrupt, SystemExit):
                b=False
                print G + '[INFO]' + W + 'Starting the Fake AP'

    def run(self):

        os.chdir('/home/lcomi/work/software/hostapd-2.6/hostapd')

        proc = subprocess.Popen('xterm -e radiusd -X', shell=True)
        time.sleep(2)
        proc1 = subprocess.Popen('xterm -e ./hostapd-wpe /home/lcomi/school/wireless/WirelessMayhem/DEF_hostapd.conf', shell=True)
        time.sleep(2)
        proc2 = subprocess.Popen('xterm -e tail -f /usr/local/var/log/radius/freeradius-server-wpe.log', shell=True)

