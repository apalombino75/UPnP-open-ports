# Python3 script to open UPnP port with user interaction
#It requires miniupnpc and requests to be installed

from ast import Try
from miniupnpc import UPnP
import ipaddress
from requests import get

#function to validate ip address format
def validate_ip_address(address):
    parts = address.split(".")
    print (parts)
    print (type(parts))

    if len(parts) != 4:
        print("IP address {} is not valid".format(address))
        return False

    for part in parts:
        if not isinstance(int(part), int):
            print("IP address {} is not valid".format(address))
            return False

        if int(part) < 0 or int(part) > 255:
            print("IP address {} is not valid".format(address))
            return False

        if int(parts[0])!=192 and int(parts[1])!=168 and int(parts[2])!=1 and int(parts[3])<=255:
            print ("IP address {} is not valid".format(address))
            return False

    print("IP address {} is valid".format(address))
    return True


upnp = UPnP()
# create a UPnP object
discovery_upnp = upnp.discover()
# discover IGD
selectigd = upnp.selectigd()
# select IGD
f=selectigd[7:18]
#get IGD IP address
g=f.split(".")
#get fields of IGD IP address
external_IP = get('https://ipapi.co/ip/').text # or get('https://api.ipify.org').text
# get public IP address by 3rd party
address_lan = upnp.lanaddr
# get local IP address

while True:
    try:
        eport = int(input("Type internal port  "))

        assert eport<65535 and eport>0

        break

    except ValueError:

        print("Please enter a number between 1 and 65535")


    except AssertionError:

        print("Please enter a number between 1 and 65535")



# while loop to validate internal port input

while True:

    try:
        iport = int(input("Type external port "))

        assert iport>1 and iport<65535

        break

    except ValueError:

        print("Please enter a number between 1 and 65535")


    except AssertionError:

        print("Please enter a number between 1 and 65535")


# while loop to validate external port input


while True:

    ipadd = input("Type an IP address of your network ")

    print (ipadd)

    #print(z[0])

    try:

        checkip = ipaddress.ip_address(ipadd)

        z=ipadd.split(".")

        assert (int(z[0]) == int(g[0]) and int(z[1]) == int(g[1]) and int(z[2]) == int(g[2]) and int(z[3]) < 255)

        break

    except ValueError:

        print("Enter a valid IP address format")

    except AssertionError:

        print ("Enter a valid IP belonging to your network")

# while loop to validate local IP address input

if discovery_upnp == True:

    add_port = upnp.addportmapping(eport, 'TCP', ipadd, iport, "test IGD Angelo", "")
    # add ports internal and external based on User Input

    print("public address" + "=" + external_IP)
    # print your public IP addres

    print("local address" + "=" + address_lan)
    # print your local IP address

    print("You have opened the following ports to the device with IP address  " + ipadd + " " + " ")
    # print the local IP address with UPnP ports opened
    print("internal open port" + "=" + str(iport) + "  " + "protocol" + " " + "TCP")
    # print port mapping details
    print("external open port" + "=" + str(eport) + "  " + "protocol" + " " + "TCP")
    # print port mapping details
else:
    print("UPnP disabled")

# if loop to add port mapping and print result

