#!/usr/bin/env python3
# -*- UTF-8 -*-

################################################################################################################################################
# Name: Subnet_Calculator
# Author: ArenGamerZ
# Email: arendevel@gmail.com
# Version: 0.4-beta
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
    parser.add_argument("-A", "--all", action="store_true", help="Activates all the flags")
    parser.add_argument("-b", "--ip_bin", action="store_true", help="Get the IP in binary representation")
    parser.add_argument("-c", "--class", dest="ip_class",action="store_true", help="Get the class of the given IP")
    parser.add_argument("-H", "--nhosts", dest="Nhosts", action="store_true", help="Get the number of hosts")
    parser.add_argument("-S", "--nsubnets", dest="Nsubnets", action="store_true", help="Get the number of subnets")
    parser.add_argument("-a", "--netadd", dest="NetAdd", action="store_true", help="Get the network address of the given IP")
    parser.add_argument("-B", "--bcast", dest="BcastAdd", action="store_true", help="Get the broadcast address of the given IP")
    parser.add_argument("-o", "--output", dest="FILE", help="Saves the output into <FILE>")
    parser.add_argument("-p", "--print", action="store_true", help="Prints to stdout in addition to outputting to file")
    parser.add_argument("-i", "--ip", dest="IP", required=True, help="IP Address")
    parser.add_argument("-m", "--mask", dest="MASK", required=True, help="MASK Address")
    args = parser.parse_args()

    opts = vars(args)
    if opts["all"] == True:
        for opt in opts:
            if opt not in ("all", "IP", "MASK", "FILE", "print"):
                opts[opt] = True


    flags = []
    for opt in opts:
        if opts[opt] == True and opt not in ("all", "IP", "MASK", "FILE", "print"):
            flags.append(opt)


    if opts["FILE"]:
        sys.stdout = open(opts["FILE"], "w")

    interface.Main(opts["IP"], opts["MASK"], "simple", *flags)

    if opts["FILE"] and opts["print"] == True:
        sys.stdout = sys.__stdout__
        file_saved = open(opts["FILE"], "r")
        print(file_saved.read(), end='')
        file_saved.close()
