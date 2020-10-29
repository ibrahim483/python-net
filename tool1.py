# import built-in os library
# https://docs.python.org/3/library/os.html

import os
#n=5
# Open file for saving ping results
results_file = open("results.txt", "w")

# Empty list to store ip addresses
ip_list = []

# Loop from 1 to 255
# Appends the concatenated ip to the ip_list
for ip in range(1, 41):
    ip_list.append("192.167.1." + str(ip))

# Print number of ip addresses in list
print(len(ip_list))
print(ip_list)

# Loop to ping ip_list and check if device up or down
# Outputs to results.txt file
#for x in range (1000):
for ip in ip_list:
    response = os.popen(f"ping -c 1 {ip}").read()
    if "1 received" in response:
        print(f"UP {ip} Ping Successful")
        results_file.write(f"UP {ip} Ping Successful" + "\n")
    else:
        print(f"Down {ip} Ping Unsuccessful")
        results_file.write(f"Down {ip} Ping Unsuccessful" + "\n")

# Close file when script completes
results_file.close()






