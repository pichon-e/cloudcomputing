# !/usr/bin/env python
import boto
from init import *
from optparse import OptionParser

rame = 8

log = {
    'endpoint_url': 'https://fcu.eu-west-2.outscale.com',
    'AK': '79F67Z13CK5HY192067E',
    'SK': 'EG1W3ELHCK3N2S29W3YZCBG0RZ7AJWK53RHW53GH'
}

request = {
    'tina.c1r1': {
        'web': 100,
        'db': 1500,
        'rame': 1
    },
    'tina.c1r2': {
        'web': 300,
        'db': 4000,
        'rame': 2
    }
}

def init_connection():
    conn = init_connection(log)
    create_key_pair(conn)
    create_security_group(conn)
    vms = create_instance(conn)
    create_tag(conn, vms)
    link_eip_address(conn)
    deleteInstance(conn, 'linstance')

if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option('-k', '--key-pair', dest='key_name',
                      help='key_pair Name', default=None)
    parser.add_option('-s', '--security_group', dest='sg_group',
                      help='security_group name', default=None)
    parser.add_option('-n', '--tag_name', dest='tag_name',
                      help='tag name', default=None)
    parser.add_option('-t', '--vm_type', dest='vm_type',
                      help='type of vm', default=None)

    (options, args) = parser.parse_args()

    init_connection()

    while True:
        # bind udp avec incrémentation
