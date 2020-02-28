# Get public IP address

import os

def run():
    pub_ip = os.system("wget -qO - icanhazip.com")
    # TODO: how to get private ip address
    # $ ip link (show all interfaces)
    # parse text: get 2nd i.e. non-loopback if
    # $ ip addr show <2nd-if>
    # parse text: get ipv4 address
    # print ipv4-addrs

if (__name__ == '__main__'):
    run()