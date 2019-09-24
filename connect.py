from openstack import connection
import time

conn = connection.Connection(
    region_name='RegionOne',
    auth=dict(
        auth_url='http://192.168.0.23:5000/v3',
        username='Rafael',
        password='cachorro',
        project_id='139b699e41f5463cbdccf14f691c722a',
        user_domain_id='0cf17c3ad2a548139f61c48911f75118'),
    compute_api_version='2',
    identity_interface='public')

#image = conn.create_image('bionic', filename='bionic.qcow2', wait=True)

# Find a flavor with at least 512M of RAM
flavor = conn.get_flavor_by_ram(1024)

print(flavor)

network = conn.network.find_network("RafaelNet")
# Boot a server, wait for it to boot, and then do whatever is needed
# to get a public ip for it.
conn.create_server('my-server', image='bionic', flavor=flavor, wait=True, auto_ip=True, network=network)
print("Lancou a instancia")
time.sleep(30)
conn.delete_server('my-server')
print("Deletou a instancia")
