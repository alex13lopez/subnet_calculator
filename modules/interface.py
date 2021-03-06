# -*- coding: utf-8 -*-


# License GNU GPL, check out the full notice in LICENSE file
# Copyright (C) 2017 ArenGamerZ

import sys
from . import colors as c
from . import subnetting as s
from . import bin_converter as bconverter

########## INITIALIZING NECESSARY VARS ###################
IP = None
MASK = None
ip_bin = None
ip_class = None
Nhosts = None
Nsubnets = None
NetAdd = None
BcastAdd = None
##########################################################

def Simple():

    # As the name of the function suggests, it's a simple interface with prints
    print("")
    if ip and mask:
        print(c.fcolors.MAGENTA+"IP: "+c.fcolors.CYAN+str(ip)+"/"+str(mask))
    if ip_class:
        print(c.fcolors.MAGENTA+"   - Class: "+c.fcolors.CYAN+str(ip_class[0]))
    if Nhosts:
        print(c.fcolors.MAGENTA+"   - Number of Hosts: "+c.fcolors.CYAN+str(Nhosts))
    if Nsubnets:
        print(c.fcolors.MAGENTA+"   - Number of Subnets: "+c.fcolors.CYAN+str(Nsubnets))
    if NetAdd:
        print(c.fcolors.MAGENTA+"   - Net Address: "+c.fcolors.CYAN+str(NetAdd))
    if BcastAdd:
        print(c.fcolors.MAGENTA+"   - Bcast Address: "+c.fcolors.CYAN+str(BcastAdd))
    if ip_bin:
        print(c.fcolors.MAGENTA+"   - IP in binary: "+c.fcolors.CYAN+str(ip_bin)+c.fcolors.RESET)
    print("")


def Main(ip, mask, iface, *flags):

    if not flags:
        raise AttributeError # We raise the AttributeError because no flag was supplied, so no job can be done

    globals()["ip"] = ip
    globals()["mask"] = mask

    values = {"ip_bin": bconverter.convert(ip), "ip_class": s.DetClass(ip), "Nhosts": s.NumOfHosts(mask), "Nsubnets": s.NumOfSubnets(ip, mask),
                "NetAdd": s.GetNetAddress(ip, mask), "BcastAdd": s.GetBcastAddress(ip, mask)}

    # We change the value of the vars on the fly
    for flag in flags:
        globals()[flag] = values[flag]

    # We call the interface indicated
    if iface == "simple":
        Simple()
    elif iface == "table":
        # Abandoned at the moment, seems rather complicated and tedious to do
        pass
