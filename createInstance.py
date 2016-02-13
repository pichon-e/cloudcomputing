# !/usr/bin/env python

import boto
import sys
from requests import get

endpoint_url = 'https://fcu.eu-west-2.outscale.com'
AK = '79F67Z13CK5HY192067E'
SK = 'EG1W3ELHCK3N2S29W3YZCBG0RZ7AJWK53RHW53GH'

ip_antho = '163.5.12.160'
ip_nico = '163.5.12.103'
ip_max = '163.5.12.55'
ip_steve = '163.5.12.199'


def createKP(conn):
	kp = conn.create_key_pair(kname)
	kp.save('.')
	return kp


def init_connection():
	conn = boto.connect_ec2_endpoint(endpoint_url, AK, SK)
	return conn


def createSGroup(conn):
	security_group = conn.create_security_group(sg_group, sg_group)
	security_group.authorize('tcp', 22, 22, ip_antho)
	security_group.authorize('tcp', 22, 22, ip_max)
	security_group.authorize('tcp', 22, 22, ip_nico)
	security_group.authorize('tcp', 22, 22, ip_steve)


def createInstance(conn):
	vms = conn.run_instances('ami-d0214875', min_count='1', max_count='1', key_name='samedi', instance_type=IType)
	return vms


def createTag(conn, TName):
	instance = vms.instances[0]
	conn.create_tags([instance.id], {'Name': TName})
	instance.update()


if __name__ == '__main__':
	conn = init_connection()
	createKP(conn)
	createSGroup(conn)
	createInstance(conn)
	if len(sys.argv) > 1:
		createTag(conn, sys.argv[1])
	else:
		print "Need pareeribrz"
