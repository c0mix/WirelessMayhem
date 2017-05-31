import os

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
class FakeAccessPoint():

    def __init__(self):
        #self.interface = wlan
        self.conf = 'hostap_def.conf'
        self.hostapd = '/home/lcomi/work/software/hostapd-2.2/hostapd/hostapd'
        self.logfile = '/usr/local/var/log/radius/freeradius-server-wpe.log'

    def setConf(self):
        print 'Specify a configuration file path or digit "d" for use the default one: '
        input = raw_input()
        if input != 'd':
            self.conf = input
        else:
            print 'You select the default configuration: '
            os.system('cat hostap_def.conf')


    def run(self):
        command = 'radiusd -X'

        command = './hostapd-wpe ' + self.conf

        command = 'tail -f /usr/local/var/log/radius/freeradius-server-wpe.log' #se nuova istanza questo file potrebbe non essere ancora stato creato
        os.system(command)

# lanciare freeradius ... prima di hostapd
# lanciare hostapd ... usa anche finestre temrinale... GUI
# notifica password intercettata ... puoi lanciare un tail in un altra finestra
# quando si preme ctrl+c si blocca il tutto, si termina freeradius e l'hostapd
# si chiude la finestra con il tail
# si mostrano a video i risultati