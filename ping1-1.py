import os

results_file = open("results2.txt", "w")


with open('source-ip') as file:
	source = file.read()
	source = source.splitlines()
#	print (source)

with open('destination-ip') as file:
       des = file.read()
       des = des.splitlines()
#       print (des)
#for x in range (0, 1):
for ip in source :
	for ipd in des :
		os.system ('ping -c 2 -I ' + ip + ipd)
		response = os.popen(f"ping -c 1 -I {ip} {ipd}").read()
		print(response)
		if "1 received" in response:
			print(f"UP {ip} Ping Successful")
			results_file.write(f"UP {ip} Ping Successful" + "\n")
		else:
			print(f"Down {ip} Ping Unsuccessful")
			results_file.write(f"Down {ip} Ping Unsuccessful" + "\n")
#		print(response)
	print('********************************************************************** new source = ' + ip)


results_file.close()
#
#		print (ip)
#		print (des)
#	os.system('ping -c 4 ' + ip)
#############################################################

#for ipd in des:
#    response = os.popen(f"ping -c 1 {ipd}").read()
#    if "1 received" in response:
#        print(f"UP {ip} Ping Successful")
#        results_file.write(f"UP {ip} Ping Successful" + "\n")
#    else:
#        print(f"Down {ip} Ping Unsuccessful")
#        results_file.write(f"Down {ip} Ping Unsuccessful" + "\n")

# Close file when script completes
#results_file.close()
