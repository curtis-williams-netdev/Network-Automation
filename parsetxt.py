with open('c:\\Users\\cwilliams\\Desktop\\VSCode\\Projects\\config.txt.txt', 'r') as f:
    config_lines = f.readlines()    

for line in config_lines:
    if line.startswith("Te") and "down" in line and "admin" not in line:
        print(line.strip())

for line in config_lines:
    if line.startswith("Te") and "down" in line and "admin" not in line:
        lines = line.split()
        print(f"Interface: {lines[0]} is down")
    
