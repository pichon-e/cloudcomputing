# !/usr/bin/env python
import boto
import sys
from requests import get
from optparse import OptionParser

endpoint_url = 'https://fcu.eu-west-2.outscale.com'
AK = '79F67Z13CK5HY192067E'
SK = 'EG1W3ELHCK3N2S29W3YZCBG0RZ7AJWK53RHW53GH'


def createKP(conn):
    kp = conn.create_key_pair(options.key_name)
    kp.save('.')


def init_connection():
    conn = boto.connect_ec2_endpoint(endpoint_url, AK, SK)
    return conn


def createSGroup(conn):
    ip_antho = '163.5.12.160'
    ip_nico = '163.5.12.103'
    ip_max = '163.5.12.55'
    ip_steve = '163.5.12.199'

    security_group = conn.create_security_group(options.sg_group, options.sg_group)
    security_group.authorize('tcp', 22, 22, ip_antho)
    security_group.authorize('tcp', 22, 22, ip_max)
    security_group.authorize('tcp', 22, 22, ip_nico)
    security_group.authorize('tcp', 22, 22, ip_steve)


def createInstance(conn):
    vms = conn.run_instances('ami-d0214875',
                             min_count='1',
                             max_count='1',
                             key_name='samedi',
                             instance_type=options.vm_type)
    return vms


def createTag(conn):
    instance = vms.instances[0]
    conn.create_tags([instance.id], {'Name': options.tag_name})
    instance.update()


if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option('-k', '--key-pair', dest='key_name',
                      help='key_pair Name', default=None)
    parser.add_option('-s', '--security_group', dest='security_group',
                      help='security_group name', default=None)
    parser.add_option('-t', '--tag_name', dest='tag_name',
                      help='tag name', default=None)
    parser.add_option('-type', '--vm_type', dest='vm_type',
                          help='type of vm', default=None)

    (options, args) = parser.parse_args()
