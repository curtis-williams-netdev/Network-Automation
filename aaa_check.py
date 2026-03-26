from netmiko import ConnectHandler
import netmiko
import re
import logging 

logging.basicConfig(filename='C:\\Users\\cwilliams\\Desktop\\VSCode\\Projects\\netmiko.log', level=logging.DEBUG)

myusername = "cwilliams"
mypassword = ""

labswitches = [
    {"device_type": "cisco_nxos", "host": "10.0.0.1", "username": myusername, "password": mypassword, "banner_timeout": 10, "port": 22, "use_keys": False}
]

#output patterns to seach for
pattern1 = r"aaa authentication login default group RADIUS local"
pattern2 = r"aaa authentication login default group RADIUS"

#store results
results = {}

for labswitch in labswitches:
    try:
        connection = netmiko.ConnectHandler(**labswitch)
        
        # Run the command
        output = connection.send_command("show run aaa")
        
        # Check for the specified configurations
        has_local = bool(re.search(pattern1, output))
        has_radius_only = bool(re.search(pattern2, output)) and not has_local
        
        # Store results
        results[labswitch['host']] = {
            "has_local": has_local,
            "has_radius_only": has_radius_only
        }
        
        # Close connection
        connection.disconnect()
    
    except Exception as e:
        print(f"Failed to connect to {labswitch['host']}: {e}")

# Output results
for host, config in results.items():
    if config["has_local"]:
        print(f"{host} has configuration for: aaa authentication login default group RADIUS local")
    elif config["has_radius_only"]:
        print(f"{host} has configuration for: aaa authentication login default group RADIUS")
    else:
        print(f"{host} has no relevant AAA authentication configuration.")


