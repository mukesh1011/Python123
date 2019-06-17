import time
from _datetime import datetime as dt

hosts_temp = "hosts"
hosts_path = "/etc/hosts"
redirect = "127.0.0.1"

website_list = ["www.faceboook.com", "facebook.com", "mail.yahoo.com"]

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 16):
        print("Working hours...")
        with open(hosts_temp, 'r+') as hostfile:
            content = hostfile.read()
            print(content)
            for website in website_list:
                if website in content:
                    pass
                else:
                    hostfile.write(redirect + " " + website + "\n")
    else:
        with open(hosts_temp, 'r+') as hostfile:
            content = hostfile.readline()
            hostfile.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    hostfile.write(line)
        print("Fun hours...")
    time.sleep(5)
