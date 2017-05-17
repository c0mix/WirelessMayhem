<img src="images/logo.png" align="center"/>

## Project Description
This tool was developed as a final project of the "Wireless network" course @ Università degli Studi di Milano.
Our professor asked us to develop something intresting, innovative and creative regarding the wireless technologies tha we have studied during his coursework. 
I decided to build a small framework that will automate some of the tipical phases of the procedure that a penetration tester or a security expert have to perform in order to make a correct wireless network assessment.
## Technical Details
Wireless Mayhem is a python3 framework built for automate wireless attacks.
### Main Features
- Sniffing tools
- Fake Access Point based attacks
- Modular and scalable approach
- Easy to custom
### What can I do with the Wireless Mayhem Framework (WMF)
Thanks to Wireless Mayhem Framewoork you can automate some stpes of the wireless assessment procedure:
<img src="images/flowchartWIFIassessment.png" align="center"/>

- **DISCOVER**: the WMF integration with airodump-ng, can discover any Wireless network that is near you and provide a user friendly output in order to speed up the reconnaissance and discovery phases.
- **ATTACK & CRACK**: WMF implements a Fake AP using the hostapd-wpe software, which, for example, is capable to simulate a PEAP-WPA Enterprise network Access Point and intercept the passwords hashes but it can be also configured for instantiate a simple fake AP useful for many other attacks.
- **ASSESS**: WMF actually provides three different sniffer filters based on regular expressions and the python's scapy library; with this configuration you only  have to choose what you want to sniff and the launch the tool. 

### Hardware
In my personal experience with wifi penetration testing, I suggest you to buy this external wifi antenna: 
- http://www.tp-link.it/products/details/cat-11_TL-WN722N.html

But any type of wireless network adapter, if capable of packet injection, should work well, just check the compatibilty list here:
- https://www.aircrack-ng.org/doku.php?id=compatible_cards

## WMF Setup (on Debian)

### Dependencies

- **Hostapd-wpe** (https://github.com/OpenSecurityResearch/hostapd-wpe)
    Building instruction from the official repository:
```
    $ git clone https://github.com/OpenSecurityResearch/hostapd-wpe
```
    Ubuntu/Debian/Kali Building -
    -----------------------------------------------------------------------
```
        $ apt-get update
        $ apt-get install libssl-dev libnl-dev

        if you're using Kali 2.0 install:
        $ apt-get install libssl-dev libnl-genl-3-dev
```
    General -
    ------------------------------------------------------------------------
    	Now apply the hostapd-wpe.patch:
```
        $ git clone https://github.com/OpenSecurityResearch/hostapd-wpe

        $ wget http://hostap.epitest.fi/releases/hostapd-2.6.tar.gz
        $ tar -zxf hostapd-2.6.tar.gz
        $ cd hostapd-2.6
        $ patch -p1 < ../hostapd-wpe/hostapd-wpe.patch
        $ cd hostapd
```
        If you're using Kali 2.0 edit .config file and uncomment:
        CONFIG_LIBNL32=y
```
        $ make
```
        I copied the certs directory and scripts from FreeRADIUS to ease that
        portion of things. You should just be able to:
```
        $ cd ../../hostapd-wpe/certs
        $ ./bootstrap
```
        then finally just:
```
        $ cd ../../hostapd-2.6/hostapd
        $ sudo ./hostapd-wpe hostapd-wpe.conf
```

- **Python-Scapy** (http://www.secdev.org/projects/scapy/)
```
        $ sudo pip install scapy
```

- **Aircrack-ng suite** (https://www.aircrack-ng.org/)
```
        $ sudo apt-get install aircrack-ng
```

### Setup

After download and installing all the dependencies:
```
$ git clone https://github.com/c0mix/WirelessMayhem.git
$ cd WirelessMayhem
$ sudo python3 launcher.py
```

### First Run 

### Deploy New Module


## Final Presentation Slide

## Screenshots & Video Demo
[![FTP credential Sniffing](https://img.youtube.com/vi/KcH81PO7jVk/0.jpg)](https://www.youtube.com/watch?v=KcH81PO7jVk)
