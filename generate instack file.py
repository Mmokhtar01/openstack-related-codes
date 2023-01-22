import json

site_name = input("Please enter the site name and the DC name:")

blades = input("Please enter the rack number and blade numbers in format r?b? seprated by commas:").split(",")

mac_list = input("Please enter a list of MAC addresses separated by commas: ").split(",")
new_mac_list = []
for mac in mac_list:
    mac = mac.replace("-", "")
    new_mac = ":".join([mac[i:i+2] for i in range(0, len(mac),2)])
    new_mac_list.append(new_mac)
#mac_list = [':'.join([mac.replace("-", "")[i:i+2] for i in range(0, len(mac),2)]) for mac in mac_list]

ips = input("Please enter a list of IP addresses separated by commas: ").split(",")

scheduler_index= input("please enter the scheduler index start:")

name_index= input("please enter the name index start:")

un = input("Please enter the IPMI username:")
password = input("Please enter the IPMI Password:")

nodes_list = []
for i in range(len(mac_list)):
    node_dict = {
        "arch": "x86_64",
        "capabilities": "boot_option:local,node:computev5n40g-nfv-" + str((int(scheduler_index)+i)),
        "mac": [mac_list[i]],
        "name": str(site_name)+blades[i]+"ovsdpdkv5n40gcompute" + str((int(name_index)+i)),
        "pm_addr": ips[i],
        "pm_password": password,
        "pm_type": "pxe_ipmitool",
        "pm_user": un
    }
    nodes_list.append(node_dict)

data = {"nodes": nodes_list}
print(json.dumps(data, indent=4))