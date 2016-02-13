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
    security_group.authorize('udp', 6660, 6660, 0.0.0.0)


def create_instance(conn):
    vms = conn.run_instances('ami-d0214875',
                             min_count='1',
                             max_count='1',
                             key_name=options.key_name,
                             instance_type=options.vm_type)
    return vms


def create_tag(conn, vms):
    instance = vms.instances[0]
    conn.create_tags([instance.id], {'Name': options.tag_name})
    instance.update()


def init_connection(log):
    conn = boto.connect_ec2_endpoint(log.endpoint_url, log.AK, log.SK)
    return conn




