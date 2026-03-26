import requests
import os
import netmiko 
from netmiko import ConnectHandler

# Base URL for the NetBox API - all requests will start with this
NETBOX_URL = os.environ.get("NETBOX_URL")

# Pull the NetBox API token from your OS environment variables
# This keeps your token out of the code so it's safe to push to GitHub
NETBOX_TOKEN = os.environ.get("NETBOX_TOKEN")

# Headers tell the API who you are and what format you're sending
# Authorization uses your token to authenticate the request
# Content-Type tells the API to expect JSON formatted data
headers = {
      "Authorization": f"Token {NETBOX_TOKEN}",
      "Content-Type": "application/json"
  }

# Params filter what devices get returned
# role limits results to only devices with that role slug in NetBox
# limit sets the max number of devices returned - 1000 covers most environments
params = {
      "role_id": "119",  # This is the role is for the network - switch role in NetBox - change as needed
      "limit": 1000
  }

# Send a GET request to the NetBox devices endpoint with our filters and auth headers
# The response comes back as raw HTTP data
response = requests.get(f"{NETBOX_URL}/dcim/devices/", headers=headers, params=params)

# Convert the raw response into a Python dictionary so we can work with it
data = response.json()

# Create an empty list to store our cleaned up device info
devices = []

# Loop through every device NetBox returned
for device in data["results"]:
    # Pull out only the fields we care about and add them as a dictionary to our list
    # platform uses the slug for a clean readable value - defaults to None if not set
    # ip strips the /prefix off the address (e.g. 10.0.0.1/24 becomes 10.0.0.1) - defaults to None if not set
    devices.append({
        "hostname": device["name"],
        "platform": device["platform"]["slug"] if device["platform"] else None,
        "ip": device["primary_ip4"]["address"].split("/")[0] if device["primary_ip4"] else None
    })

myusername = os.environ.get("NET_USERNAME")
mypassword = os.environ.get("NET_PASSWORD")

for device in devices:
    # skip devices with no IP
    if device["ip"] is None:
        continue
    # build the netmiko connection dict using data from NetBox
    connection_info = {
        "device_type": "cisco_nxos",
        "host": device["ip"],
        "username": myusername,
        "password": mypassword
    }
    # connect and run a command
    try:
        connection = netmiko.ConnectHandler(**connection_info)
        output = connection.send_command("show version")
        # write output to file
        with open("C:\\Users\\cwilliams\\Desktop\\VSCode\\Projects\\show_version_output.txt", "a") as f:
            f.write(f"{device['hostname']}\n")
            f.write(output + "\n")
        connection.disconnect()
    except Exception as e:
        print(f"Failed to connect to {device['hostname']}: {e}")