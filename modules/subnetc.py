#!/usr/bin/env python3

# License GNU GPL, check out the full notice in LICENSE file
# Copyright (C) 2017 ArenGamerZ

import sys
import bin_converter as bconverter

def Count(string, character):
    """ This function counts how many ocurrences of 'character' are in 'string' """
    count = 0
    for cc in string:
        if cc == character:
            count += 1
    return count


def DetClass(ip):
    """ This function determines whether the ip is class A, B, C, D or E
        Name of variables:
            fb_bin means first byte binary"""

    first_byte = str(ip.split('.')[0])
    fb_bin = bconverter.convert(first_byte)

    # We count the successive number of ones in the ip
    count = 0
    for i in range(4):
        if fb_bin[i] == "1":
            count += 1
        else:
            break

    # If the count it's equal to '0', that means it begins with a '0' which means it's an A class
    if count == 0:
        dclass = "A"
        dmask = "255.0.0.0"
    # If the count it's equal to '1', that means that it begins with a '1' but it's followed by a '0' which means it's a B class
    elif count == 1:
        dclass = "B"
        dmask = "255.255.0.0"
    # If the count it's equal to '2' that means there is '2' consecutive ones which means it's a C class.
    elif count == 2:
        dclass = "C"
        dmask = "255.255.255.0"
    # Same as above but with '3' ones which means it's a D class
    elif count == 3:
        dclass = "D"
        dmask = None # D class has no mask
    # If nothing of the above it's accomplished, that means that it has '4' or more ones which means it's an E class.
    else:
        dclass = "E"
        dmask = None # E class has no mask
    return dclass, dmask


def NumOfHosts(ip, masc):
    dclass, dmask = DetClass(ip)
    if bconverter.check(masc):
        # Continue here
        pass
    #return result
