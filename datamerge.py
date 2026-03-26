hostnames = ["coreswitch1", "coreswitch2", "coreswitch3"]
ips = ["10.0.0.0", "10.0.0.1", "10.0.0.2"]
       
inventory = {}

#loop through the hostnames and ips and add them to the inventory dictionary
for i in range(len(hostnames)):
    name = hostnames[i]
    address = ips[i]

#add the hostname and ip address to the inventory dictionary
    inventory[name] = address

#print the inventory dictionary
print("final Inventory Dictionary")
print(inventory)
