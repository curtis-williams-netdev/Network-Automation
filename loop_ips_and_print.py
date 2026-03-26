#loop through a list of ip's and print them

#list the ip's to loop through
ips = ["10.0.0.1", "10.0.0.2", "10.0.0.3"]

#for loop to print each ip
for ip in ips:
    if ip.endswith(".3"):
         print(ip)
