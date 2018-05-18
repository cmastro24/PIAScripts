#!/usr/bin/env python3

import requests
import netifaces as ni
from hashlib import md5
import os
import json

#Todo#
#Parameterize Username/Password

USERNAME = ''
PASSWORD = ''

def get_interface_ip(iface):
    ni.ifaddresses(iface)
    return ni.ifaddresses(iface)[ni.AF_INET][0]['addr']

def get_pia_port(username, password, iface):
    ip = get_interface_ip(iface)
    client_id = md5(os.urandom(16)).hexdigest()
    payload = { 'client_id': client_id, 
                'local_ip': ip,
                'user': USERNAME, 
                'pass': PASSWORD }
    r = requests.post('https://www.privateinternetaccess.com/vpninfo/port_forward_assignment', data=payload)
    port_json = json.loads(r.text)
    return port_json['port']

print(get_pia_port(USERNAME,PASSWORD,'tun0'))
