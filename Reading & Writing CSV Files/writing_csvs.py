import csv

hosts = [["workstation.local", "192.168.25.46"], ["webserve.cloud", "10.2.5.6"]]

with open("host.csv", "w") as hosts_csv:
    writer = csv.writer(hosts_csv)

    writer.writerows(hosts)
    