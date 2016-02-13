# !/usr/bin/env python
import boto
import sys
from requests import get
from main import log


def create_key_pair(conn):
    kp = conn.create_key_pair(options.key_name)
    kp.save('.')


def create_security_group(conn):
    ip_antho = '163.5.12.160'
    ip_nico = '163.5.12.103'
    ip_max = '163.5.12.55'
    ip_steve = '163.5.12.199'

    security_group = conn.create_security_group(options.sg_group, options.sg_group)
    security_group.authorize('tcp', 22, 22, ip_antho)
    security_group.authorize('tcp', 22, 22, ip_max)
    security_group.authorize('tcp', 22, 22, ip_nico)
    security_group.authorize('tcp', 22, 22, ip_steve)


def create_instance(conn, nb_rame):
    if nb_rame == 1:
        vms = conn.run_instances('ami-d0214875',
                             min_count='1',
                             max_count='1',
                             key_name=options.key_name,
                             instance_type='tina.c1r1')
    else:
        vms = conn.run_instances('ami-d0214875',
                             min_count='1',
                             max_count='1',
                             key_name=options.key_name,
                             instance_type='tina.c1r2')
    return vms


def create_tag(conn, vms):
    instance = vms.instances[0]
    conn.create_tags([instance.id], {'Name': 'web'})
    instance.update()


def init_connection(log):
    conn = boto.connect_ec2_endpoint(log.endpoint_url, log.AK, log.SK)
    return conn

def link_eip_address(conn):
    conn.associate_address(vms.instances[0][instance_id], '171.33.91.119', None)
