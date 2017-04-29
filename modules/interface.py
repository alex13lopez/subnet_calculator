# -*- UTF-8 -*-


# License GNU GPL, check out the full notice in LICENSE file
# Copyright (C) 2017 ArenGamerZ

import sys
from . import subnetting as s
from . import bin_converter as bconverter

########## INITIALIZING NECESSARY VARS ###################
ip = None
mask = None
ip_bin = None
ip_class = None
Nhosts = None
Nsubnets = None
NetAdd = None
BcastAdd = None
##########################################################

def Simple():

    # As the name of the function suggests, it's a simple interface with prints
    if ip_class:
        print("Class: "+str(ip_class[0]))
    if Nhosts:
        print("Nº of Hosts: "+str(Nhosts))
    if Nsubnets:
        print("Nº of Subnets: "+str(Nsubnets))
    if NetAdd:
        print("Net Address: "+str(NetAdd))
    if BcastAdd:
        print("Bcast Address: "+str(BcastAdd))
    if ip_bin:
        print("IP in binary: "+str(ip_bin))


def Main(ip, mask, iface, *flags):

    ######## Global Vars ########
    globals()[ip] = ip
    globals()[mask] = mask
    #############################

    values = {"ip_bin": bconverter.convert(ip), "ip_class": s.DetClass(ip), "Nhosts": s.NumOfHosts(mask), "Nsubnets": s.NumOfSubnets(ip, mask),
                "NetAdd": s.GetNetAddress(ip, mask), "BcastAdd": s.GetBcastAddress(ip, mask)}

    # We change the value of the vars on the fly
    for flag in flags:
        globals()[flag] = values[flag]

    # We call the interface indicated
    if iface == "simple":
        Simple()
    elif iface == "table":
        # In development
        pass
