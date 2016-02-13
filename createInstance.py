import boto
from requests import get

endpoint_url = 'https://fcu.eu-west-2.outscale.com'
AK = 79F67Z13CK5HY192067E
SK = EG1W3ELHCK3N2S29W3YZCBG0RZ7AJWK53RHW53GH

ip_antho = '163.5.12.160'
ip_nico = '163.5.12.103'
ip_max = '163.5.12.99'
ip_steve = '163.5.12.199'

def createKP():
	kp = conn.create_key_pair(kname)
	kp.save('.')

def createConn():
	conn = boto.connect_ec2_endpoint(endpoint_url, AK, SK)

def createSGroup():
	security_group = conn.create_security_group(sg_group, sg_group)
	security_group.authorize('tcp', 22, 22, ip_antho)
	security_group.authorize('tcp', 22, 22, ip_max)
	security_group.authorize('tcp', 22, 22, ip_nico)
	security_group.authorize('tcp', 22, 22, ip_steve)

def createInstance():
	vms = conn.run_instances('ami-d0214875', min_count='1', max_count='1', key_name='samedi', instance_type=IType)

def createTag():
	instance = vms.instances[0]
	conn.create_tags([instance.id], {'Name': TName})
	instance.update()


