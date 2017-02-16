#this python code is to telnet on cisco routers and make "show ip interface brief | in admin" and parse the output to get the admin down
# GigabitEthernet and Ethernet interfaces"
import re
from netmiko import ConnectHandler
from my_ccie_routers import P1, P2, P3, P4, PE1, PE2

def search_for_admin_down_interfaces(ip):
    """ this function is to collect all the admin down interfaces in the Network """
    connect = ConnectHandler(**router)
    hostname = re.findall(r'(\w+)>', str(connect.find_prompt()))
    output = str(connect.send_command('show ip int br | include admin'))
    admin_down_giga_interfaces = re.findall(r'(GigabitEthernet\d/\d)', output)
    admin_down_ethernet_interfaces = re.findall(r'(^Ethernet\d/\d)', output)
    print "\n# For Device with hostname : {0} and ip {1} #".format(hostname[0],ip)
    print '--------------------------------------------------------------------------'
    print 'these are the administrative down  interfaces  :'
    print admin_down_giga_interfaces
    print admin_down_ethernet_interfaces

routers = [P1, P2, P3, P4, PE1, PE2]
for router in routers:
    search_for_admin_down_interfaces(router['ip'])
