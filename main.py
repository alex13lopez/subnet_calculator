#!/usr/bin/env python3
# -*- UTF-8 -*-

################################################################################################################################################
# Name: Subnet_Calculator
# Author: ArenGamerZ
# Email: arendevel@gmail.com
# Version: 0.3-beta
# Description: It's a tool that calculates the number of hosts, number of subnets, the network address, the broadcast address
#              from the given IP and MASK
# License GNU GPL, check out the full notice in LICENSE file
# Copyright (C) 2017 ArenGamerZ
################################################################################################################################################

import sys, argparse
from modules import interface

######### INITIALIZING VARS #########
ip_bin = None
ip_class = None
Nhosts = None
Nsubnets = None
NetAdd = None
BcastAdd = None
Csubnets = None
#####################################

if __name__ != "__main__":
    print(c.fcolors.RED+"This module is meant to be executed not imported!!!"+c.fcolors.RESET)
    exit(1)
else:
    parser = argparse.ArgumentParser(description=" It's a tool that calculates the number of hosts, number of subnets, the network address, the broadcast add from the given IP and MASK")
    parser.add_argument("-i", "--ip", dest="IP", required=True, help="IP Address")
    parser.add_argument("-m", "--mask", dest="MASK", required=True, help="MASK Address")
    parser.add_argument("-ib", "--ip_bin", action="store_true", help="Get the IP in binary representation")
    parser.add_argument("-c", "--class", dest="ip_class",action="store_true", help="Get the class of the given IP")
    parser.add_argument("-nh", "--nhosts", action="store_true", help="Get the number of hosts")
    parser.add_argument("-ns", "--nsubnets", action="store_true", help="Get the number of subnets")
    parser.add_argument("-na", "--netadd", action="store_true", help="Get the network address of the given IP")
    parser.add_argument("-bc", "--bcast", action="store_true", help="Get the broadcast address of the given IP")
    args = parser.parse_args()

    flags = []

    if args.ip_bin:
        flags.append("ip_bin")
    if args.ip_class:
        flags.append("ip_class")
    if args.nhosts:
        flags.append("Nhosts")
    if args.nsubnets:
        flags.append("Nsubnets")
    if args.netadd:
        flags.append("NetAdd")
    if args.bcast:
        flags.append("BcastAdd")

    interface.Main(args.IP, args.MASK, "simple", *flags)
