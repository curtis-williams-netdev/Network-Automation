import json

#example of reading a json file and printing the contents
json_data = ''' 
{
    "devices": [
        {"hostname": "switch1", "ip": "10.0.0.1"},
        {"hostname": "switch2", "ip": "10.0.0.2"},
        {"hostname": "switch3", "ip": "10.0.0.3"}
    ]
}
'''

#convert json string to python dictionary
data = json.loads(json_data)

#loop through the devices and print the hostname and ip
for device in data["devices"]:
    if device["hostname"] == "switch2":
        print(f"Hostname: {device['hostname']}, IP: {device['ip']}")
