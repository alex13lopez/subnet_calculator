#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################################################################################
# Name: Subnet_Calculator
# Author: ArenGamerZ
# Email: arendevel@gmail.com
# Version: 1.3-beta
# Description: It's a tool that calculates the number of hosts, number of subnets, the network address, the broadcast address
#              from the given IP and MASK
# License GNU GPL, check out the full notice in LICENSE file
# Copyright (C) 2017 ArenGamerZ
################################################################################################################################################


try:
    import sys, argparse, colorama
    from modules import interface
    from modules import colors as c

except ModuleNotFoundError:
    print("Fatal Error: Make sure you meet all the requirements")
    exit(1)

finally:
    colorama.init()

######### INITIALIZING VARS #########
ip_bin = None
ip_class = None
Nhosts = None
Nsubnets = None
NetAdd = None
BcastAdd = None
#####################################

if __name__ != "__main__":
    print(c.fcolors.RED+"This module is meant to be executed not imported!!!"+c.fcolors.RESET)
else:
    try:
        parser = argparse.ArgumentParser(description=" It's a tool that calculates the number of hosts, number of subnets, the network address, the broadcast add from the given IP and MASK")
        parser.add_argument("-a", "--all", dest="ALL", action="store_true", help="Activates all the flags, except for ip_bin")
        parser.add_argument("-b", "--ip_bin", action="store_true", help="Shows the IP in binary representation")
        parser.add_argument("-C", "--class", dest="ip_class",action="store_true", help="Get the class of the given IP")
        parser.add_argument("-H", "--nhosts", dest="Nhosts", action="store_true", help="Get the number of hosts")
        parser.add_argument("-S", "--nsubnets", dest="Nsubnets", action="store_true", help="Get the number of subnets")
        parser.add_argument("-A", "--netadd", dest="NetAdd", action="store_true", help="Get the network address of the given IP")
        parser.add_argument("-B", "--bcast", dest="BcastAdd", action="store_true", help="Get the broadcast address of the given IP")
        parser.add_argument("-i", "--input", dest="IFILE", help="Takes the input of <IFILE> instead of stdin. The file must have the form of IP/MASK per line like stdin")
        parser.add_argument("-o", "--output", dest="OFILE", help="Saves the output into <OFILE>")
        parser.add_argument("-p", "--print", dest="PRINT", action="store_true", help="Prints to stdout in addition to outputting to file")
        parser.add_argument("IP/MASK", type=str, nargs="?", help="IP Address/Mask")
        args = parser.parse_args()

        opts = vars(args)
        if opts["ALL"] == True:
            for opt in opts:
                if opt not in ("ALL", "ip_bin", "IP/MASK", "IFILE", "OFILE", "PRINT"):
                    opts[opt] = True


        flags = []
        for opt in opts:
            if opts[opt] == True and opt not in ("ALL", "IP/MASK", "IFILE", "OFILE", "PRINT"):
                flags.append(opt)


        if opts["OFILE"]:
            sys.stdout = open(opts["OFILE"], "w")

        if opts["IFILE"]:
            with open(opts["IFILE"], "r") as lines:
                for line in lines:
                    line = line[:-1] # To remove the trailing newline character
                    ip, mask = line.split("/")
                    interface.Main(ip, mask, "simple", *flags)
        else:
            ip, mask = opts["IP/MASK"].split("/")
            interface.Main(ip, mask, "simple", *flags)

        if opts["OFILE"] and opts["PRINT"] == True:
            sys.stdout = sys.__stdout__
            file_saved = open(opts["OFILE"], "r")
            print(file_saved.read(), end='')
            file_saved.close()


    except (ValueError, IndexError):
        print(c.fcolors.RED+"The IP or the MASK are not valid")
    except (AttributeError):
        print(c.fcolors.RED+"No argument supplied! Try '-h' to see available arguments!")
    except TypeError:
        # The default mask not exists because either it's a D or E class
        print(c.fcolors.RED+"The given IP is either a D or E class, thus, it can't be used for subnetting!")
