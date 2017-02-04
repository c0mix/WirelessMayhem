import csv
from StringIO import StringIO

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

def csvParser(result_file):
    with open(result_file, 'rb') as f:
        string = f.read()
    parts = string.split('\r\n\r\n')

    try:
        stations = parts[0]
    except IndexError:
        print R+'[INFO]'+W+' No Access Point Found, Exiting'
        exit()

    stations_str = StringIO(stations)

    try:
        clients = parts[1]
    except IndexError:
        print B+'[INFO]'+W+' No Client Found'
        pass

    try:
        clients_str = StringIO(clients)
    except UnboundLocalError:
        pass

    r = csv.reader(stations_str)
    i = list(r)
    z = [k for k in i if k <> []]
    stations_list = z

    try:
        r = csv.reader(clients_str)
        i = list(r)
        z = [k for k in i if k <> []]
        clients_list = z
    except UnboundLocalError:
        clients_list = []
        pass

    print_result(stations_list, clients_list)


def print_result(stations_list, clients_list):

    mac_list = []

    nstations = len(stations_list)
    sthead = stations_list[0]
    stations_head = [j.strip() for j in sthead]
    stations_data = [stations_list[i] for i in range(1,nstations)]

    print G+'[INFO]'+W+' Access Point Found:'
    for i,row in enumerate(stations_data):

        # get indices
        ap_mac_ix  = stations_head.index('BSSID')
        ap_name_ix = stations_head.index('ESSID')
        ap_sec_ix  = stations_head.index('Privacy')
        ap_pow_ix  = stations_head.index('Power')
        ap_ch_ix   = stations_head.index('channel')

        # get values
        ap_mac = row[ap_mac_ix].strip()
        ap_name = row[ap_name_ix].strip()
        ap_sec = row[ap_sec_ix].strip()
        ap_pow = row[ap_pow_ix].strip()
        ap_ch = row[ap_ch_ix].strip()

        # other stuff
        #mac_prefix = ap_mac[0:8]
        #ap_mfg = ''#ms.search(mac_prefix)

        if ap_name=='':
            ap_name="unlabeled"

        #mac_name = re.sub('\:','_',ap_mac)

        ######################
        # Print out some information
        print "="*40
        print "Name:",ap_name
        print "Channel:",ap_ch
        print "MAC:",ap_mac
        #print "Manufacturer:",ap_mfg
        print "Encryption:",ap_sec
        print "Power:",ap_pow
        print ""

    #################################
    # Data for
    # Clients
    #################################

    nclients = len(clients_list)
    clhead = clients_list[0]
    clients_head = [j.strip() for j in clhead]
    clients_data = [clients_list[i] for i in range(1,nclients)]

    print G + '[INFO]' + W + ' Clients Found:'
    for i,row in enumerate(clients_data):

        #indici
        c_mac_ix = clients_head.index('Station MAC')
        ap_mac_ix = clients_head.index('BSSID')
        c_pow_ix = clients_head.index('Power')

        #valori
        c_mac = row[c_mac_ix].strip()
        c_pow = row[c_pow_ix].strip()
        ap_mac = row[ap_mac_ix].strip()

        if c_mac=='(not associated)':
            continue

        #evito i duplicati
        if c_mac not in mac_list:
            mac_list.append(c_mac)

            #mac_prefix = c_mac[0:8]
            #c_mfg = lookup_hardware(mac_prefix)

            ######################
            # Print out some information
            print "="*40
            print "Client MAC:",c_mac
            print "Access Point MAC:",ap_mac
            print "Power:",c_pow
            print ""

    return False