import boto
from requests import get
ip = get('https://api.ipify.org').text
ip_antho = '163.5.12.39'
ip_nico = '163.5.12.79'

endpoint_url = 'https://fcu.eu-west-2.outscale.com'


def first_vm():
   conn = boto.connect_ec2_endpoint(endpoint_url, access_key, secret_key)

   security_group = conn.create_security_group('sg_first_vm', 'sg_first_vm')
   security_group.authorize('tcp', 22, 22, ip_antho)
   security_group.authorize('tcp', 22, 22, ip_nico)
   security_group.authorize('tcp', 22, 22, ip)

   keypair = conn.create_key_pair('keypair_first_vm')
   keypair.save('~')

   vms = conn.run_instances('ami-d0214875',
                            min_count='1',
                            max_count='1',
                            key_name='keypair_first_vm',
                            security_group_ids=[security_group.id],
                            instance_type='t1.micro',
                            )

   instance = vms.instances[0]
   conn.create_tags(instance.id, {'Name': 'Girafe_first'})
   instance.update()


def second_vm():
   conn = boto.connect_ec2_endpoint(endpoint_url, access_key, secret_key)

   security_group = conn.create_security_group('sg_second_vm', 'sg_second_vm')
   security_group.authorize('tcp', 22, 22, ip_antho)
   security_group.authorize('tcp', 22, 22, ip_nico)
   security_group.authorize('tcp', 22, 22, ip)

   keypair = conn.create_key_pair('keypair_second_vm')
   keypair.save('~')

   vms = conn.run_instances('ami-d0214875',
                            min_count='1',
                            max_count='1',
                            key_name='keypair_second_vm',
                            security_group_ids=[security_group.id],
                            instance_type='t1.micro',
                            )

   instance = vms.instances[0]
   conn.create_tags(instance.id, {'Name': 'Girafe_second'})
   instance.update()

first_vm()
second_vm()
